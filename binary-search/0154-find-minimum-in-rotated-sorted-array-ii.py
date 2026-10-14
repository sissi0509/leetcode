"""
154. Find Minimum in Rotated Sorted Array II  (Hard)
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Pattern:    Binary search, converge form (l < r), clue: LC153 + "may contain duplicates"
Key idea:
  - same as LC153, plus a tie case: nums[mid] == nums[r]
  - on a tie you can't tell which side the min is on:
    [1, 1, 1, 0, 1, 1] (min right of mid) vs [1, 0, 1, 1, 1, 1] (min left of mid)
  - so drop one element: r -= 1. Safe because mid and r are different positions
    with the same value, so that value is still in [l, r] at mid
Complexity: O(log n) time on average, O(n) worst case (e.g. all equal except one), O(1) space
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r -= 1      # nums[r] has a copy at mid, so dropping r loses nothing

        return nums[l]
