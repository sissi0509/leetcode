"""
Network Endpoint  (Easy/Medium, OA-style, no LeetCode number)
compute(start_node_id, from_ids, to_ids): link i is from_ids[i] -> to_ids[i], every node has
at most one outgoing link. Follow the links from start and return the last node reached:
the dead end, or with a loop, the last new node before a node would repeat.
e.g. 1->2->3->4 -> 4,  1->2->3->1 -> 3,  1->2->3->4->2 -> 4,  start 7 with no links -> 7

Pattern:    Walk a "one next pointer" graph (like a linked list), clue: "at most one outgoing"
Key idea:
  - dict node -> next node, built with zip(from_ids, to_ids)
  - walk until the node has no next (dead end) or the next one is already visited (loop)
  - keep the previous node: when the loop stops on a repeated node, the answer is the one before it
  - the problem statement doesn't say what a loop returns: check the examples on the real test
Complexity: O(n) time, O(n) space, n = number of links
Mistake I made:
  - first version returned -1 for a loop: it stepped onto the repeated node and lost the previous one
Twins: LC142 (cycle start), LC2359, LC2360
"""


def compute(start_node_id, from_ids, to_ids):
    graph = {}
    for u, v in zip(from_ids, to_ids):
        graph[u] = v

    if start_node_id not in graph:
        return start_node_id

    visited = set()
    cur = start_node_id
    while cur in graph and cur not in visited:
        visited.add(cur)
        pre = cur
        cur = graph[cur]

    if cur in visited:
        return pre
    return cur


print(compute(1, [1, 2, 3], [2, 3, 4]))        # 4
print(compute(1, [1, 2, 3], [2, 3, 1]))        # 3
print(compute(1, [1, 2, 3, 4], [2, 3, 4, 2]))  # 4
print(compute(7, [1, 2], [2, 3]))              # 7
