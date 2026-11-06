"""
143. Reorder List  (Medium)
https://leetcode.com/problems/reorder-list/

Pattern:    find middle (fast/slow) + reverse second half + merge alternately
Key idea:
  - fast/slow: slow ends at the start of the second half; prev = node before slow
  - cut with prev.next = None -> first half head..prev, second half slow..end
  - reverse the second half, then alternate: first-half node, second-half node, ...
  - leftover node (second half is longer by one for odd n) gets attached at the end
Complexity: O(n) time, O(1) space
Mistake I made (v1, v2):
  - v1: cut slow.next = None, then reversed from fast (last node or None) -> second half lost
  - v2: reversed from slow AFTER cutting slow.next -> nodes after slow lost + slow in both halves (cycle)
  - lesson: after any x.next = None, ask "what did I cut off, and do I still hold a pointer to it?"
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        fast = slow = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        pre, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = pre
            pre, cur = cur, nxt

        left, right = head.next, pre

        cur = head
        while left and right:
            cur.next = right
            right = right.next
            cur = cur.next
            cur.next = left
            left = left.next
            cur = cur.next

        if left:
            cur.next = left
        if right:
            cur.next = right
