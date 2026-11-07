"""
22. Generate Parentheses  (Medium)
https://leetcode.com/problems/generate-parentheses/

Pattern:    backtracking with counts; clue = "generate ALL valid combinations"
Key idea:
  - track left = "(" used, right = ")" used
  - add "(" while left < n; add ")" only while right < left (never close more than opened)
  - right == n -> a full valid string
  - each append has exactly ONE pop, right after the recursive call
  - SolutionClean: check limits before adding, so no "went too far" base case
Complexity: O(4^n / sqrt(n)) results (Catalan number), each O(n) to build
Mistake I made (v1):
  - extra path.pop() inside the `left > n` base case -> caller popped again -> path lost a char
    (n = 1 returned ")")
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        path = []

        def dfs(left, right):
            if left > n:
                return

            if right == n:
                res.append("".join(path))
                return

            if left >= right:
                path.append("(")
                dfs(left + 1, right)
                path.pop()

            if left > right:
                path.append(")")
                dfs(left, right + 1)
                path.pop()

        dfs(0, 0)

        return res


class SolutionClean:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def dfs(s, left, right):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                dfs(s + "(", left + 1, right)
            if right < left:
                dfs(s + ")", left, right + 1)

        dfs("", 0, 0)
        return res
