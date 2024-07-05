from typing import List

class UnionFind:
    def __init__(self,n):
        self.par = {}
        self.rank = {}
        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1

    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        else:
            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
            elif self.rank[p2] > self.rank[p1]:
                self.par[p1] = p2
            else:
                self.par[p2] = p1
                self.rank[p1] += 1
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda item: item[0])
        uf = UnionFind(n)
        group_count = n
        for time, n1, n2 in logs:
            if uf.union(n1,n2):
                group_count -= 1
            
            if group_count == 1:
                return time

        return -1