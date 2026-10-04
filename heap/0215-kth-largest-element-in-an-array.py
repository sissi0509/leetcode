"""
215. Kth Largest Element in an Array  (Medium)
https://leetcode.com/problems/kth-largest-element-in-an-array/

Pattern:    heap (top-k) or quickselect, clue: "kth largest" without needing full sort
Key idea:
  - heap: min-heap of the k largest seen so far; its top is the answer
  - heap: push every number, pop when size > k (one pop is always enough)
  - quickselect: random pivot, split into larger / equal / smaller lists
  - quickselect: k <= len(larger) -> recurse larger; within equal -> pivot;
    else recurse smaller with k - len(larger) - len(equal)
  - the "equal" list keeps duplicates from making it slow
Complexity:
  - heap: O(n log k) time, O(k) space
  - quickselect: O(n) average (n + n/2 + ... = 2n), O(n^2) worst, O(n) extra space
Mistake I made:
  - first heap rule compared with the top before checking size -> dropped
    items while the heap had fewer than k
"""

import heapq
import random


# Method 1: quickselect (three-way split), O(n) average time
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pivot = random.choice(nums)
        smaller, equal, larger = [], [], []

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        
        if k <= len(larger):
            return self.findKthLargest(larger, k)
        elif k <= len(larger) + len(equal):
            return pivot
        else:
            return self.findKthLargest(smaller, k - len(larger) - len(equal))

# Method 2: min-heap of size k, O(n log k) time
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        hp = []

        for num in nums:
            heapq.heappush(hp, num)
            if len(hp) > k: # while also works
                heapq.heappop(hp)
        
        return hp[0]