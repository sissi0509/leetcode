"""
82. Remove Duplicates from Sorted List II  (Medium)
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Pattern:    linked list + dummy node, "skip the whole run" (vs LC83: keep one copy)
Key idea:
  - dummy node: the head itself can be deleted ([1, 1, 2] -> [2])
  - prev = last node we KEEP, cur = node being checked
  - cur.val == cur.next.val -> a run starts: save val, move cur past EVERY node with that val,
    then prev.next = cur (unlink the whole run); prev stays
  - otherwise cur is unique (it differs from the node before it, which was kept or skipped,
    and from the node after it) -> keep it: prev, cur = cur, cur.next
Complexity: O(n) time, O(1) extra space
Mistake I made:
  - inner loop `while cur.val == cur.next.val` -> crashed at the end ([1, 1]: cur.next is None)
  - stopped on the LAST copy and linked prev to it -> kept one copy (LC83 behavior)
    -> fix: save val, skip while cur and cur.val == val, so cur lands on the first node after the run
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        dummy.next = head
        cur = head
        prev = dummy

        while cur and cur.next:
            if cur.val == cur.next.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                prev.next = cur
            else:
                prev, cur = cur, cur.next

        return dummy.next
