"""
102. Binary Tree Level Order Traversal  (Medium)
https://leetcode.com/problems/binary-tree-level-order-traversal/

Pattern:    BFS, clue: "level by level"
Key idea:
  - queue starts with the root
  - each level: pop exactly len(queue) nodes, the size at the level's start
  - children added during that loop wait for the next level
  - range(len(queue)) is evaluated once, so it's a safe snapshot
Complexity: O(n) time, O(w) space (w = max width, at most about n/2)

"""

from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)

        return res
