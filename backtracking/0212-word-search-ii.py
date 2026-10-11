"""
212. Word Search II  (Hard)
https://leetcode.com/problems/word-search-ii/

Pattern:    Trie + backtracking DFS on a grid, clue: Word Search I, but many words at once
Key idea:
  - running Word Search I once per word repeats the same grid walks for shared prefixes
  - put all words in a trie; one DFS from every cell walks the board and the trie together
  - stop a path as soon as the next letter isn't a child of the current trie node
  - the node at the end of a word stores the word itself, so no string is built during DFS
  - mark the cell '#' before recursing, restore it after (a path can't reuse a cell)
  - the same word can be found by many paths -> collect into a set
    (standard alternative: clear the node's word after the first hit)
  - here `is_word` is checked BEFORE the bounds check, so a word ending at the board's edge
    is still recorded when dfs steps off the board
Complexity: O(m * n * 4 * 3^(L-1)) time worst case (L = longest word), O(total letters) trie space
Speed-up worth mentioning: after a word is found, delete trie leaves that no longer lead to any
word, so later searches skip dead branches (about 3x faster on an all-'a' board)
Mistake I made:
  - 2026-09-15: `TrieNode` without (), undefined `col`, appended a stale `word` variable
  - 2026-10-10: `TrieNode` without () again (3rd time overall), forgot to restore the cell,
    each word appended 4 times (one per neighbor call) -> switched to a set
"""


class TrieNode:
    def __init__(self, word=""):
        self.children = {}
        self.is_word = False
        self.word = word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.is_word = True
        cur.word = word

    def find_word(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return cur.is_word


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        trie = Trie()
        for word in words:
            trie.add_word(word)

        rows = len(board)
        cols = len(board[0])
        res = set()

        def dfs(r, c, node):
            if node.is_word:
                res.add(node.word)

            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] not in node.children:
                return

            temp = board[r][c]
            board[r][c] = '#'

            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = dr + r, dc + c
                dfs(nr, nc, node.children[temp])

            board[r][c] = temp

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)

        return list(res)
