"""
73. Set Matrix Zeroes  (Medium)
https://leetcode.com/problems/set-matrix-zeroes/

Pattern:    in-place marker storage, clue: "do it in place" + follow-up "O(1) space"
Key idea:
  - first row/col are the flags: matrix[0][c] == 0 -> zero column c, matrix[r][0] == 0 -> zero row r
  - save "did row 0 / col 0 have a zero?" in two booleans BEFORE marking
  - decode the inner cells first, then apply the two booleans last
  - path there: copy O(mn) -> row/col sets O(m+n) -> reuse first row/col O(1)
Complexity: O(m*n) time, O(1) extra space
Mistake I made:
  - decode loops started at 0, so they read markers I had just written
  - lesson: check the code against my own plan (the plan said skip row/col 0)
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
        first_col_zero = any(matrix[r][0] == 0 for r in range(rows))

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0
        
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0

