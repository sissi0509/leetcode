"""
297. Serialize and Deserialize Binary Tree  (Hard)
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Pattern:    BFS with null markers (LeetCode's own format), both directions
Key idea:
  - serialize: pop a real node -> write its value, enqueue BOTH children (None included);
    pop a None -> write "null", enqueue NOTHING (only real nodes have child slots)
    -> the queue empties by itself; n nodes give at most 2n + 1 entries
  - deserialize: same order; one moving index into the value list; for every REAL parent
    popped from the queue, the next two values are its left and right child
    ("null" -> None, not enqueued); values go back through int()
  - separator "," so negative / multi-digit values survive the round trip
DFS version (CodecDFS): preorder (root, left, right) with "null" for missing children;
  decode with one shared index (nonlocal i; or iter() + next()): next value -> "null" means None, else build root, then left, then right
  (the nulls tell the decoder where each subtree ends; preorder puts the root first, inorder can't)
Complexity: O(n) time and O(n) space for both (DFS: O(h) recursion stack)
Mistake I made (v1):
  - serialize gave every None two None children (full-tree slots): mismatched with deserialize
    and exponential on a skewed tree
  - deserialize: TreeNode([nodes[cur]]) (a list, not an int), "null" turned into a real node,
    second child read without a bounds check
"""

from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        if not root:
            return "null"

        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")

        return ",".join(res)

    def deserialize(self, data):
        if data == "null":
            return None

        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        queue = deque([root])
        i = 1

        while queue:
            node = queue.popleft()

            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1

            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1

        return root


class CodecDFS:

    def serialize(self, root):
        res = []

        def dfs(node):
            if not node:
                res.append("null")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        i = 0                                   # next unread value, shared by all calls

        def build():
            nonlocal i
            val = vals[i]
            i += 1
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()
