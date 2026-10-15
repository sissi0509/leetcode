"""
142. Linked List Cycle II  (Medium)
https://leetcode.com/problems/linked-list-cycle-ii/

Pattern:    Fast/slow pointers (Floyd), clue: "where does the cycle begin", O(1) space follow-up
Key idea:
  - set version: the first node seen twice is the cycle start (O(n) space)
  - Floyd phase 1: slow +1, fast +2; they meet only if there's a cycle
  - Floyd phase 2: move one pointer back to head, step both by 1; they meet at the start
  - why: a = head->start, b = start->meet, c = cycle length.
    fast walked twice as far: 2(a + b) = (a + b) + k*c, so a = k*c - b.
    walking a steps from meet = back b steps + whole laps = the start
  - guard `fast and fast.next`: fast jumps 2, so both must exist
Complexity: set O(n) time, O(n) space; Floyd O(n) time, O(1) space
Mistake I made:
  - put "not met yet" in the while condition (`... or fast != slow`): they start equal,
    and the `or` kept it true -> infinite loop with a cycle, crash without one
"""


class SolutionSet:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        cur = head
        while cur and cur not in seen:
            seen.add(cur)
            cur = cur.next

        return cur


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:                 # phase 1 done: there's a cycle
                slow = head                  # phase 2: one pointer back to head
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                return slow                  # they meet at the cycle start
        return None                          # fast hit the end: no cycle
