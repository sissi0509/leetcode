"""
10. Regular Expression Matching  (Hard)
https://leetcode.com/problems/regular-expression-matching/

Pattern:    2-D DP over (pattern prefix, string prefix)
Key idea:
  - `.` = any one char; `x*` = ZERO OR MORE copies of x (the star belongs to the char before it,
    so read the pattern as units: c*a*b -> [c*][a*][b])
  - dp[r][c] = does p[:r] match s[:c]; dp[0][0] = True
  - empty string column: only `x*` units can vanish -> dp[r][0] = dp[r-2][0] when p[r-1] == '*'
  - plain char or `.`: dp[r][c] = matches(p[r-1], s[c-1]) and dp[r-1][c-1]
  - `*` (unit = p[r-2] + '*'), two choices:
      zero copies  -> skip the unit:             dp[r-2][c]
      one more copy -> p[r-2] matches s[c-1] and dp[r][c-1]  (unit stays available)
Edge case: a leading '*' (p = "*") would make dp[r - 2] = dp[-1], which Python silently wraps
  to the LAST row (no crash, just a wrong read). LeetCode guarantees every '*' has a valid char
  before it, so r >= 2 always holds; say that constraint out loud, or guard with r >= 2.
Complexity: O(m * n) time and space (m = len(s), n = len(p)); can roll to two rows
Mistake I made:
  - first read `*` as the wildcard meaning (any sequence, LC44); in LC10 it repeats the
    preceding char, and "zero copies" removes both chars of the unit
  - first draft checked dp[r-1][c] inside the loop over i (never used i) and set dp[r][0] = True
    for any `*`
  - working v2 had extra branches (r == 1, c == 1) -> collapsed into the two-term `*` rule
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        def matches(pc, sc):
            return pc == '.' or pc == sc

        for r in range(1, n + 1):
            if p[r - 1] == '*':
                dp[r][0] = dp[r - 2][0]
            for c in range(1, m + 1):
                if p[r - 1] == '*':
                    dp[r][c] = dp[r - 2][c] or (matches(p[r - 2], s[c - 1]) and dp[r][c - 1])
                else:
                    dp[r][c] = matches(p[r - 1], s[c - 1]) and dp[r - 1][c - 1]

        return dp[n][m]
