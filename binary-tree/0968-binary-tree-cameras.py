"""
968. Binary Tree Cameras  (Hard)
https://leetcode.com/problems/binary-tree-cameras/

Pattern:    bottom-up greedy (post-order), each child reports a state to its parent
            clue = "fewest X so that every node is covered" on a tree
Key idea:
  - the deepest nodes force decisions: a leaf is best covered by a camera on its PARENT
    (covers more than a camera on the leaf) -> leaves never get a camera
  - states: 0 = not covered, 1 = covered (no camera), 2 = has camera
  - rules for a node, after both children:
      any child 0          -> place a camera here, return 2
      else any child 2     -> covered by the child, return 1
      else (both 1)        -> not covered, return 0 (let the parent cover me)
  - None returns 1 (covered): it never forces a camera and never covers anyone
  - the root has no parent: if it returns 0, add one more camera
  - same greedy as "Snapshot Budget": wait as long as possible, place as high as allowed
Complexity: O(n) time, O(h) space (recursion stack)
Mistake I made: forgot the root check (single node gave 0 instead of 1);
                needed hints to see it as greedy and to define the 3 states
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode | None) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            # 0: not covered, 1: covered, 2: camera
            if not node:
                return 1
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 0 or right == 0:
                res += 1
                return 2
            if left == 2 or right == 2:
                return 1
            return 0

        if dfs(root) == 0:
            res += 1
        return res
