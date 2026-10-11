"""
380. Insert Delete GetRandom O(1)  (Medium)
https://leetcode.com/problems/insert-delete-getrandom-o1/

Pattern:    Design: hashmap + list, clue: O(1) insert/remove AND O(1) random pick
Key idea:
  - dict alone: O(1) insert/remove, but no O(1) random pick
  - list alone: O(1) random pick (random.choice), but remove from the middle is O(n)
  - keep both. Invariant: self.dict[val] is always val's index in self.lst
  - remove: list.pop() is O(1) only at the end, so move the last element into val's slot,
    update the moved element's index, then pop
  - edge case: val is already the last element -> no swap, just pop
    (delete val from the dict BEFORE writing the moved index, so it can't come back)
Complexity: O(1) average for every method, O(n) space
Mistake I made:
  - 2026-08-18: insert returned the opposite True/False; remove broke when val was the last element
  - 2026-10-10: swap condition `idx == len(self.lst)` never fires (last index is len - 1,
    and the swap should run when val is NOT last); `Random.choice` instead of `random.choice`
"""

import random


class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.lst.append(val)
            self.dict[val] = len(self.lst) - 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False

        idx = self.dict[val]
        del self.dict[val]

        if idx != len(self.lst) - 1:
            self.lst[-1], self.lst[idx] = self.lst[idx], self.lst[-1]
            self.dict[self.lst[idx]] = idx

        self.lst.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)
