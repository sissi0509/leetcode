"""
49. Group Anagrams  (Medium)
https://leetcode.com/problems/group-anagrams/

Pattern:    hashmap with a canonical key, clue: "group things that are equivalent"
Key idea:   All anagrams share one "signature", so use it as the dict key and
            collect words in key -> list. A Counter can't be the key (mutable,
            unhashable), so:
              v1: sorted string as key      -> "".join(sorted(s))
              v2: tuple of 26 letter counts -> no sorting needed
Complexity: v1 O(n * k log k) time, v2 O(n * k) time; both O(n * k) space
            (n = number of strings, k = max string length)
Mistake I made: Thought sorted("eat") returns a string; it returns a LIST
            (unhashable), so it needs "".join(...) or tuple(...). Also forgot to
            import defaultdict; it only passes on LeetCode's auto-imports.
"""

from collections import defaultdict


# v1: sorted-string key, O(n * k log k)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            res[key].append(string)
        
        return list(res.values())


# v2: letter-count tuple key, O(n * k)
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        def anagram_key(string):
            counts = [0] * 26
            for ch in string:
                counts[ord(ch) - ord('a')] += 1
            
            return tuple(counts)

        for string in strs:
            key = anagram_key(string)
            res[key].append(string)
        
        return list(res.values())