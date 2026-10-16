"""
33. Search in Rotated Sorted Array  (Medium)
https://leetcode.com/problems/search-in-rotated-sorted-array/

Pattern:    Binary search, exact match (closed [l, r], l <= r, drop mid), clue: "rotated", "O(log n)"
Key idea:
  - at any mid, one half is always sorted
  - nums[l] <= nums[mid] -> the left half is sorted, else the right half is
  - if the target is inside the sorted half's range, search there, otherwise the other half
  - <= (not <) in nums[l] <= nums[mid]: when l == mid the "left half" is just one element
Complexity: O(log n) time, O(1) space
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
