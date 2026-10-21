"""
3. Longest Substring Without Repeating Characters  (Medium)
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Pattern:    sliding window with a last-seen-index map
Key idea:
  - window = s[l..r], all characters distinct
  - seen[ch] = last index of ch; if ch was seen INSIDE the window (seen[ch] >= l),
    jump l to seen[ch] + 1 (never move l backward: an old index left of l is ignored)
  - update seen[ch] = r, answer = max window length r - l + 1
Complexity: O(n) time (r moves once, l only jumps forward), O(k) space, k = distinct characters
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        res = 0
        for r, ch in enumerate(s):
            if ch in seen and l <= seen[ch]:
                l = seen[ch] + 1
            seen[ch] = r
            res = max(r - l + 1, res)

        return res
