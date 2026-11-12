"""
134. Gas Station  (Medium)
https://leetcode.com/problems/gas-station/

Pattern:    greedy one pass; clue = "circular route" + "unique start if one exists"
Key idea:
  - sum(gas) < sum(cost) -> no start works, return -1
  - otherwise a start exists: walk once, keep a running tank of gas - cost
  - tank < 0 at i -> no station from the current start up to i can be the start;
    reset tank, try start = i + 1
  - the last start that never went negative is the answer
Complexity: O(n) time, O(1) space
Mistake I made:
  - none; passed on the first run
  - v1 built a net_gain list first; not needed, gas[i] - cost[i] inline
"""


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            total += g - c
            if total < 0:
                total = 0
                res = i + 1

        return res
