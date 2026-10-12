"""
556. Next Greater Element III  (Medium)
https://leetcode.com/problems/next-greater-element-iii/

Pattern:    Next permutation, clue: "smallest number > n with exactly the same digits"
Key idea:
  - change digits as far right as possible (changing a left digit makes a big jump)
  - pivot: scan from the right for the first digit smaller than the one after it
    (no pivot -> digits never go up, already the largest arrangement -> -1)
  - everything after the pivot is decreasing (that's why the scan didn't stop there)
  - swap the pivot with the smallest digit bigger than it on its right
    = the rightmost digit bigger than it, because that part is decreasing
  - after the swap that part is still decreasing -> reverse it (not sort) to make it the smallest
  - check the 32-bit limit at the end
  - the swap target can be found with binary search (last index > pivot), but the reverse is
    O(d) anyway, so a plain right-to-left scan is just as fast and simpler
Complexity: O(d) time, O(d) space (d = number of digits, at most 10)
Mistake I made:
  - first tried brute force (scan up / all permutations): correct but 10! perms is ~1 s per input
  - built the digits with % 10 (reversed order) but scanned as if they were in normal order;
    list(str(n)) keeps the indices matching the number
  - loop guard `i == 0 or ...` instead of `i >= 0 and ...` -> ran into negative indices
  - thought the part after the pivot was increasing and tried to bubble one digit; it's decreasing,
    so the whole part has to be reversed
  - binary search with `lo = mid` must round mid UP, or it loops forever when hi = lo + 1
  - with duplicates the swap target must be the RIGHTMOST bigger digit (1331 -> 3113, not 3131)
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i == -1:
            return -1

        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if nums[mid] > nums[i]:
                lo = mid
            else:
                hi = mid - 1

        j = lo

        nums[j], nums[i] = nums[i], nums[j]

        nums[i + 1:] = nums[i + 1:][::-1]

        res = int("".join(nums))
        return res if res < 2 ** 31 else -1
