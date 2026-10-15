"""
Magic Stones  (Medium, OA-style, CodinGame-style puzzle, no LeetCode number)
Two stones of level n merge into one stone of level n + 1. Return the minimum number of
stones left after any number of merges. 0 < level < 10000, at least one stone.
e.g. [1, 2, 1] -> 1,  [3, 3, 3] -> 2,  [1, 1, 1, 1] -> 1,  [5] -> 1

Pattern:    Counting + carry (like adding binary numbers, LC67), clue: "two equal -> one bigger"
Key idea:
  - count stones per level in a list, then sweep levels from low to high
  - at each level: count % 2 stones are left over (add to the answer),
    count // 2 pairs become count // 2 stones one level up (the carry)
  - the order of merges doesn't matter: leftovers are fixed, like binary digits
  - carries can go above 9999, so the list needs extra room:
    each carry halves the count, so about log2(n) extra levels are enough (n // 2 is plenty)
  - changing levels[i + 1] while sweeping is safe: the loop reads it only when it gets there
Complexity: O(n + L) time, L = number of levels (~10000 + log n); O(L) space
Mistake I made:
  - first carry line was levels[i + cnt // 2] += 1 (one stone at level i + pairs);
    it should be levels[i + 1] += cnt // 2 (pairs stones at the next level)
"""


def magic(stones):
    length = max(stones) + len(stones) // 2 + 1
    levels = [0] * (length + 1)

    for num in stones:
        levels[num] += 1

    res = 0
    for i in range(length):
        cnt = levels[i]
        res += cnt % 2
        levels[i + 1] += cnt // 2
    return res


print(magic([1, 2, 1]))     # 1
print(magic([3, 3, 3]))     # 2
print(magic([1, 1, 1, 1]))  # 1
print(magic([5]))           # 1
