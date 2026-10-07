"""
547. Number of Provinces  (Medium)
https://leetcode.com/problems/number-of-provinces/

Pattern:    union-find (DSU = Disjoint Set Union), clue: "count connected groups"
Key idea:
  - DSU is the whole forest, not one node: a parent array + a rank array for all n nodes
  - start: every node is its own root (parent[i] = i)
  - find: walk up to the root AND rewrite pointers on the way (path compression)
  - union: attach the shorter tree's root under the taller one; equal ranks -> +1
  - union returns True only when it really merges two groups
  - provinces starts at n, minus 1 for every successful union
  - matrix is symmetric, so only check one triangle (j < i)
Complexity: O(n^2 * α(n)) time, O(n) space
  - union by rank alone keeps the height at O(log n)
  - + path compression: amortized α(n) (inverse Ackermann, <= 4 in practice)
Mistake I made:
  - forgot that DSU is short for Disjoint Set Union
  - first designed it as a single node (UnionNode); it needs parent + rank for the whole tree
  - thought path compression meant "keep walking up"; it means rewriting parent[x]
  - find tested x but updated cur, so x never moved (infinite loop)
  - `return True` indented inside the else: merges into the taller root returned None
"""

from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False

        rank_x, rank_y = self.rank[rx], self.rank[ry]
        if rank_x < rank_y:
            self.parent[rx] = ry
        else:
            self.parent[ry] = rx
            if rank_x == rank_y:
                self.rank[rx] += 1

        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)
        provinces = n
        for i in range(n):
            for j in range(0, i):
                if isConnected[i][j] and dsu.union(i, j):
                    provinces -= 1

        return provinces
