"""
377. Combination Sum IV  (Medium)
https://leetcode.com/problems/combination-sum-iv/

Pattern:    1-D DP / memoized DFS, clue: COUNT the ways (not list them),
            and order matters (1,2) != (2,1), despite the name "combination"
Key idea:
  - same as climbing stairs (LC70) with step sizes nums: to reach total,
    the LAST number was some num, so before it the sum was total - num
  - dfs(total) = number of ways to reach total from 0
      * total == 0 -> 1 (the empty sequence: already there, one way)
      * otherwise sum dfs(total - num) for every num <= total
  - memo: check before the work, SAVE before returning (forgetting the save = still slow)
  - backtracking that only counts (res += 1) is exponential: the same total gets reached
    by many paths, and the answer depends only on total -> memoize
  - bottom-up table is the same thing: dp[i] += dp[i - num]
      * sum OUTER, nums inner -> permutations (this problem)
      * nums OUTER, sum inner -> combinations (Coin Change II, LC518)
  - negative numbers: the count can be infinite unless the length is bounded
Complexity: O(target * n) time, O(target) space
Mistake I made:
  - first DP had nums as the outer loop -> counted combinations (4 instead of 7)
  - solved with help: needed the stairs picture to see why dp counts orders
"""


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        memo = {}

        def dfs(total):
            if total == 0:
                return 1
            if total in memo:
                return memo[total]

            ways = 0
            for num in nums:
                if num <= total:
                    ways += dfs(total - num)

            memo[total] = ways
            return ways

        return dfs(target)
