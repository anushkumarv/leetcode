from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_cap = [(capital[i], profits[i]) for i in range(len(profits))]
        max_p = []
        heapify(min_cap)
        while k:
            while min_cap and min_cap[0][0] <= w:
                c, p = heappop(min_cap)
                heappush(max_p, -p)
            
            if max_p:
                p = -heappop(max_p)
                w += p

            k -= 1
        return w

        
