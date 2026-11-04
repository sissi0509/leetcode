"""
416. Partition Equal Subset Sum  (Medium)
https://leetcode.com/problems/partition-equal-subset-sum/

Pattern:    0/1 knapsack (subset sum) DP; clue = "pick some items, each at most once,
            hit an exact total" + small total (n <= 200, values <= 100 -> half <= 10,000)
Key idea:
  - odd total -> False right away; else target = total // 2
  - dp[s] = some subset of the numbers seen so far sums to s; dp[0] = True
  - each num: skip it (dp[s]) or take it (dp[s - num])
  - copy the row (prev) so each num is used once; no-copy version: loop s from target DOWN to num
  - early exit as soon as dp[target] is True
Complexity: O(n * target) time, O(target) space
Mistake I made (v1):
  - first plan was greedy: sort + prefix sums -> fails on [1, 2, 3, 4] (5 = 1 + 4)
  - didn't recognize DP: brute force is 2^n take/skip, but many subsets share the same sum
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            prev = dp[:]
            for i in range(num, target + 1):
                dp[i] = prev[i - num] or prev[i]
            if dp[-1]:
                return True

        return dp[-1]
