"""
155. Min Stack  (Medium)
https://leetcode.com/problems/min-stack/

Pattern:    stack + auxiliary min stack, clue: "getMin in O(1) time"
Key idea:
  - push / pop / top: a normal stack on a list
  - a second stack records the minimum so far
  - push: if value <= current min, push it onto the min stack too
  - <= not <: duplicates of the min must each be recorded (push 2, 2; pop once)
  - pop: if the popped value == min top, pop the min stack too
  - +inf sentinel in the min stack, so push needs no empty check
Invariant:
  - min_stack[-1] is always the minimum of everything in the main stack
  - so a popped value can never be smaller than min_stack[-1]:
    == means it was the min (pop it), > means the min is still below (do nothing)
Complexity: O(1) time for every operation, O(n) space
Mistake I made:
  - forgot the empty check before popping at first
"""


class MinStack:

    def __init__(self):
        self.list = []
        self.min_stack = [float('+inf')]

    def push(self, value: int) -> None:
        self.list.append(value)
        if value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        if not self.list:
            return

        value = self.list.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if not self.list:
            return None

        return self.list[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
