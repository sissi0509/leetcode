"""
743. Network Delay Time  (Medium)
https://leetcode.com/problems/network-delay-time/

Pattern:    Dijkstra (min-heap), clue: "shortest time" + weighted edges
Key idea:
  - BFS finds the fewest edges; that's only the shortest path when every edge costs 1
  - min-heap of (distance, node): distance first, so the heap orders by it
  - every node starts at infinity, the source at 0
  - nodes are 1-indexed: list of size n + 1, dis[0] = 0 so it can't break max()
  - pop the closest unfinished node; its distance is final (weights are non-negative)
  - a node is finalized when POPPED, so visited starts empty (not like BFS)
  - the heap keeps old (distance, node) tuples: a tuple copies the value at push time,
    so later updates to dis[v] don't change it -> skip nodes already visited
  - answer = max(dis); infinity means some node is unreachable -> -1
Complexity: O(E log E) = O(E log V) time, O(V + E) space
Mistake I made:
  - u = heappop(hp) kept the whole (distance, node) tuple, so graph[u] was always []
  - started visited with the source (BFS habit), so the source skipped itself
"""

import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dis = [float('inf')] * (n + 1)
        dis[0] = 0
        dis[k] = 0

        hp = [(0, k)]
        visited = set()

        while hp:
            u = heapq.heappop(hp)[1]
            if u in visited:
                continue

            visited.add(u)
            for v, w in graph[u]:
                if v not in visited:
                    dis[v] = min(dis[v], dis[u] + w)
                    heapq.heappush(hp, (dis[v], v))

        longest = max(dis)

        return longest if longest < float('inf') else -1
