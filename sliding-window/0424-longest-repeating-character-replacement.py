"""
424. Longest Repeating Character Replacement  (Medium)
https://leetcode.com/problems/longest-repeating-character-replacement/

Pattern:    sliding window + letter counts; clue = "longest substring" + "at most k changes"
Key idea:
  - replacements needed = window length - count of the most common letter
  - window valid while max_freq + k >= window length; otherwise shrink from the left
  - Solution (simple): max(freq) over 26 letters each step -> O(26n) = O(n)
  - SolutionMaxFreq: max_freq only goes UP, never down when shrinking;
    a stale (too high) max_freq can't give a wrong answer, because the answer
    only grows when max_freq grows -> the while shrinks at most once
  - answer = min(max_freq + k, n): a letter seen max_freq times in one window
    can be widened with neighbors to max_freq + k and still need <= k changes
Complexity: O(n) time, O(1) space (26 letters)
Mistake I made:
  - none; both versions passed on the first run
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = 0
        res = 0
        for r in range(len(s)):
            freq[ord(s[r]) - ord('A')] += 1
            max_freq = max(freq)
            while max_freq + k < r - l + 1:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


class SolutionMaxFreq:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        freq = defaultdict(int)
        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            max_freq = max(freq[s[r]], max_freq)
            while max_freq + k < r - l + 1:
                freq[s[l]] -= 1
                l += 1
        return min(max_freq + k, len(s))
