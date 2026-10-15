"""
981. Time Based Key-Value Store  (Medium)
https://leetcode.com/problems/time-based-key-value-store/

Pattern:    Dict of sorted lists + binary search, clue: "largest timestamp <= t" and
            "timestamps of set are strictly increasing"
Key idea:
  - dict: key -> list of (timestamp, value)
  - set: timestamps only increase, so append keeps the list sorted, O(1)
    (a heap is O(log n) insert but can't find "largest <= t" quickly; a sorted list with
    middle inserts is O(n); with timestamps in any order -> balanced BST / SortedList)
  - get: last index with time <= t = (first index with time > t) - 1
  - first index with time > t can be "past the end", so hi = len(lst)
  - l == 0 means nothing is <= t -> ""
Complexity: set O(1), get O(log n); O(total sets) space
Mistake I made:
  - "last true" search with no check after the loop: returned lst[0] when every time was > t
  - fell off the end of get (returned None) on a missing key
  - returned the timestamp [0] instead of the value [1]; started hi at len - 1
"""

from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.dict[key]
        l, r = 0, len(lst)
        while l < r:
            mid = (l + r) // 2
            if lst[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid

        if l == 0:
            return ""
        return lst[l - 1][1]
