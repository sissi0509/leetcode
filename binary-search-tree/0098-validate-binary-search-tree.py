"""
98. Validate Binary Search Tree  (Medium)
https://leetcode.com/problems/validate-binary-search-tree/

Pattern:    DFS (or BFS) passing down a valid range, clue: "every node in the
            left/right subtree", a rule about whole subtrees, not just children
Key idea:
  - checking only direct children isn't enough (5 -> right 7 -> left 4 fails)
  - each node gets a range (lower, upper); the root gets (-inf, inf)
  - left child: keeps the parent's lower bound, parent's value becomes upper
  - right child: parent's value becomes lower, keeps the parent's upper bound
  - strict < on both sides, so duplicates are invalid
  - BFS works too: store (node, lower, upper) in the queue, order doesn't matter
Complexity:
  - O(n) time for both
  - DFS: O(h) space (O(log n) balanced, O(n) skewed)
  - BFS: O(w) space (about n/2 on the last level of a complete tree)
Mistake I made:
  - first rule gave each child only one bound; forgot the inherited one
  - typos: upper.val on a float, isValide, node,val instead of node.val
"""

from collections import deque


# Method 1: DFS (recursive)
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def isValid(node, lower, upper):
            if not node:
                return True
            if not lower < node.val < upper:
                return False

            return (
                isValid(node.left, lower, node.val)
                and isValid(node.right, node.val, upper)
            )

        return isValid(root, float('-inf'), float('inf'))


# Method 2: BFS (queue of node + its range)
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        queue = deque([(root, float('-inf'), float('inf'))])

        while queue:
            node, lower, upper = queue.popleft()
            if node.left:
                if not lower < node.left.val < node.val:
                    return False
                queue.append((node.left, lower, node.val))
            if node.right:
                if not node.val < node.right.val < upper:
                    return False
                queue.append((node.right, node.val, upper))

        return True
