"""
1482. Minimum Number of Days to Make m Bouquets  (Medium)
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

Pattern:    binary search on the answer (days), clue: "minimum day such that ..." + an O(n) check
Key idea:
  - impossible iff m * k > n (not enough flowers at all) -> -1 up front
  - can_make(day): one pass, count runs of adjacent bloomed flowers; every k in a row = 1 bouquet
  - monotone: a flower bloomed by day d is still bloomed on day d + 1 -> F F F T T T over days
  - search days in [min(bloomDay), max(bloomDay)] for the first T (l < r, r = mid / l = mid + 1);
    after the m * k check the answer always exists, so no check after the loop is needed
Complexity: O(n log D) time, D = max - min day; O(1) extra space with the one-pass check
Note: v1 built a 0/1 flowers array on every check (extra O(n) memory) and re-checked l after
      the loop; both work, SolutionLean drops them and stops early once m bouquets are made
"""


class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def can_make(day):
            flowers = [0] * len(bloomDay)
            for i, days in enumerate(bloomDay):
                if days <= day:
                    flowers[i] = 1

            group = 0
            cur = 0
            for cnt in flowers:
                cur += cnt
                if cur == k:
                    cur = 0
                    group += 1

                if cnt == 0:
                    cur = 0

            return group >= m

        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if can_make(mid):
                r = mid
            else:
                l = mid + 1

        if can_make(l):
            return l
        else:
            return -1


class SolutionLean:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def can_make(day):
            bouquets = run = 0
            for d in bloomDay:
                if d <= day:
                    run += 1
                    if run == k:
                        bouquets += 1
                        if bouquets == m:
                            return True
                        run = 0
                else:
                    run = 0
            return False

        l, r = min(bloomDay), max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if can_make(mid):
                r = mid
            else:
                l = mid + 1
        return l
