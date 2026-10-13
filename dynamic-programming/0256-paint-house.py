"""
256. Paint House  (Medium, Premium)
https://leetcode.com/problems/paint-house/

Pattern:    DP with a small fixed state (3 colors), clue: "no two adjacent the same" + minimize cost
Key idea:
  - dp[c] = cheapest total so far with the CURRENT house painted color c
  - new[c] = cost[i][c] + min(dp of the other two colors)    (dp[:c] + dp[c+1:])
  - only the previous row matters -> two rows of 3 numbers, O(1) space
  - variant (ElevenLabs OA "Lowest-Cost Shirts"): return the COLOR SEQUENCE, not the cost
      keep the full table + prev[h][c] = the color used the day before in that plan,
      pick the cheapest color on the last day, walk back through prev, reverse
      (the full table is needed only because the path is rebuilt)
Complexity: O(n) time; O(1) space for the cost, O(n) for the color sequence
Mistake I made:
  - new_dp = costs[i] is an alias, not a copy -> silently rewrote the input; use costs[i][:]
  - created new_dp inside the color loop (only worked because it was the same object)
  - colors version: prev sized by 3 instead of n; read dp[h-1][c] instead of the loop
    variable dp[h-1][i]; `=` instead of `+=` (lost today's price); compared a whole row
    dp[c] to a number; appended `last` instead of the current color on the walk back
"""


class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        dp = costs[0][:]
        for i in range(1, len(costs)):
            new_dp = costs[i][:]
            for color in range(3):
                new_dp[color] += min(dp[:color] + dp[color + 1:])
            dp = new_dp
        return min(dp)


def min_cost_colors(costs: list[list[int]]) -> list[int]:
    """Variant: return the cheapest color sequence (0/1/2 per house) instead of the cost."""
    n = len(costs)
    dp = [row[:] for row in costs]
    prev = [[-1] * 3 for _ in range(n)]

    for h in range(1, n):
        for c in range(3):
            best = min((i for i in range(3) if i != c), key=lambda i: dp[h - 1][i])
            dp[h][c] += dp[h - 1][best]
            prev[h][c] = best

    c = min(range(3), key=lambda k: dp[-1][k])
    res = []
    for h in range(n - 1, -1, -1):
        res.append(c)
        c = prev[h][c]
    return res[::-1]
