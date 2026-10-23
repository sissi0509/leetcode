"""
91. Decode Ways  (Medium)
https://leetcode.com/problems/decode-ways/

Pattern:    1-D DP (Climbing Stairs with conditions), rolled into two variables
Key idea:
  - dp[i] = number of ways to decode the first i characters; dp[0] = 1 (empty prefix)
  - one-digit step: s[i] != '0'                -> + dp[i]      (pre1)
  - two-digit step: s[i-1:i+1] is 10..26       -> + dp[i - 1]  (pre2)
    (a leading '0' like "06" is NOT a valid two-digit code)
  - roll: pre2, pre1 = pre1, cur
Complexity: O(n) time, O(1) space
Mistake I made:
  - first version only checked 1 <= two-digit value <= 26, so "06" counted as a code;
    fixed with s[i-1] != '0' (equivalently: 10 <= value <= 26)
  - the early `s[0] == '0'` return is safe but not needed: the DP gives 0 by itself
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        pre2, pre1 = 1, 1

        for i in range(len(s)):
            cur = 0
            if s[i] != '0':
                cur += pre1
            if i > 0 and 1 <= int(s[i - 1:i + 1]) <= 26 and s[i - 1] != '0':
                cur += pre2

            pre2, pre1 = pre1, cur

        return pre1
