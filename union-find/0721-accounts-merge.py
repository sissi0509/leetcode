"""
721. Accounts Merge  (Medium)
https://leetcode.com/problems/accounts-merge/

Pattern:    union-find on account indices, a dict links accounts that share an email
Key idea:
  - map each email to the account indices that contain it (emails start at index 1;
    index 0 is the name, and two different people can share a name)
  - union every account in an email's list with the first one
  - group: for each account i, add all its emails to groups[find(i)] (a set; find, not parent[i])
  - output: name of the root account + sorted emails
Complexity: O(E log E) time for sorting (E = total emails); unions/finds are near O(1)
            amortized (α(n)); O(E + n) space
Simpler: store only the FIRST owner of each email and union while reading (one loop, plain dict)
        -> see SolutionSimple
Mistake I made (v1):
  - looped over the whole account, so the NAME was a key -> both Johns merged
  - union(0, i) used positions in the list, not the account indices nodes[0], nodes[i]
  - read rank from x, y instead of the roots
  - set.extend (sets use update), `acounts` typo, never appended/sorted/returned the result
"""

from collections import defaultdict


class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty:
            return
        rankx, ranky = self.rank[rootx], self.rank[rooty]
        if ranky < rankx:
            self.parents[rooty] = rootx
        else:
            self.parents[rootx] = rooty
            if ranky == rankx:
                self.rank[rooty] += 1


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        dsu = DSU(n)

        mail_map = defaultdict(list)
        for i, account in enumerate(accounts):
            for mail in account[1:]:
                mail_map[mail].append(i)

        for nodes in mail_map.values():
            for i in range(1, len(nodes)):
                dsu.union(nodes[0], nodes[i])

        groups = defaultdict(set)
        for i in range(n):
            groups[dsu.find(i)].update(accounts[i][1:])

        result = []
        for root, mails in groups.items():
            result.append([accounts[root][0]] + sorted(mails))

        return result


class SolutionSimple:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        dsu = DSU(n)

        owner = {}                              # email -> first account index that had it
        for i, account in enumerate(accounts):
            for mail in account[1:]:
                if mail in owner:
                    dsu.union(i, owner[mail])
                else:
                    owner[mail] = i

        groups = defaultdict(set)
        for i in range(n):
            groups[dsu.find(i)].update(accounts[i][1:])

        return [[accounts[root][0]] + sorted(mails) for root, mails in groups.items()]
