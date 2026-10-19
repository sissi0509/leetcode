"""
1836. Remove Duplicates From an Unsorted Linked List  (Medium, Premium)
https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

Pattern:    two passes: count first, then delete (unsorted -> duplicates aren't adjacent)
Key idea:
  - pass 1: seen + discard sets (a value seen twice goes into discard); a Counter works too
  - pass 2: dummy node (the head can be deleted), prev = last kept node
      cur.val in discard -> unlink cur (prev stays), else keep it (prev = cur)
  - can't beat O(n) time: deciding about a node needs the whole list
  - O(1) space only by trading time: compare every pair O(n^2), or sort first O(n log n)
    (loses the original order)
Complexity: O(n) time, O(n) space
Duplicates family: LC83 sorted, keep one | LC82 sorted, keep none | LC1836 unsorted, keep none
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        seen = set()
        discard = set()
        cur = head
        while cur:
            if cur.val in seen:
                discard.add(cur.val)
            else:
                seen.add(cur.val)
            cur = cur.next

        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur:
            if cur.val in discard:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return dummy.next
