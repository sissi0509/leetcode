"""
Lowest-Cost Shirts  (Medium, OA-style; = LC256 Paint House + return the colors)
n days, one shirt per day in blue/green/red with daily prices, never the same color on
consecutive days. Return the color list ('b'/'g'/'r') with the minimum total cost (unique).
e.g. blue [1,5,1], green [5,1,5], red [5,5,5] -> ['b', 'g', 'b'] (cost 3)

Pattern:    3-state DP + parent pointers, clue: "min total" + "no two in a row" + return the choices
Key idea:
  - dp[day][c] = cheapest total for days 0..day if I buy color c on that day
  - dp[day][c] = price[c][day] + min(dp[day - 1][other two colors])
  - prev[day][c] = which color day - 1 used for that min, so the choices can be rebuilt
  - rebuild: start at the cheapest color on the last day, follow prev back to day 0, reverse
Complexity: O(n) time (3 x 2 work per day), O(n) space for dp + prev
Mistake I made:
  - mixed up min and max (picked the most expensive previous color), color keys 1-3 vs 0-2
  - rebuild loop stopped at day 1, so day 0's color was missing ([] for n = 1)
  - returned [res][::-1] (list inside a list) / reversed(res) (an iterator, not a list)
"""


def lowest_cost(blue_costs, green_costs, red_costs):
    n = len(blue_costs)
    dp = [[0] * 3 for _ in range(n)]
    dp[0] = [blue_costs[0], green_costs[0], red_costs[0]]
    color_map = {0: blue_costs, 1: green_costs, 2: red_costs}
    prev = [[0] * 3 for _ in range(n)]
    color_str = {0: "b", 1: "g", 2: "r"}

    for day in range(1, n):
        for c in range(3):
            pre = float('inf')
            for prev_c in range(3):
                if prev_c == c:
                    continue
                if dp[day - 1][prev_c] < pre:
                    pre = dp[day - 1][prev_c]
                    prev[day][c] = prev_c
            dp[day][c] = color_map[c][day] + pre

    min_cost = dp[-1][0]
    last_c = 0
    for color, cost in enumerate(dp[-1]):
        if cost < min_cost:
            min_cost = cost
            last_c = color

    res = []
    for day in range(n - 1, -1, -1):
        res.append(color_str[last_c])
        last_c = prev[day][last_c]

    return res[::-1]


print(lowest_cost([1, 5, 1], [5, 1, 5], [5, 5, 5]))  # ['b', 'g', 'b']
print(lowest_cost([10], [3], [7]))                   # ['g']
