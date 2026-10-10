"""
213. House Robber II  (Medium)
https://leetcode.com/problems/house-robber-ii/

Pattern:    1-D DP (House Robber I on two ranges), clue: "adjacent" + "maximum" + houses in a circle
Key idea:
  - the circle only adds one rule: the first and the last house can't both be robbed
  - so run the plain line DP twice and take the max:
      houses 1..n-1 (first house out) and houses 0..n-2 (last house out)
  - line DP: dp[i] = max money from houses 0..i, robbed or not
      dp[i] = max(dp[i-1], dp[i-2] + nums[i])   (rob i -> skip i-1)
  - dp[i] only looks back two steps -> keep two variables (prev, cur), not an array
  - edge case: one house -> both ranges are empty and return 0, so return nums[0]
Complexity: O(n) time, O(1) extra space (O(n) for the slices; pass indices to avoid it)
Mistake I made:
  - first version: two full dp arrays + a special `if i == 1` inside the loop (correct, not clean)
  - rewrite: forgot the len(nums) == 1 check, so [x] returned 0
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.rob_line(nums[1:]), self.rob_line(nums[:-1]))

    def rob_line(self, houses) -> int:
        prev, cur = 0, 0

        for money in houses:
            prev, cur = cur, max(cur, prev + money)

        return cur
