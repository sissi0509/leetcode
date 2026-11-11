"""
17. Letter Combinations of a Phone Number  (Medium)
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Pattern:    backtracking; clue = "return ALL combinations", one choice per position
Key idea:
  - dfs(i) = pick one letter for digit i, then recurse on i + 1
  - base case: path has one letter per digit -> save "".join(path)
  - one append <-> one pop around each recursive call
Complexity: O(4^n * n) time (up to 4 letters per digit, join costs n), O(n) recursion depth
Mistake I made:
  - none; passed on the first run
  - edge case to ask: empty digits -> [] (this version returns [""])
  - `map` shadows Python's built-in map(); a name like `phone` is safer
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        letters = []
        for digit in digits:
            letters.append(map[digit])
        res = []
        path = []

        def dfs(i):
            if len(path) == len(digits):
                res.append("".join(path))
                return

            for ch in letters[i]:
                path.append(ch)
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res
