"""
904. Fruit Into Baskets  (Medium)
https://leetcode.com/problems/fruit-into-baskets/

Pattern:    sliding window + dict; clue = "longest contiguous run" + "at most 2 types"
Key idea:
  - same as "longest subarray with at most 2 distinct values"
  - dict maps fruit type -> its LAST index in the window
  - more than 2 types -> move l right; when l is a type's last index, that type
    leaves the window -> pop it from the dict
  - answer = max window length r - l + 1
Complexity: O(n) time (each index enters and leaves once), O(1) space (dict holds <= 3 keys)
Mistake I made:
  - none; passed on the first run (forgot how to delete from a set/dict: d.pop(k) / del d[k])
"""


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        l = 0
        visited = {}
        res = 0
        for r, fruit in enumerate(fruits):
            visited[fruit] = r
            while len(visited) > 2:
                if l == visited[fruits[l]]:
                    visited.pop(fruits[l])
                l += 1

            res = max(res, r - l + 1)

        return res
