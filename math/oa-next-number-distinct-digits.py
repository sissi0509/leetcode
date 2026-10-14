"""
Next Number with No Shared Digits  (Medium, OA-style, no LeetCode number)
Smallest integer > n whose digits share none of n's digits; -1 if none.  1 <= n < 2^31
e.g. 654321 -> 700000, 89 -> 100, 10 -> 22, 2020 -> 3111, 123456789 -> -1

Pattern:    Construct the answer digit by digit, clue: brute force from n + 1 can take
            over a billion steps (2,000,000,000 -> 3111111111)
Key idea:
  - n's leftmost digit is banned, so the answer's leftmost digit can't stay the same,
    and it can't get smaller (the number would be smaller) -> only two cases:
    1. same length: smallest allowed digit > n's leftmost, then fill with the smallest allowed digit
    2. one digit longer: smallest non-zero allowed digit, then fill with the smallest allowed digit
  - -1 when every digit 1-9 is used (only 0 left, and a number can't start with 0)
Complexity: O(d) time, d = number of digits (<= 10); O(d) space for the answer string
Mistake I made:
  - first version counted digits with not_seen[d] -= 1; repeated digits made it -1,
    and `if not_seen[i]:` treats -1 as True (1123456789 -> 0 instead of -1)
  - after str(n) the digits are characters: compare with '0', not 0 ('0' != 0 is always True)
"""


def find_next(num):
    num_str = str(num)
    allowed = [d for d in "0123456789" if d not in num_str]
    non_zero = [d for d in allowed if d != '0' ]

    if not non_zero:
        return -1

    bigger = -1
    for d in allowed:
        if d > num_str[0]:
            bigger = d
            break
    if bigger == -1:
        return int(non_zero[0] + allowed[0] * len(num_str))

    return int(bigger + allowed[0] * (len(num_str) - 1))


print(find_next(654321))     # 700000
print(find_next(89))         # 100
print(find_next(10))         # 22
print(find_next(2020))       # 3111
print(find_next(123456789))  # -1
