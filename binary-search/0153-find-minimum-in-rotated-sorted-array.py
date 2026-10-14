"""
153. Find Minimum in Rotated Sorted Array  (Medium)
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Pattern:    Binary search, converge form (l < r), clue: "rotated sorted", "O(log n)"
Key idea:
  - compare nums[mid] with nums[r], the right end of the current range
  - nums[mid] < nums[r]: mid is in the right (smaller) part, the min is at mid or left of it -> r = mid
  - otherwise mid is in the left (bigger) part, the min is right of it -> l = mid + 1
  - nums[mid] can never equal nums[r]: mid < r inside the loop and the values are distinct
  - also works when the array isn't rotated at all
Complexity: O(log n) time, O(1) space
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]
