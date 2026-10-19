"""
124. Binary Tree Maximum Path Sum  (Hard)
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Pattern:    tree DFS, "return one value up, track another globally"
Key idea:
  - return to the parent: best path that STARTS at this node and goes down one side
      node.val + max(0, left, right)   (0 = take neither child)
    a parent can only extend a path that doesn't fork
  - track globally: best path that BENDS at this node
      node.val + max(0, left) + max(0, right)   (can't be returned: it forks)
  - clamp negative children to 0: a negative branch only hurts
  - global max starts at -inf: all-negative trees (single node -3 -> -3)
Complexity: O(n) time (each node visited once, O(1) work each),
            O(h) space for the recursion stack: O(log n) balanced, O(n) skewed (a chain)
Mistake I made:
  - single path = node.val + max(left, right) with no 0 option -> forced a negative child in
    ([1, 10, null, -1, -1] -> 10 instead of 11); hidden in small tests because a missing child
    returns 0
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_sum = [float('-inf')]

        def find_max(node):
            if not node:
                return 0

            left_path, right_path = find_max(node.left), find_max(node.right)
            single_path = node.val + max(0, left_path, right_path)
            across_path = node.val + max(0, left_path) + max(0, right_path)

            max_sum[0] = max(max_sum[0], single_path, across_path)

            return single_path

        find_max(root)
        return max_sum[0]
