"""
1131. Maximum of Absolute Value Expression  (Medium)
https://leetcode.com/problems/maximum-of-absolute-value-expression/

Pattern:    remove absolute values by trying every sign choice, then split into f(i) - f(j)
            clue = a sum of |x_i - x_j| terms maximized over pairs (Manhattan-style distance)
Key idea:
  - |x| = max(x, -x)  ->  |p| + |q| + |r| = max over sign choices of (+-p +-q +-r)
  - symmetry (swap i, j) -> assume i >= j, so |i - j| = i - j; only 4 sign pairs (s1, s2) left
  - regroup: s1*(a_i - a_j) + s2*(b_i - b_j) + (i - j) = f(i) - f(j),
    f(k) = s1*a_k + s2*b_k + k   -> the pair disappears
  - max over pairs of f(i) - f(j) = max(f) - min(f), one pass
  - no need to enforce i >= j: a signed term is never bigger than its |.|, so a "wrong" pair
    can't overshoot, and the best pair is hit exactly by its right sign choice
  - same idea as the Manhattan rotation u = x + y, v = x - y ("Jobs and Techs", 2026-11-08)
Complexity: O(n) time (4 passes), O(n) space (O(1) with running max/min)
Mistake I made: couldn't see the regroup into f(i) - f(j); saw the i >= j symmetry myself; code shown
"""


class Solution:
    def maxAbsValExpr(self, arr1: list[int], arr2: list[int]) -> int:
        res = 0
        for s1, s2 in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            f = [s1 * a + s2 * b + i for i, (a, b) in enumerate(zip(arr1, arr2))]
            res = max(res, max(f) - min(f))
        return res
