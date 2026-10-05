"""
103. Binary Tree Zigzag Level Order Traversal  (Medium)
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Pattern:    BFS, clue: "level by level", alternating direction
Key idea:
  - same as 102: pop len(queue) nodes per level
  - a flag left_to_right flips after every level
  - always push children left then right; reverse the level list when needed
Complexity:
  - O(n) time: each node is reversed at most once, so the reverses add up to O(n)
  - O(w) space for the queue
"""

from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()
            res.append(level)
            left_to_right = not left_to_right

        return res
