"""
4. Median of Two Sorted Arrays  (Hard)
https://leetcode.com/problems/median-of-two-sorted-arrays/

Pattern:    Binary search on a partition (a cut), clue: "O(log (m+n))", two sorted arrays
Key idea:
  - cut both arrays so the two left parts together are the smaller half:
    left half size = (m + n + 1) // 2 (odd total -> the left half has the extra one)
  - a cut is a COUNT (how many go left), not an index; choose only the cut in A, B's follows
  - search the shorter array so B's cut never goes out of range
  - correct cut: a_left <= b_right and b_left <= a_right (each array is sorted already);
    a missing left neighbor is -inf, a missing right neighbor is +inf
  - a_right < b_left -> too few from A -> l = cut + 1; b_right < a_left -> too many -> r = cut - 1
  - returns inside the loop -> closed template (l <= r, drop mid)
  - median: odd -> max of the lefts; even -> (max of lefts + min of rights) / 2
Complexity: O(log min(m, n)) time, O(1) space
Mistake I made:
  - 08-18: 3 bugs, never solved. 10-16 retype: `while l < r` (returned None), b_left defaulted
    to +inf instead of -inf, and // 2 instead of / 2 for the even median
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A
        m, n = len(A), len(B)
        single = (m + n) % 2 != 0

        half = (len(A) + len(B) + 1) // 2
        l, r = 0, m

        while l <= r:
            a_m = (l + r) // 2
            b_m = half - a_m

            a_left = A[a_m - 1] if a_m - 1 >= 0 else float('-inf')
            a_right = A[a_m] if a_m < m else float('inf')
            b_left = B[b_m - 1] if b_m - 1 >= 0 else float('-inf')
            b_right = B[b_m] if b_m < n else float('inf')

            if a_right < b_left:
                l = a_m + 1
            elif b_right < a_left:
                r = a_m - 1
            else:
                if single:
                    return max(a_left, b_left)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
