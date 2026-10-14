"""
875. Koko Eating Bananas  (Medium)
https://leetcode.com/problems/koko-eating-bananas/

Pattern:    Binary search on the answer, clue: "minimum speed such that ... within h hours"
Key idea:
  - search over speeds 1..max(piles), not over the piles
    (at speed max(piles) every pile takes 1 hour -> len(piles) <= h hours, always enough)
  - hours(k) = sum of ceil(p / k); a faster speed never needs more hours,
    so "hours(k) <= h?" looks like F F F T T T -> find the first T
  - same template as "first index >= x": too slow -> l = mid + 1, fast enough -> r = mid (keep it)
  - ceiling division with integers: (p + k - 1) // k
Complexity: O(n log M) time, M = max(piles); O(1) space
Mistake I made:
  - first thought of sorting the piles and searching them; it got easy once
    I searched the range of possible speeds instead
"""


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        largest = max(piles)
        if len(piles) == h:
            return largest

        l, r = 1, largest

        while l < r:
            mid = (l + r) // 2

            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid
            if hours > h:
                l = mid + 1
            else:
                r = mid

        return l
