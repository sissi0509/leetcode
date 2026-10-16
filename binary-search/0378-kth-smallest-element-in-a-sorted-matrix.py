"""
378. Kth Smallest Element in a Sorted Matrix  (Medium)
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Pattern:    Binary search on the VALUE range + counting, clue: rows and columns sorted, "kth smallest"
Key idea:
  - search values lo = matrix[0][0] .. hi = matrix[-1][-1], not indexes
  - check: count of elements <= mid, in O(n) with a staircase walk from the bottom-left:
    cell <= mid -> it and everything above it count (row + 1), move right; else move up
  - count(mid) >= k means "the kth smallest is <= mid" -> keep mid (hi = mid): first T
  - >= not >: with duplicates ([[1,2],[2,3]], k=2) count(2) = 3 > k but 2 is the answer
  - mid may not be in the matrix; that's fine, it's only a question. The FIRST T is always a
    matrix value, because the count only changes at matrix values
  - heap alternative: k-way merge of the rows (like LC23), O(k log n) time, O(n) space
Complexity: O(n log(max - min)) time, O(1) space
Mistake I made:
  - wrote r / l instead of hi / lo (new variables, infinite loop); used > k instead of >= k
  - heap version: hp = heapq.heapify(hp) -> heapify works in place and returns None
"""

import heapq


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        def cnt_less(num):
            # counts elements <= num
            cnt = 0
            row, col = rows - 1, 0
            while row >= 0 and col < cols:
                if matrix[row][col] <= num:
                    cnt += row + 1
                    col += 1
                else:
                    row -= 1

            return cnt

        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            if cnt_less(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo


class SolutionHeap:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        hp = [(matrix[r][0], r, 0) for r in range(n)]   # first element of each row
        heapq.heapify(hp)                               # in place, returns None
        for _ in range(k - 1):                          # pop the k - 1 smallest
            val, r, c = heapq.heappop(hp)
            if c + 1 < n:
                heapq.heappush(hp, (matrix[r][c + 1], r, c + 1))
        return hp[0][0]
