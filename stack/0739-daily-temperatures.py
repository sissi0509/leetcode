"""
739. Daily Temperatures  (Medium)
https://leetcode.com/problems/daily-temperatures/

Pattern:    monotonic stack, "next greater element" (the simplest form)
Key idea:
  - the stack holds indices of days still WAITING for a warmer day; their temperatures
    go down from bottom to top (a decreasing stack)
  - a new day j that is warmer than the top answers the top: pop it, res[i] = j - i,
    and keep popping while it's still warmer
  - then push j (it waits too)
  - days left in the stack never got an answer -> 0
Complexity: O(n) time (each index pushed once, popped at most once), O(n) space
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []                                   # indices waiting for a warmer day

        for j, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                i = stack.pop()
                res[i] = j - i
            stack.append(j)

        return res
