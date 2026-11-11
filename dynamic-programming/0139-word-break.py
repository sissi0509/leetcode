"""
139. Word Break  (Medium)
https://leetcode.com/problems/word-break/

Pattern:    1-D DP over prefixes; clue = "can the string be split into dictionary words"
Key idea:
  - dp[r] = True if s[:r] can be split into words
  - dp[0] = True (the empty prefix)
  - dp[r] = True if some l has dp[l] True and s[l:r] in the word set
  - answer = dp[len(s)]
Complexity: O(n^3) time (n^2 pairs, slicing costs n), O(n) space
  - SolutionMaxLen: only try l >= r - max_len -> O(n * max_len^2)
Mistake I made:
  - none; passed on the first run
  - `continue` at the end of the loop does nothing; `break` stops once dp[r] is True
  - leftover `l = 0` line; range(r + 1) also checks the empty slice s[r:r]
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        word_set = set(wordDict)
        l = 0
        for r in range(len(s) + 1):
            for l in range(r + 1):
                if dp[l] and s[l:r] in word_set:
                    dp[r] = True
                    continue
        return dp[-1]


class SolutionMaxLen:
    # only try words that fit: l from r - 1 down to r - max_len
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        word_set = set(wordDict)
        max_len = max(len(word) for word in word_set)
        for r in range(len(s) + 1):
            for l in range(r - 1, max(-1, r - max_len - 1), -1):
                if dp[l] and s[l:r] in word_set:
                    dp[r] = True
                    break
        return dp[-1]
