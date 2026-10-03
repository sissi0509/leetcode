"""
290. Word Pattern  (Easy)
https://leetcode.com/problems/word-pattern/

Pattern:    hashmap bijection (one-to-one mapping), clue: "full match" / "bijection"
Key idea:   Same as Isomorphic Strings (205), but with words. One dict pattern -> word
            keeps the mapping consistent; a set of used words makes sure no two
            letters share a word. A set is enough for the reverse direction because
            I only need membership.
Complexity: O(n) time, O(n) space (n = len(s); the word list is the O(n) part)
Mistake I made: Forgot to compare len(pattern) with the number of WORDS (not len(s)).
            Without it, zip() stops early: "abba" vs "dog cat cat dog fish" -> True.
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