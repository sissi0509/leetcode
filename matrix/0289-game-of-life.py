"""
<number>. <Problem Title>  (<Easy|Medium|Hard>)
https://leetcode.com/problems/<problem-slug>/

Pattern:    <technique>, clue: "<what in the problem points to it>"
Key idea:   <1-2 sentences, plain words, as if explaining to a friend>
Complexity: O(?) time, O(?) space
Mistake I made: <optional>
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

