"""
133. Clone Graph  (Medium)
https://leetcode.com/problems/clone-graph/

Pattern:    DFS + hashmap (original -> copy), clue: "deep copy" of a graph that can have cycles
Key idea:
  - the dict does two jobs: visited set AND lookup from an original node to its copy
  - put the copy into the dict BEFORE recursing into neighbors,
    so a cycle back to this node finds it and returns instead of looping forever
  - {None: None} seed: clone(None) returns None, so the empty input needs no special case
  - first version was two passes (copy nodes, then wire neighbors); it works, but
    one pass does the same work with less code
Complexity: O(V + E) time, O(V) extra space (dict + recursion stack)
Mistake I made:
  - said O(E) time: write O(V + E), the nodes cost work even with no edges
"""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_copy = {None: None}

        def clone(node):
            if node in node_copy:
                return node_copy[node]

            copy = node_copy[node] = Node(node.val)
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))

            return copy

        return clone(node)
