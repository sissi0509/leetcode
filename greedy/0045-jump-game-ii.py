"""
45. Jump Game II  (Medium)
https://leetcode.com/problems/jump-game-ii/

Pattern:    greedy "BFS by levels": the indices reachable with k jumps form one window [start, end]
Key idea:
  - scan the current window, track the farthest index the next jump can reach
  - the next window is [end + 1, farthest]; one window = one jump
  - stop as soon as farthest >= n - 1
  - cleaner form (SolutionSimple): one pass over i < n - 1; when i reaches the end of the current
    window, take a jump and set end = farthest. n == 1 needs no special case (the loop never runs)
Complexity: O(n) time (every index scanned once), O(1) space
Mistake I made:
  - step started at 1, so a single-element array (already at the end) needed a special case
    -> trace n = 1 every time; count jumps when they happen instead of starting at 1
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        start, end, far = 0, 0, 0
        n = len(nums)
        if n == 1:
            return 0

        step = 1

        while start <= end:
            far = end
            for i in range(start, end + 1):
                far = max(i + nums[i], far)
                if far >= n - 1:
                    return step

            start, end = end + 1, far
            step += 1

        return -1


class SolutionSimple:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        end = 0                      # last index reachable with `jumps` jumps
        far = 0                      # farthest index reachable with one more jump
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == end:             # used up the current window: must jump
                jumps += 1
                end = far
        return jumps
