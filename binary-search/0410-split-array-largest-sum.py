"""
410. Split Array Largest Sum  (Hard)
https://leetcode.com/problems/split-array-largest-sum/

Pattern:    Binary search on the answer, clue: "minimize the largest sum" (min of a max)
Key idea:
  - same shape as LC1011: guess the largest allowed subarray sum, greedily cut left to right
  - can_split(total): start a new subarray when the next number would go over total;
    F F F T T T (a bigger limit never needs more pieces) -> first T: hi = mid, round down
  - range: lo = max(max(nums), ceil(sum / k)), hi = sum (one piece)
  - "at most k pieces" is enough: a valid split with fewer pieces can always be cut more
Complexity: O(n log S) time, S = sum(nums); O(1) space
Mistake I made:
  - lower bound sum // k + 1 is not the ceiling: one too big when k divides the sum
    ([1,1], k=2 -> 2 instead of 1). A lower bound must never be above the answer;
    use (sum + k - 1) // k, or just max(nums)
"""


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        hi = sum(nums)
        lo = max((hi + k - 1) // k, max(nums))

        def can_split(total):
            cnt = 1
            cur = 0
            for num in nums:
                if cur + num > total:
                    cnt += 1
                    cur = 0
                    if cnt > k:
                        return False
                cur += num
            return cnt <= k

        while lo < hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
