"""
23. Merge k Sorted Lists  (Hard)
https://leetcode.com/problems/merge-k-sorted-lists/

Pattern:    divide & conquer (merge sort where each "element" is a whole list) + merge two sorted lists;
            or a min-heap of the k list fronts (k-way merge)
Key idea:
  - split the k lists into two halves, merge each half recursively, then merge the two results
  - base cases: 0 lists -> None, 1 list -> that list
  - split point must leave >= 1 list on each side: mid = len(lists) // 2
  - merge two lists: dummy node + cur pointer, attach the leftover tail at the end
Complexity: O(n log k) time (log k levels, every node touched once per level),
            O(log k) recursion stack (+ slice copies; pass (lo, hi) indices to avoid them)
Heap version:
  - heap holds one front node per list: push every non-empty head, pop the smallest, push its .next
  - push (val, i, node): i breaks ties so heapq never compares two ListNodes (TypeError);
    only one node per list is in the heap at a time, so i is unique inside it
  - O(N log k) time (N pops/pushes on a heap of size <= k), O(k) heap space
Mistake I made:
  - mid = (l + r) // 2 with l, r = 0, len - 1 -> for 2 lists mid = 0, lists[:0] is empty,
    lists[0:] is the same 2 lists -> infinite recursion
  - forgot cur = cur.next in merge -> every step overwrote dummy.next, nodes lost
  - heap v1: hp.pop() (plain list pop = last item, not the smallest), no tie-breaker,
    no filter for empty lists (None.val)
"""

import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2

        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode()
        cur = dummy

        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        if left:
            cur.next = left
        if right:
            cur.next = right

        return dummy.next


class SolutionHeap:
    def mergeKLists(self, lists):
        hp = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(hp)

        dummy = ListNode()
        cur = dummy
        while hp:
            val, i, node = heapq.heappop(hp)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(hp, (node.next.val, i, node.next))

        return dummy.next
