"""
25. Reverse Nodes in k-Group  (Hard)
https://leetcode.com/problems/reverse-nodes-in-k-group/

Pattern:    linked-list pointer surgery: dummy node + "cut, reverse, reconnect" per group
Key idea:
  - dummy node, because the head changes after the first group; return dummy.next
  - tail = the node just before the current group (starts at dummy)
  - per group: walk k - 1 steps to find the group's last node; fewer than k left -> stop
  - cut the group off (cur_tail.next = None), reverse it, and reverse returns (new_head, new_tail):
    the old first node is the new last node
  - tail.next = new_head, tail = new_tail, then tail.next = the rest of the list
Complexity: O(n) time (each node is walked once to check, once to reverse), O(1) extra space
Mistake I made:
  - list length a multiple of k ([1, 2], k = 2): after the last group cur_head is None,
    but the loop ran again and did None.next -> fixed with `while can_reverse and cur_head`
  - list shorter than k ([1], k = 2): no group reversed, dummy.next never set -> returned []
    -> fixed by doing `tail.next = cur_head` on every pass, not only after a reverse
  - test 3 sizes: shorter than k, a multiple of k, a leftover tail
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if k == 1:
            return head

        def reverse(head):
            prev = None
            cur = head

            while cur:
                nxt = cur.next
                cur.next = prev
                prev, cur = cur, nxt

            return prev, head

        dummy = ListNode()
        tail = dummy
        cur_head = head
        can_reverse = True

        while can_reverse and cur_head:
            cur_tail = cur_head
            for i in range(k - 1):
                cur_tail = cur_tail.next
                if not cur_tail:
                    can_reverse = False
                    break

            if can_reverse:
                next_head = cur_tail.next
                cur_tail.next = None
                new_head, new_tail = reverse(cur_head)
                tail.next = new_head
                tail = new_tail
                cur_head = next_head

            tail.next = cur_head

        return dummy.next
