"""
84. Largest Rectangle in Histogram  (Hard)
https://leetcode.com/problems/largest-rectangle-in-histogram/

Pattern:    monotonic stack, "nearest smaller on both sides" (LC739 with smaller instead of greater)
Key idea:
  - flip the question: if bar i is the SHORTEST bar of a rectangle, how wide can it be?
    it spreads until the first shorter bar on each side -> width = right - left - 1
  - increasing stack of indices: bars waiting for their first shorter bar on the right
  - a new bar j shorter than the top -> j is the top bar's RIGHT boundary; the bar now under it
    in the stack is its LEFT boundary (everything between was taller and already popped)
  - append a 0-height sentinel so every bar gets popped at the end; empty stack -> left = -1
Complexity: O(n) time (each index pushed and popped once), O(n) space
Mistake I made:
  - didn't see why a stack fits; learned it via LC739 first (solution shown, retype owed)
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []                                   # indices, heights increasing
        best = 0

        for j, h in enumerate(heights + [0]):        # 0 = sentinel, flushes the stack
            while stack and heights[stack[-1]] > h:
                i = stack.pop()                      # bar i's right boundary is j
                left = stack[-1] if stack else -1    # its left boundary
                best = max(best, heights[i] * (j - left - 1))
            stack.append(j)

        return best
