"""
5. Longest Palindromic Substring  (Medium)
https://leetcode.com/problems/longest-palindromic-substring/

Pattern:    expand around center (2n - 1 centers: each char for odd lengths, each gap for even)
Key idea:
  - expand(l, r): while in bounds and s[l] == s[r], move outward
    the loop stops one step too far on BOTH sides -> palindrome = s[l + 1:r], length r - l - 1
  - try (i, i) and (i, i + 1) for every i, keep the longest
  - the loop skips the odd center at the last index; the initial answer s[-1] covers it
    (a palindrome centered on the last char has length 1)
Complexity: O(n^2) time; O(1) extra space if expand returns indices and you slice once at the end
            (slicing inside expand builds an O(n) string per call)
Alternative: 2-D DP (SolutionDP), dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])
  - fill order: dp[i][j] needs dp[i + 1][j - 1] (the row below), so i goes from n - 1 DOWN to 0
  - O(n^2) time AND space
Mistake I made (DP):
  - top-down memo with a dict of (l, r) tuples -> Memory Limit Exceeded at n = 1000
    (~500k tuple keys); a 2-D list of bools is much lighter and needs no recursion
  - called find_palindrome(l, n) instead of (l, r); updated max_string but never max_len
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def max_palindrom(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1, s[l + 1:r]

        max_len = 1
        max_string = s[-1]

        for i in range(n - 1):
            len1, s1 = max_palindrom(i, i)
            len2, s2 = max_palindrom(i, i + 1)

            if len1 > max_len:
                max_len = len1
                max_string = s1

            if len2 > max_len:
                max_len = len2
                max_string = s2

        return max_string


class SolutionDP:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        best_l, best_r = 0, 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i > best_r - best_l:
                        best_l, best_r = i, j

        return s[best_l:best_r + 1]
