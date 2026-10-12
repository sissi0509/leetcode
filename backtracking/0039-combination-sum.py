"""
39. Combination Sum  (Medium)
https://leetcode.com/problems/combination-sum/

Pattern:    backtracking, clue: "return ALL combinations" + a number may be reused
Key idea:
  - one dfs call = one NODE of the decision tree: "sum so far, choose from start on"
    -> the empty root is just dfs(0, 0), no extra loop outside
  - loop i from start (not start + 1): reuse allowed, never go back -> no duplicates
  - append -> recurse -> pop, all inside the loop
  - sorted + every candidate >= 2: once one candidate is too big, all later ones are
    too -> break in the PARENT's loop (a child can't stop its siblings)
  - with negatives the answer is infinite unless the length is bounded (LC377 follow-up)
  - DP (sum x candidate table) would COUNT combinations (LC518); listing them is exponential
Complexity: O(n^(T/m)) time roughly (T = target, m = smallest candidate),
            O(T/m) recursion depth, not counting the output
Mistake I made:
  - v1 recursed with i + 1 and no loop: one chain, no branching, no reuse
  - v2 had dfs mean "add candidates[i]", so the root forced candidates[0] first
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        path = []
        n = len(candidates)

        def dfs(start, pre_total):
            if pre_total == target:
                res.append(path[:])
                return

            for i in range(start, n):
                if pre_total + candidates[i] > target:
                    break
                path.append(candidates[i])
                dfs(i, pre_total + candidates[i])
                path.pop()

        dfs(0, 0)
        return res
