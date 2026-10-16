"""
File Permissions at a Time  (Medium, OA-style design; based on a reported interview theme:
"does a user have access to a file at a specific time, in a hierarchical file system
with inherited and overridden permissions")

Events (time, user, path, "allow"/"deny"). get_access(user, path, t):
  - inherit: check the path, then its parent, ... up to "/"; the nearest rule for this user wins
  - override: a nearer rule beats a farther one, even if the farther one is newer
  - time: only events with time <= t count; on one path, the latest of those wins
  - nothing applies -> False

Pattern:    group + sort once, walk up the path, binary search per level (LC981 inside)
Key idea:
  - build once: (path, user) -> list of (time, action) sorted by time
  - find_action = LC981 get: first index with time > t, answer is the one before it
  - walk up with path[:path.rfind("/")]; "" means the root "/", and stop after checking it
  - "nearest wins" vs "newest parent change wins" is a design choice: ask the interviewer
Complexity: build O(E log E); query O(depth * log k), k = events per (path, user)
Mistake I made:
  - loop variables `for time, user, path, action` overwrote the query's user and path
  - returned the action string ("deny" is truthy) instead of action == "allow"
  - stepped up only inside the if (infinite loop), and skipped the root "/"
  - looked up `path` instead of `cur_path` inside the walk (a defaultdict hides it: [] not KeyError)
Follow-up: a trie of folders, walk down once and remember the last rule -> no string slicing
"""

from collections import defaultdict

class Permission:
    def __init__(self, events):
        self.path_map = defaultdict(list)
        events.sort(key=lambda x:x[0])
        for time, u, p, action in events:
            self.path_map[(p, u)].append((time, action))

    def find_action(self, user, path, time):
        lst = self.path_map[(path, user)]
        l, r = 0, len(lst)
        while l < r:
            mid = (l + r) // 2
            if lst[mid][0] <= time:
                l = mid + 1
            else:
                r = mid
        if l == 0:
            return None
        return lst[l - 1][1]

    def get_access(self, user, path, time):
        cur_path = path
        while True:
            cur_path = cur_path if cur_path else "/"
            if (cur_path, user) in self.path_map:
                action = self.find_action(user, cur_path, time)
                if action:
                    return action == "allow"
            if cur_path == "/":
                return False
            cur_path = cur_path[:cur_path.rfind('/')]
            




            
            


events = [(1, "alice", "/docs", "allow"),
          (5, "alice", "/docs/private", "deny"),
          (8, "alice", "/docs/private", "allow"),
          (3, "bob", "/", "allow")]
p = Permission(events)
print(p.get_access("alice", "/docs/private/a.txt", 6))  # False
print(p.get_access("alice", "/docs/private/a.txt", 9))  # True
print(p.get_access("alice", "/docs/private/a.txt", 4))  # True
print(p.get_access("alice", "/music/x.mp3", 10))        # False
print(p.get_access("bob", "/docs/private/a.txt", 2))    # False
print(p.get_access("bob", "/docs/private/a.txt", 3))    # True
