"""
55. Jump Game  (Medium)
https://leetcode.com/problems/jump-game/

Pattern:    Greedy (max reach), clue: yes/no "can you reach the end", jumps of "at most" nums[i]
Key idea:
  - track `furthest`: the furthest index reachable so far
  - visit each index: if i > furthest, nothing before it can get there -> False
    otherwise furthest = max(furthest, i + nums[i])
  - why one number is enough: if I can reach index 7, I can reach index 5 (take a shorter jump),
    so the reachable indices are always one block [0, furthest] with no gaps
  - it never commits to a jump (unlike "always take the biggest jump", which fails on [2, 5, 0, 0]),
    so there is no risky greedy choice to prove
  - early exit: once furthest reaches the last index, return True
Complexity: O(n) time, O(1) space
Mistake I made:
  - didn't think of the early return at first (found it while explaining)
  - early exit uses `== n - 1`; `>= n - 1` is better because the reach often overshoots
    ([5, 0, 0] never hits == 2, so it scans the whole array; still correct, just slower)
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        furthest = 0
        n = len(nums)

        for i, num in enumerate(nums):
            if i > furthest:
                return False
            furthest = max(furthest, i + num)
            if furthest == n - 1:
                return True

        return True
