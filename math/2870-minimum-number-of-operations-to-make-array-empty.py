"""
2870. Minimum Number of Operations to Make Array Empty  (Medium)
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

Pattern:    Count by group (Counter) + a per-count formula; clue: each operation removes
            2 or 3 EQUAL elements, so every value is its own independent subproblem
Key idea:
  - Counter(nums): each value's count c is solved separately, then the answers are SUMMED
  - c == 1 -> impossible -> return -1
  - otherwise ceil(c / 3) = (c + 2) // 3:
      use as many 3s as possible; leftover 2 -> one more op; leftover 1 -> trade one 3
      for two 2s (3 + 1 = 2 + 2), also one more op
  - how to find the formula: write the DP ops(c) = 1 + min(ops(c-3), ops(c-2)), fill it
    by hand for c = 2..12 -> 1 1 | 2 2 2 | 3 3 3 | 4 4 4 -> up by 1 every 3 -> ceil(c/3)
  - ceil(a / b) == (a + b - 1) // b for positive ints (exact, no floats)
Complexity: O(n) time, O(n) space (the Counter)
Mistake I made:
  - went straight to memoized recursion; filling a small table first shows the formula
  - memo stored the running total passed down from the top call (`cnt`), so a reused key
    returned another path's total -> a memo value must depend only on its key
  - combined the groups with max instead of sum; started res at -1
  - no base case for negative numbers (4 -> 1 -> -2 -> ... forever)
"""

from collections import Counter


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        res = 0
        for c in Counter(nums).values():
            if c == 1:
                return -1
            res += (c + 2) // 3
        return res
