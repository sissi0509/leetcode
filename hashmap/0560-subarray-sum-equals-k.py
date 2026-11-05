"""
560. Subarray Sum Equals K  (Medium)
https://leetcode.com/problems/subarray-sum-equals-k/

Pattern:    prefix sum + hashmap of counts; clue = "count contiguous subarrays with sum k"
            and values can be negative (so a sliding window doesn't work)
Key idea:
  - sum(i..j) = prefix[j] - prefix[i-1] -> a subarray ending here sums to k
    exactly when some EARLIER prefix equals (current prefix - k)
  - map: prefix sum -> how many times seen so far; starts with {0: 1}
    (the empty prefix, for subarrays that start at index 0)
  - record the previous prefix BEFORE adding num -> the current element is never
    paired with itself (k = 0 doesn't count empty subarrays)
Complexity: O(n) time, O(n) space
Mistake I made:
  - none in the code; coded it straight from memory but couldn't explain it in words at first
"""

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        pre_sum = defaultdict(int)

        total = 0
        res = 0
        for num in nums:
            pre_sum[total] += 1
            total += num
            res += pre_sum[total - k]

        return res
