"""
138. Copy List with Random Pointer  (Medium)
https://leetcode.com/problems/copy-list-with-random-pointer/

Pattern:    linked list + hashmap (old node -> new node), clue: "deep copy" + pointers to arbitrary nodes
Key idea:
  - method 1 (hashmap): pass 1 creates every copy, map old -> new; pass 2 wires next/random
  - seed the map with {None: None}, so None pointers need no special case
  - method 2 (O(1) extra space): put each copy right after its original, A -> A' -> B -> B'
  - then copy of X is X.next, so copy.random = original.random.next
  - three passes: interleave, set randoms, split (restore originals + link copies)
Complexity:
  - method 1: O(n) time, O(n) extra space (the map)
  - method 2: O(n) time, O(1) extra space (not counting the output list)
Mistake I made:
  - method 1: loop 2 reused `copy` left over from loop 1 -> need copy = old_to_new[cur]
  - method 2: set randoms while splitting -> earlier originals' next already restored
  - method 2: forgot cur.next = nxt in the split -> original list left modified
  - None checks on X.random / X.next (fixed with `... if x else None`)
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


# Method 1: hashmap, O(n) extra space
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None: None}
        cur = head
        while cur:
            copy = Node(cur.val)
            old_to_new[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = old_to_new[cur]
            copy.random = old_to_new[cur.random]
            copy.next = old_to_new[cur.next]
            cur = cur.next

        return old_to_new[head]


# Method 2: interleave copies, O(1) extra space
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        while cur:
            copy = Node(cur.val)
            nxt = cur.next
            cur.next = copy
            copy.next = nxt
            cur = nxt

        cur = head
        while cur:
            copy = cur.next
            nxt = cur.next.next
            copy.random = cur.random.next if cur.random else None
            cur = nxt

        cur = head
        new_head = cur.next
        while cur:
            copy = cur.next
            nxt = cur.next.next
            cur.next = nxt
            copy.next = nxt.next if nxt else None
            cur = nxt

        return new_head
