"""
290. Word Pattern  (Easy)
https://leetcode.com/problems/word-pattern/

Pattern:    hashmap bijection (one-to-one mapping), clue: "full match" / "bijection"
Key idea:
  - same as Isomorphic Strings (205), but with words
  - dict pattern -> word keeps each letter's mapping consistent
  - set of used words: no two letters share a word (only need membership)
  - check len(pattern) == number of words first
Complexity: O(n) time, O(n) space (n = len(s); the word list is the O(n) part)
Mistake I made:
  - forgot the length check (and it's the WORD count, not len(s))
  - without it zip() stops early: "abba" vs "dog cat cat dog fish" -> True
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        p2s = {}
        seen = set()

        for ch, w in zip(pattern, words):
            if ch not in p2s:
                if w in seen:
                    return False
                p2s[ch] = w
                seen.add(w)
            
            elif p2s[ch] != w:
                return False
        
        return True