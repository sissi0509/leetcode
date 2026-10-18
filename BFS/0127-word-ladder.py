"""
127. Word Ladder  (Hard)
https://leetcode.com/problems/word-ladder/

Pattern:    BFS on an implicit graph, clue: "shortest" + every step costs 1 (unweighted)
            -> BFS, not DFS (all paths, exponential) and not Dijkstra (no weights)
Key idea:
  - pattern map: for every word and every position, mask that letter with "*"
      "hot" -> "*ot", "h*t", "ho*"; words sharing a pattern differ in exactly one letter
  - the pattern map IS the graph: neighbors are looked up on the fly, no explicit edges
    (a pattern shared by m words would need m^2 edges)
  - BFS level by level; the first time endWord is popped, that level is the answer
  - visited is on patterns: each pattern is expanded once (same effect as clearing it after use)
    a word can still be queued more than once; still correct, a word-level visited set trims it
Complexity: O(N * L^2) time (N * L patterns, each built by an O(L) slice), O(N * L^2) space for the map
Mistake I made:
  - first plan: DFS + keep the smaller step count -> exponential, and a visited set breaks it
  - next idea: explicit graph + Dijkstra -> works, but every edge costs 1, so BFS is enough
  - v1 pattern = word[:i] + word[i + 1:] (deleted the letter, no "*") -> patterns from different
    positions collide: "abc" and "bcd" both give "bc" -> returned 2 instead of 0
"""

from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList or endWord == beginWord:
            return 0

        pattern_map = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_map[pattern].append(word)

        visited = set()
        first_level = []
        for i in range(len(beginWord)):
            pattern = beginWord[:i] + "*" + beginWord[i + 1:]
            first_level.extend(pattern_map[pattern])
            visited.add(pattern)

        queue = deque(first_level)

        level = 2
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return level
                for i in range(len(word)):
                    new_pattern = word[:i] + "*" + word[i + 1:]
                    if new_pattern not in visited:
                        visited.add(new_pattern)
                        queue.extend(pattern_map[new_pattern])
            level += 1

        return 0
