from collections import heapq
from typing import List

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
