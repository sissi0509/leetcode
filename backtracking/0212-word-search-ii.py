"""
212. Word Search II  (Hard)
https://leetcode.com/problems/word-search-ii/

Pattern:    Trie + backtracking DFS on a grid, clue: Word Search I, but many words at once
Key idea:
  - running Word Search I once per word repeats the same grid walks for shared prefixes
  - put all words in a trie; one DFS from every cell walks the board and the trie together
  - stop a path as soon as the next letter isn't a child of the current trie node
  - ONE guard at the top of dfs (bounds + letter in parent.children); '#' is never a child,
    so visited cells are skipped by the same check, and no call site needs its own check
  - the node at the end of a word stores the word itself (non-empty `word` = a word ends here)
  - found a word -> append it, then clear node.word, so no path can add it twice (no set needed)
  - mark the cell '#' before recursing, restore it after (a path can't reuse a cell)
  - prune: after the loop, if the node has no children and no word, delete it from its PARENT
    (`del parent.children[ch]`). True exactly when every word under this node is found.
    It runs on the way back up, so deletions cascade toward the root.
Complexity: O(m * n * 4 * 3^(L-1)) time worst case (L = longest word), O(total letters) trie space;
            pruning makes later searches skip finished branches (about 3x faster on an all-'a' board)
Mistake I made:
  - 2026-09-15: `TrieNode` without (), undefined `col`, appended a stale `word` variable
  - 2026-10-10 v1: `TrieNode` without () again (3rd time), forgot to restore the cell,
    each word appended 4 times (one per neighbor call) -> fixed with a set
  - 2026-10-10 pruned rewrite:
      * `res.append(word)`: `word` was the leftover loop variable from building the trie
        (always the last word) -> must be `node.word`. Same bug as 09-15.
      * `del node` only deletes the local name; the trie still holds the node
        -> `del parent.children[ch]` (that's why dfs gets the parent)
      * outer loop called dfs on every cell, but dfs starts with parent.children[ch]
        -> KeyError; final version moves the one guard to the top of dfs
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.word = word


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        trie = Trie()
        for word in words:
            trie.add_word(word)

        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(r, c, parent):
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] not in parent.children:
                return

            ch = board[r][c]
            node = parent.children[ch]

            if node.word:
                res.append(node.word)
                node.word = ""

            board[r][c] = '#'
            for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nr, nc = dr + r, dc + c
                dfs(nr, nc, node)
            board[r][c] = ch

            if not node.children and not node.word:
                del parent.children[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie.root)

        return list(res)
