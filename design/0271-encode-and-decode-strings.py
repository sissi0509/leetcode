"""
271. Encode and Decode Strings  (Medium, Premium)
https://leetcode.com/problems/encode-and-decode-strings/

Pattern:    string design / length header; clue = "strings can contain ANY character" -> no safe separator
Key idea:
  - joining with "," fails: ["a,b", "c"] and ["a", "b", "c"] both give "a,b,c"
  - write the lengths first: "count,len1,len2,...," then all strings glued together
  - decode reads the header (only digits and commas), then cuts the strings by length
  - the content is never searched, so a comma inside a string can't confuse it
  - standard alternative: length prefix per string, "5#Hello5#World"
Complexity: O(total length) time and space
Mistake I made:
  - loop index not moving (`i += 1` missing / inside the `if`) -> infinite loop
  - off by one: start at r + 1 and slice w_len + 1 -> skipped/extra characters
  - ",".join(...) puts no comma after the LAST length -> decode ran into the content
"""

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        words_len = [str(len(strs))]
        for string in strs:
            words_len.append(str(len(string)))

        return ",".join(words_len) + "," + "".join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if s[0] == "0":
            return []

        cur = 0
        while s[cur] != ",":
            cur += 1
        total_len = int(s[:cur])

        words_len = []
        l = r = cur + 1
        cnt = 0
        while cnt < total_len:
            if s[r] == ",":
                words_len.append(int(s[l:r]))
                cnt += 1
                l = r + 1
            r += 1
        cur = r

        res = []
        for word_len in words_len:
            res.append(s[cur: cur + word_len])
            cur += word_len

        return res
