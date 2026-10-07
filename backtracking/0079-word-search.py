"""
79. Word Search  (Medium)
https://leetcode.com/problems/word-search/

Pattern:    backtracking DFS on a grid, clue: "adjacent cells" + "same cell may not be used twice"
Key idea:
  - try every cell as a start; dfs(r, c, i) = can word[i:] be spelled starting at (r, c)?
  - i == len(word) -> True (checked first, so a full match never needs a valid cell)
  - out of bounds, or letter != word[i] -> False (bounds check BEFORE board[r][c])
  - mark the cell used ('#') before recursing, restore it after: that undo is the backtracking
  - '#' never matches a letter, so the same check also blocks reuse
  - no memo: a False at (r, c, i) depends on which cells this path already used
Speed-ups (in the code; same worst case, much faster in practice):
  - if any letter appears more often in word than on the board -> False before searching
  - if the last letter is rarer on the board than the first, search the reversed word
Complexity: O(m * n * 3^L) time (4 directions at the first step, then 3), O(L) recursion space
Mistake I made:
  - first try: forgot to mark the visited cell with '#', so the path reused cells
"""

from collections import Counter


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        n = len(word)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        board_cnt = Counter(ch for row in board for ch in row)
        word_cnt = Counter(word)

        for ch, cnt in word_cnt.items():
            if cnt > board_cnt[ch]:
                return False

        if board_cnt[word[0]] > board_cnt[word[-1]]:
            word = word[::-1]

        def dfs(r, c, i):
            if i == n:
                return True

            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, i + 1):
                    return True

            board[r][c] = temp

            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
