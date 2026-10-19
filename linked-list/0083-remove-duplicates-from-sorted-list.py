"""
83. Remove Duplicates from Sorted List  (Easy)
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Pattern:    linked list, compare each node with the last kept node (sorted -> duplicates are adjacent)
Key idea:
  - prev = last kept node, cur = node being checked
  - same value -> skip cur (prev.next jumps over it), prev stays
  - new value  -> keep it, both move forward
  - the head is always kept, so no dummy node is needed
Complexity: O(n) time, O(1) extra space
Alternative: one pointer, `while cur and cur.next`: if cur.next.val == cur.val, cur.next = cur.next.next,
             else cur = cur.next
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head

        prev = head
        cur = head.next
        while cur:
            if cur.val == prev.val:
                cur = cur.next
                prev.next = cur
            else:
                prev, cur = cur, cur.next

        return head
