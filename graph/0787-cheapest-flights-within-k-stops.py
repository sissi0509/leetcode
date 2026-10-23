"""
787. Cheapest Flights Within K Stops  (Medium)
https://leetcode.com/problems/cheapest-flights-within-k-stops/

Pattern:    Dijkstra with an extra dimension in the state: (cost, city, stops)
Key idea:
  - plain Dijkstra fails: the cheapest path may use too many stops, and once a city is settled
    a pricier path with FEWER stops is thrown away -> the state must be (city, stops)
  - stops = flights - 1 (a stop is a city in the middle); a direct flight arrives with 0 stops,
    flying on from a city makes it a stop -> next state has stops + 1; expand only if stops < k
  - k = 0 still allows direct flights (no early return -1)
  - the heap pops in cost order (non-negative prices) -> the first time dst is popped is the answer
  - skip a (city, stops) state that was already expanded: without it, duplicate entries get
    re-expanded again and again -> Time Limit Exceeded
Complexity: about n * (k + 1) states, each expanded once over its out-edges -> O(E * k * log(E * k))
Alternative: Bellman-Ford limited to k + 1 rounds (copy the cost array each round), O(k * E)
Mistake I made:
  - counted flights but compared with k as if they were stops (off by one) -> k = 1 returned 500
  - kept an `if k < 1: return -1` guard -> k = 0 lost the direct flight
  - set((src, 0)) is {src, 0}, not {(src, 0)} (set() iterates its argument)
  - no skip for already-visited states at pop time -> TLE
"""

import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))

        heap = [(price, target, 0) for (target, price) in graph[src]]
        heapq.heapify(heap)

        visited = {(src, 0)}

        while heap:
            price, node, stop = heapq.heappop(heap)
            if (node, stop) in visited:
                continue
            if node == dst:
                return price
            visited.add((node, stop))
            if stop >= k:
                continue

            for to_city, p in graph[node]:
                if (to_city, stop + 1) not in visited:
                    heapq.heappush(heap, (price + p, to_city, stop + 1))

        return -1
