"""
347. Top K Frequent Elements  (Medium)
https://leetcode.com/problems/top-k-frequent-elements/

Pattern:    count with a hashmap, then "top k" -> min-heap of size k (or bucket sort by count)
Key idea:
  - Counter(nums) gives value -> count
  - min-heap of (count, value) capped at size k: push, and pop when size > k
    -> the smallest count leaves, the k largest stay
  - bucket sort: a count is at most n, so bucket[c] = values seen c times;
    walk buckets from high count to low until k values are collected -> O(n)
  - one-liner: Counter(nums).most_common(k) (uses a heap inside)
Complexity: heap O(n log k) time, O(n) space; bucket O(n) time, O(n) space
Mistake I made: none (worked first try). Remember `import heapq` outside LeetCode.
"""

import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)

        hp = []
        for key, value in counter.items():
            heapq.heappush(hp, (value, key))
            if len(hp) > k:
                heapq.heappop(hp)

        return [key for _, key in hp]


class SolutionBucket:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counter.items():
            buckets[count].append(num)

        res = []
        for count in range(len(buckets) - 1, 0, -1):
            for num in buckets[count]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
