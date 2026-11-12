"""
863. All Nodes Distance K in Binary Tree  (Medium)
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

Pattern:    tree -> undirected graph (parent map) + BFS by levels; clue = "distance k" from a node that isn't the root
Key idea:
  - a tree node only knows its children; distance can also go UP
  - DFS once to record parent[child] = node -> every node has 3 neighbors: left, right, parent
  - BFS from target, one level per step, visited set so we never walk back
  - after k levels the queue holds exactly the nodes at distance k
  - queue empty before k levels -> no node that far -> []
Complexity: O(n) time, O(n) space (parent map + visited + queue)
Mistake I made:
  - none; passed on the first run
  - parent.get(node) does the same as `parent[node] if node in parent else None`
"""

from collections import deque
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: "TreeNode", target: "TreeNode", k: int) -> List[int]:
        parent = {}

        def find_parent(node):
            if node.left:
                parent[node.left] = node
                find_parent(node.left)
            if node.right:
                parent[node.right] = node
                find_parent(node.right)

        find_parent(root)

        visited = set()
        queue = deque([target])
        visited.add(target)

        res = []
        for _ in range(k):
            if not queue:
                return []
            for _ in range(len(queue)):
                node = queue.popleft()
                parent_node = parent[node] if node in parent else None
                for nxt in [node.left, node.right, parent_node]:
                    if nxt and nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

        for _ in range(len(queue)):
            res.append(queue.popleft().val)

        return res
