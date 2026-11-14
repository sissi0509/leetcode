"""
362. Design Hit Counter  (Medium, Premium)
https://leetcode.com/problems/design-hit-counter/

Pattern:    sliding time window design; clue = "hits in the past 5 minutes" + timestamps in chronological order
Key idea:
  - store a COUNT per second, not every hit -> a huge number of hits per second costs nothing extra
  - window for time t = (t - 300, t]; a hit at t - 300 is already out
  - HitCounterQueue: deque of (timestamp, count) + running total;
    evict from the front in BOTH hit and getHits (a query can come after a long gap)
  - HitCounterBuckets: 300 reused slots, slot = t % 300, remember which second each slot holds
Complexity:
  - v1 (mine): hit O(1), getHits O(300), memory grows forever (old seconds never deleted)
  - Queue: getHits O(1) amortized, memory <= 300 entries
  - Buckets: getHits O(300), memory exactly 300
Mistake I made:
  - none in logic; v1 passed
  - reading a missing key from a defaultdict INSERTS it -> every getHits added up to 300 keys; use .get(k, 0)
  - said "effective" for "efficient"
"""

from collections import defaultdict, deque


class HitCounter:
    # v1 (mine): count per second; correct, but memory never shrinks
    def __init__(self):
        self.cnt = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.cnt[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        res = 0
        for i in range(300):
            res += self.cnt.get(timestamp - i, 0)
        return res


class HitCounterQueue:
    def __init__(self):
        self.q = deque()      # (timestamp, count), oldest at the front
        self.total = 0

    def _evict(self, timestamp):
        while self.q and self.q[0][0] <= timestamp - 300:
            _, c = self.q.popleft()
            self.total -= c

    def hit(self, timestamp: int) -> None:
        self._evict(timestamp)
        if self.q and self.q[-1][0] == timestamp:
            self.q[-1] = (timestamp, self.q[-1][1] + 1)
        else:
            self.q.append((timestamp, 1))
        self.total += 1

    def getHits(self, timestamp: int) -> int:
        self._evict(timestamp)
        return self.total


class HitCounterBuckets:
    def __init__(self):
        self.times = [0] * 300    # which second each slot currently holds
        self.counts = [0] * 300

    def hit(self, timestamp: int) -> None:
        i = timestamp % 300
        if self.times[i] != timestamp:     # stale slot from 300+ seconds ago
            self.times[i] = timestamp
            self.counts[i] = 0
        self.counts[i] += 1

    def getHits(self, timestamp: int) -> int:
        return sum(c for t, c in zip(self.times, self.counts) if timestamp - t < 300)
