"""
50. Pow(x, n)  (Medium)
https://leetcode.com/problems/powx-n/

Pattern:    fast power (divide and conquer): x^n = (x^(n//2))^2, times x if n is odd
Key idea:
  - n == 0 -> 1
  - n < 0 -> 1 / myPow(x, -n): take the reciprocal at the END, not x = 1 / x first
  - one recursive call per level -> no memo needed, O(log n)
Complexity: O(log n) time, O(log n) recursion depth
Mistake I made (v1):
  - x = 1 / x first: the tiny rounding error in 1/x is a relative error in the BASE,
    and raising to the n-th power multiplies it by n (~1.7e9) -> 191.06372 vs 191.06370
  - an unneeded memo dict (each call recurses only once)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)

        half = self.myPow(x, n // 2)
        if n % 2 == 1:
            return half * half * x
        else:
            return half * half
