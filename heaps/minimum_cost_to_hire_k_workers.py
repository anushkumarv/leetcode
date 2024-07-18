from heapq import heapify, heappop, heappush
from typing import List

# Inspiration from https://leetcode.com/problems/minimum-cost-to-hire-k-workers/solutions/177269/n-log-n-explanation-no-code

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        wage2quality = [(-quality[i], wage[i]/quality[i]) for i in range(len(quality))]
        wage2quality.sort(key=lambda item: item[1])

        h = []
        qs = 0
        for i in range(k):
            heappush(h, wage2quality[i])
            qs += wage2quality[i][0] * -1
        res = wage2quality[k-1][1] * qs
        for i in range(k, len(wage2quality)):
            q , _ = heappop(h)
            qs -= -q
            heappush(h, wage2quality[i])
            qs += wage2quality[i][0] * -1
            res = min(res, wage2quality[i][1] * qs)

        return res