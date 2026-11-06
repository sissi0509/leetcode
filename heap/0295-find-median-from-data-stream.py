"""
295. Find Median from Data Stream  (Hard)
https://leetcode.com/problems/find-median-from-data-stream/

Pattern:    two heaps; clue = "median" of a stream that keeps growing
Key idea:
  - smaller = max heap (store -num) for the lower half, larger = min heap for the upper half
  - route: num <= top of smaller -> smaller, else larger
  - balance rule: smaller holds the same count or ONE extra, never more -> fix both directions
  - median = top of smaller (odd count) or average of both tops (even count)
Complexity: addNum O(log n), findMedian O(1), O(n) space
Mistake I made (v1):
  - balanced only one way (larger -> smaller), so smaller could grow 2+ bigger:
    add 1, 2, 0, -1 -> returned 1 instead of 0.5
"""

import heapq


class MedianFinder:

    def __init__(self):
        self.smaller = []  # max heap
        self.larger = []   # min heap

    def addNum(self, num: int) -> None:
        if not self.smaller or num <= -self.smaller[0]:
            heapq.heappush(self.smaller, -num)
        else:
            heapq.heappush(self.larger, num)

        if len(self.larger) > len(self.smaller):
            heapq.heappush(self.smaller, -(heapq.heappop(self.larger)))

        if len(self.larger) + 1 < len(self.smaller):
            heapq.heappush(self.larger, -(heapq.heappop(self.smaller)))

    def findMedian(self) -> float:
        if len(self.smaller) == len(self.larger):
            return (self.larger[0] - self.smaller[0]) / 2.0

        return -self.smaller[0]
