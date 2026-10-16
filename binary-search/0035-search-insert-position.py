"""
35. Search Insert Position  (Easy)
https://leetcode.com/problems/search-insert-position/

Pattern:    Binary search, "first index where ___ is true", clue: "index where it would be inserted"
Key idea:
  - the answer is the first index with nums[i] >= target (= bisect_left):
    found -> the target's index, not found -> where it would go
  - can be past the end (target bigger than everything) -> hi = len(nums)
  - which condition? >= lands ON the left edge of the target, > lands just PAST its right edge.
    Pick the one whose index IS the answer: first position / insert -> >=,
    last position / latest <= t (LC34 end, LC981) -> > and then step back one
Complexity: O(log n) time, O(1) space
Mistake I made:
  - none, but my first version searched "first > target" and then checked the index before it;
    ">=" gives the answer directly
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l


class SolutionFirstGreater:
    # my first version: first index with nums[i] > target, then check the one before it
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid

        if l > 0 and nums[l - 1] == target:
            return l - 1
        return l
