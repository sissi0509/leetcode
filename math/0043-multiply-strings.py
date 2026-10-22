"""
43. Multiply Strings  (Medium)
https://leetcode.com/problems/multiply-strings/

Pattern:    grade-school multiplication on a digit array (no int() on the whole string)
Key idea:
  - an m-digit number times an n-digit number has at most m + n digits -> res = [0] * (m + n)
  - num1[i] * num2[j] lands on positions i + j (tens) and i + j + 1 (ones)
  - go from the right (i, j descending) so carries flow left: add the product to res[i + j + 1],
    keep its last digit there, push the carry into res[i + j]
  - strip leading zeros at the end; "0" * anything -> "0"
Complexity: O(m * n) time, O(m + n) space
Mistake I made:
  - had no idea where to start -> solution shown (learn mode), retype owed
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                total = product + res[i + j + 1]
                res[i + j + 1] = total % 10           # ones digit stays here
                res[i + j] += total // 10             # carry goes one place left

        start = 0
        while start < len(res) - 1 and res[start] == 0:
            start += 1

        return "".join(str(d) for d in res[start:])
