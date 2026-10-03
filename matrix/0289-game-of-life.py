"""
289. Game of Life  (Medium)
https://leetcode.com/problems/game-of-life/

Pattern:    in-place state encoding, clue: "update simultaneously" + "in place"
Key idea:   Each cell needs its neighbours' OLD values, so encode old + new state
            together: 2 = live -> dead, 3 = dead -> live (0 and 1 unchanged).
            A neighbour was originally live if it is 1 or 2; unvisited cells still
            hold 0/1, so the same check works. A second pass decodes 2 -> 0, 3 -> 1.
Complexity: O(m*n) time, O(1) extra space
Follow-ups: bitmask version (bit 0 = old, bit 1 = new, decode with >>= 1);
            infinite board -> store only a set of live (r, c) cells + Counter.
"""

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # < 2 or > 3: 1->0,  2
        # 2-3: 1->1,  1
        # = 3: 0 -> 1, 3
        # other: 0->0, 0
        
        rows = len(board)
        cols = len(board[0])
        dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        def count_live_neighbour(r, c):
            cnt = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] in (1, 2):
                        cnt += 1
            
            return cnt
        
        for r in range(rows):
            for c in range(cols):
                nei = count_live_neighbour(r, c)
                if board[r][c] == 1:
                    if nei < 2 or nei > 3:
                        board[r][c] = 2
                elif nei == 3:
                    board[r][c] = 3
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1

