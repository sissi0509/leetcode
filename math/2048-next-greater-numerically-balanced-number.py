"""
2048. Next Greater Numerically Balanced Number  (Medium)
https://leetcode.com/problems/next-greater-numerically-balanced-number/

Pattern:    Brute force with a bounded search, clue: n <= 10^6 is small on purpose
Key idea:
  - balanced = every digit d appears exactly d times (so 0 can never appear)
  - check one number: Counter(str(x)), then every int(digit) == its count
  - count up from n + 1 until a number is balanced
  - why it's fast enough: 1666666 is balanced and > 10^6, so the loop always stops by then
    (tightest bound: 1224444), about 1.2M numbers x 7 digits ~ 10^7 steps
  - if n were huge: generate instead of scan. Pick digit sets that add up to <= 7
    (itertools.combinations), write each digit d d times, try every order
    (itertools.permutations), return the smallest candidate > n
Complexity: O(B * d) time, B ~ 1.2M candidates, d <= 7 digits; O(d) space
Mistake I made:
  - forgot str(): Counter(1333) -> TypeError, an int isn't iterable; Counter(str(1333)) works
  - after str() the keys are strings ('3'), so compare int(d) == c, not d == c
"""

from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x):
            count = Counter(str(x))
            return all(int(d) == c for d, c in count.items())

        x = n + 1
        while not is_balanced(x):
            x += 1
        return x
