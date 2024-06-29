from collections import heapq, deque
from typing import List

# #####
# https://leetcode.com/problems/maximum-total-importance-of-roads
# #####

class Solution27Jun:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        nnghs = [0] * n
        for r1, r2 in roads:
            nnghs[r1] += 1
            nnghs[r2] += 1
        heapq.heapify(nnghs)
        res, val = 0, 1
        while nnghs:
            freq = heapq.heappop(nnghs)
            res += val * freq
            val += 1
        return res


# #####
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
# #####

class Node:
    def __init__(self, val):
        self.val = val
        self.ind = 0
        self.neighbours = []
        self.res = set()

    def __repr__(self):
        return f'node val: {self.val}'

class Solution28Jun:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        nodes = [Node(i) for i in range(n)]
        for src, tgt in edges:
            nodes[tgt].ind += 1
            nodes[src].neighbours.append(nodes[tgt])

        q = deque()
        for node in nodes:
            if node.ind == 0:
                q.append(node)

        
        while q:
            node = q.popleft()
            for nghr in node.neighbours:
                nghr.ind -= 1
                nghr.res.update(node.res)
                nghr.res.add(node.val)
                if nghr.ind == 0:
                    q.append(nghr)

        res = [sorted(list(nodes[i].res)) for i in range(n)]
        
        return res
        