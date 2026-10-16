"""
162. Find Peak Element  (Medium)
https://leetcode.com/problems/find-peak-element/

Pattern:    Binary search on an unsorted array, clue: "any peak", "O(log n)", neighbors never equal
Key idea:
  - compare mid with its neighbor: if the slope goes up (nums[mid] < nums[mid + 1]),
    a peak must exist on the right (it can't keep rising forever, nums[n] = -inf)
  - so each step keeps a half that is guaranteed to contain a peak
  - my version: closed [l, r], -inf for missing neighbors, return mid when it's a peak
  - standard version: converge (l < r), compare only nums[mid] and nums[mid + 1],
    rising -> l = mid + 1, falling -> r = mid (mid might be the peak); hi = len - 1 because
    a peak is always a real index, and mid + 1 is always in range since mid < r
Complexity: O(log n) time, O(1) space
"""


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            left = nums[mid - 1] if mid - 1 >= 0 else float('-inf')
            right = nums[mid + 1] if mid + 1 < len(nums) else float('-inf')

            if left < nums[mid] and nums[mid] > right:
                return mid

            if left < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return -1


class SolutionConverge:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l
