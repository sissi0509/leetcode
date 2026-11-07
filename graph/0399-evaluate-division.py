"""
399. Evaluate Division  (Medium)
https://leetcode.com/problems/evaluate-division/

Pattern:    weighted graph + DFS per query; clue = a/b = v chains -> multiply along a path
Key idea:
  - edge a -> b with weight v, and b -> a with weight 1 / v
  - a query a/c = product of the weights on any path from a to c; no path -> -1.0
  - check "unknown variable" BEFORE a == target (x / x with unknown x is -1.0)
  - one fresh visited set per query; never un-mark -> each node at most once, O(V + E) per query
    (un-marking = backtracking -> can blow up exponentially on dense graphs)
  - mark on entry (SolutionMarkOnEntry): `if a in visited: return -1; visited.add(a)`
Complexity: O(Q * (V + E)) time, O(V + E) space
Mistake I made:
  - v1: one visited set shared by ALL queries; found paths returned before discard -> later queries blocked
  - v1: a == target checked before the unknown-variable check -> x / x returned 1.0
  - v2: `visited + {b}` (TypeError: sets use |) and a new set per call = per-path visited
"""

from collections import defaultdict


class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        def dfs(a, target, cur, visited):
            if a not in graph or target not in graph:
                return -1.0
            if a == target:
                return cur
            for b, v in graph[a]:
                if b not in visited:
                    visited.add(b)
                    q = dfs(b, target, cur * v, visited)
                    if q != -1.0:
                        return q
                    visited.discard(b)
            return -1.0

        res = []
        for a, b in queries:
            res.append(dfs(a, b, 1.0, {a}))

        return res


class SolutionMarkOnEntry:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        graph = defaultdict(list)
        for (a, b), v in zip(equations, values):
            graph[a].append((b, v))
            graph[b].append((a, 1 / v))

        def dfs(a, target, cur, visited):
            if a == target:
                return cur
            visited.add(a)
            for b, v in graph[a]:
                if b not in visited:
                    q = dfs(b, target, cur * v, visited)
                    if q != -1.0:
                        return q
            return -1.0

        res = []
        for a, b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(a, b, 1.0, set()))
        return res
