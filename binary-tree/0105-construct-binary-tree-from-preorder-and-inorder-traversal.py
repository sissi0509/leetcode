"""
105. Construct Binary Tree from Preorder and Inorder Traversal  (Medium)
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Pattern:    recursive DFS with a shared preorder index; clue = "preorder" gives roots in order,
            "inorder" tells which values sit left / right of a root
Key idea:
  - values are unique (check the constraints) -> map value -> inorder index, O(1) lookups
  - each call owns an inorder range [left, right] = exactly the nodes of one subtree
  - next preorder value is this subtree's root, unless its inorder index is outside the range
    (then the subtree is empty -> return None without consuming it)
  - build LEFT before RIGHT: preorder is root, left subtree, right subtree
  - simpler base case: `if left > right: return None` (then the idx guard and range check go away)
Complexity: O(n) time, O(n) space (map + O(h) recursion stack)
Mistake I made (v1):
  - base case flipped: `if left <= right: return None` -> every call returned None
  - `inorder[num]` (indexing the list by a value) instead of `inorder_map[num]`
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_map = {}
        for i, num in enumerate(inorder):
            inorder_map[num] = i

        idx = 0

        def dfs(left, right):
            nonlocal idx
            if idx >= len(preorder):
                return None

            num = preorder[idx]
            in_idx = inorder_map[num]
            if not left <= in_idx <= right:
                return None
            node = TreeNode(num)

            idx += 1
            node.left = dfs(left, in_idx - 1)
            node.right = dfs(in_idx + 1, right)

            return node

        return dfs(0, len(preorder) - 1)
