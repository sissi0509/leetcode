"""
41. First Missing Positive  (Hard)
https://leetcode.com/problems/first-missing-positive/

Pattern:    "is 1 present? 2? 3?" = hash-set lookups; O(1) space -> use the array itself as the set
Key idea:
  - with n numbers the answer is always in 1..n+1 (best case the array is exactly 1..n -> n+1),
    so only values 1..n matter, and the array has exactly n slots: value v's home is index v - 1
  - cyclic placement: while nums[i] is in 1..n and its home doesn't already hold it, swap it home
    (the swapped-in value gets checked next, so stay on i)
  - then scan: the first index i with nums[i] != i + 1 -> answer i + 1; all homes filled -> n + 1
  - the guard `nums[nums[i] - 1] != nums[i]` (not `nums[i] != i + 1`) stops duplicates from
    swapping forever ([1, 1])
Complexity: O(n) time (each swap puts one value home for good, so at most n swaps), O(1) extra space
Simple version first: put everything in a set, check 1, 2, 3, ... -> O(n) time, O(n) space
Mistake I made:
  - didn't see the "array as its own hash set" trick -> solution shown (learn mode), retype owed
"""


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                home = nums[i] - 1
                nums[i], nums[home] = nums[home], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


class SolutionSet:
    def firstMissingPositive(self, nums: list[int]) -> int:
        seen = set(nums)
        x = 1
        while x in seen:
            x += 1
        return x
