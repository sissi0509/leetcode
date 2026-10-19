"""
208. Implement Trie (Prefix Tree)  (Medium)
https://leetcode.com/problems/implement-trie-prefix-tree/

Pattern:    trie = tree of dicts, one edge per character; is_word marks where a word ends
Key idea:
  - TrieNode: children dict {ch: TrieNode} + is_word flag
  - insert: walk down, create missing children, mark the last node is_word
  - _walk(s): shared helper, returns the node at the end of s or None if the path breaks
      search(word)       -> the path exists AND ends at a word
      startsWith(prefix) -> the path exists
Complexity: insert / search / startsWith O(L) time, L = word length;
            insert adds up to L nodes, so total space O(total characters inserted)
Mistake I made:
  - insert: cur = cur.children (stepped into the dict, not the child node) -> AttributeError
  - startsWith called _walk(word) instead of _walk(prefix) (copy-paste slip) -> NameError
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]

        cur.is_word = True

    def _walk(self, word: str) -> TrieNode:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                return None
            cur = cur.children[ch]

        return cur

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None
