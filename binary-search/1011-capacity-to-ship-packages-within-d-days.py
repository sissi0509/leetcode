"""
1011. Capacity To Ship Packages Within D Days  (Medium)
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

Pattern:    Binary search on the answer, clue: "least capacity such that ... within days"
Key idea:
  - capacities: F F F T T T (too small fails, anything bigger also works) -> find the FIRST T
  - range: lo = max(heaviest package, ceil(total / days)) (a package can't be split),
    hi = total (everything in one day)
  - can_ship(cap): add packages in order; when one would overflow, start a new day with it;
    count the last, unfinished day too
  - first T: works -> hi = mid (keep it), fails -> lo = mid + 1; hi = mid keeps mid,
    so round DOWN
Complexity: O(n log S) time, S = sum(weights); O(1) space
Mistake I made:
  - moves flipped (lo = mid on success = searching for the LAST capacity that works -> sum)
  - lower bound min(weights) instead of max(weights); last day not counted
  - after flipping the moves, kept round-up mid -> infinite loop (hi = mid needs round down)
"""


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        total = sum(weights)
        min_cap = max((total + days - 1) // days, max(weights))
        max_cap = total

        lo, hi = min_cap, max_cap

        def can_ship(cap):
            day = 0
            cur = 0
            for w in weights:
                cur += w
                if cur > cap:
                    day += 1
                    cur = w
            if cur > 0:
                day += 1

            return day <= days

        while lo < hi:
            mid = (lo + hi) // 2
            if can_ship(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
