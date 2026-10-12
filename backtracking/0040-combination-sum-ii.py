"""
40. Combination Sum II  (Medium)
https://leetcode.com/problems/combination-sum-ii/

Pattern:    backtracking + skip duplicates, clue: input has duplicates, each number used once,
            "no duplicate combinations"
Key idea:
  - the for loop = the choices at ONE level of the tree (which value goes in this slot)
  - at the same level, skip a value already tried: i > start and candidates[i] == candidates[i - 1]
      * i > start, not i > 0: the first try at a level (i == start) is never a duplicate,
        so the same value can still be picked again one level deeper ([1, 1, 6])
  - the child gets dfs(i + 1, ...): this number is used, it can't be picked twice
    ("use once" lives in the child's start, not in the loop's range)
  - continue for a duplicate (only this value is bad), break when too big (sorted: all later are too)
  - differs from LC39 in one place: LC39 passes i (reuse), LC40 passes i + 1
Complexity: O(2^n) time roughly (each number in or out), O(n) recursion depth, not counting the output
Mistake I made:
  - loop started at start + 1 with dfs(0, 0), so candidates[0] was never used
  - no same-level duplicate skip (hidden by the first bug)
  - solved with help: needed the code for the skip condition
"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []
        path = []
        n = len(candidates)

        def dfs(start, total):
            if total == target:
                res.append(path[:])
                return
            for i in range(start, n):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(i + 1, total + candidates[i])
                path.pop()

        dfs(0, 0)
        return res
