"""
658. Find K Closest Elements  (Medium)
https://leetcode.com/problems/find-k-closest-elements/

Pattern:    binary search (lower bound) + two pointers expanding outward
Key idea:
  - lower bound: first index with arr[i] >= x -> l = that - 1, r = that
  - take the closer side k times; tie -> the smaller value (left side)
  - deque: appendleft for the left side, append for the right side -> stays sorted
  - when one side runs out, keep taking from the other (and count k down!)
  - the answer is always the contiguous block arr[l+1:r] -> could return that slice
  - SolutionShrink: start with the whole array, drop the farther end until k are left, O(n - k)
Complexity: O(log n + k) time, O(k) space for the deque
Mistake I made (v1):
  - upper middle (l + r + 1) // 2 with r = mid -> infinite loop / IndexError at mid = len(arr)
    (rule: r = mid needs the LOWER middle)
  - the two leftover loops never did k -= 1 -> took every remaining element
"""

from collections import deque


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l, r = 0, len(arr)
        while l < r:
            mid = (l + r) // 2
            if arr[mid] >= x:
                r = mid
            else:
                l = mid + 1

        l, r = l - 1, l
        res = deque()

        while l >= 0 and r < len(arr) and k > 0:
            if abs(arr[l] - x) < abs(arr[r] - x) or (abs(arr[l] - x) == abs(arr[r] - x) and arr[l] < arr[r]):
                res.appendleft(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            k -= 1

        while l >= 0 and k > 0:
            res.appendleft(arr[l])
            l -= 1
            k -= 1

        while r < len(arr) and k > 0:
            res.append(arr[r])
            r += 1
            k -= 1

        return list(res)


class SolutionShrink:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l, r = 0, len(arr) - 1
        while r - l + 1 > k:
            if x - arr[l] <= arr[r] - x:   # left is closer or tied -> drop right
                r -= 1
            else:
                l += 1
        return arr[l:r + 1]
