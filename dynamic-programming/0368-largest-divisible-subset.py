"""
368. Largest Divisible Subset  (Medium)
https://leetcode.com/problems/largest-divisible-subset/

Pattern:    1-D DP like LIS + path reconstruction, clue: "every pair: one divides the other",
            and the answer is the subset itself, not its size
Key idea:
  - sort first: a number's divisors are smaller, so they always come before it
  - after sorting, a divisible subset = a chain where each number divides the next
    (a | b and b | c -> a | c, so every pair works)
  - dp[i] = length of the longest chain ENDING at nums[i]
    = 1 + max dp[j] over earlier j where nums[j] divides nums[i]   (LIS with "divides" for "<")
  - prev[i] = the j that gave that best chain -> save where each answer came from
  - rebuild: start at the index with the biggest dp, follow prev back to -1, reverse
  - "attach to the largest previous divisor" is wrong: [1,2,4,8,9,72] -> 9's chain is short
Complexity: O(n^2) time, O(n) space
Mistake I made:
  - first idea was a tree (each number a child of a divisor); a tree allows one parent,
    but 6 needs both 2 and 3 -> each number keeps only its BEST parent (prev)
  - compared dp[i] % dp[j] (chain lengths) instead of nums[i] % nums[j] (the values)
  - walked back with `while prev[i] >= 0`, which drops the chain's first number
    ([2, 3] -> []); loop on the index itself: `while i >= 0`
  - reversed twice (res.reverse() and res[::-1]); one is enough
"""


class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)

        dp = [1] * n
        prev = [-1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

        max_len = max(dp)
        last = -1
        for i in range(n):
            if dp[i] == max_len:
                last = i
                break

        i = last
        res = []
        while i >= 0:
            res.append(nums[i])
            i = prev[i]

        res.reverse()
        return res
