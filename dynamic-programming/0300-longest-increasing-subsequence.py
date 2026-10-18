"""
300. Longest Increasing Subsequence  (Medium)
https://leetcode.com/problems/longest-increasing-subsequence/

Pattern:    1-D DP (O(n^2)), then "smallest tail per length" + binary search (O(n log n))
            clue: "subsequence" = can skip elements, keep order -> NOT two pointers / sliding window
Key idea:
  - DP: dp[i] = length of the LIS ending at i
      dp[i] = 1 + max(dp[j] for j < i if nums[j] < nums[i]), base 1, answer max(dp)
  - faster: ends[k] = smallest possible last number of an increasing subsequence of length k
      ends is always sorted, so each new number either
        - is bigger than every tail -> extends the longest one (append), or
        - replaces the first tail >= it (binary search: first T where T = ends[i] >= num)
      a smaller tail is never worse: it leaves more room for later numbers
  - ends holds lengths, not a real subsequence; only len(ends) is the answer
Complexity: DP O(n^2) time, O(n) space; tails O(n log n) time, O(n) space
Mistake I made:
  - first plan was two pointers resetting on a break -> that's the longest increasing SUBARRAY
    ([0, 3, 1, 2] -> 2, real answer 3: [0, 1, 2])
"""


class Solution:
    # O(n^2) DP
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            max_prev = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_prev = max(max_prev, dp[j])
            dp[i] = max_prev + 1

        return max(dp)


class SolutionTails:
    # O(n log n): smallest tail per length + binary search
    # -inf sentinel: ends[k] = smallest tail of a length-k subsequence
    def lengthOfLIS(self, nums: list[int]) -> int:
        ends = [float('-inf')]
        for num in nums:
            if num > ends[-1]:
                ends.append(num)
            else:
                # first index with ends[i] >= num; it always exists here, so r = len - 1 is safe
                l, r = 0, len(ends) - 1
                while l < r:
                    mid = (l + r) // 2
                    if ends[mid] < num:
                        l = mid + 1
                    else:
                        r = mid
                ends[l] = num

        return len(ends) - 1
