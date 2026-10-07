"""
2050. Parallel Courses III  (Hard)
https://leetcode.com/problems/parallel-courses-iii/

Pattern:    topological sort (Kahn's BFS) + DP on the DAG, clue: "prerequisites" + "minimum time"
Key idea:
  - edge pre -> nxt; indegree[nxt] counts unfinished prerequisites
  - courses are 1-indexed: subtract 1 before using them as indices
  - seed the queue with course indices from range(n), not indegree values
  - dis[c] = when course c can start; add time[c] at pop to get its finish time
  - a course starts after ALL its prerequisites finish -> max over every parent
  - update dis on every edge; push only when indegree hits 0
  - answer = the latest finish time, max(dis)
Complexity: O(V + E) time, O(V + E) space
Mistake I made:
  - 1st try (10-01): seeded the queue with indegree counts instead of indices
  - review (10-07): put the max update inside `if indegree == 0`,
    so only the LAST parent's finish time counted, not the slowest one
"""

from collections import defaultdict, deque


class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        graph = defaultdict(list)
        in_degree = [0] * n

        for pre, nxt in relations:
            pre -= 1
            nxt -= 1
            graph[pre].append(nxt)
            in_degree[nxt] += 1

        dis = [0] * n
        queue = deque([course for course in range(n) if in_degree[course] == 0])

        while queue:
            course = queue.popleft()
            dis[course] += time[course]

            for nei in graph[course]:
                dis[nei] = max(dis[nei], dis[course])
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)

        return max(dis)
