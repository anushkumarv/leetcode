from typing import List
import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        l = [(sqrt((p[0])**2 + (p[1])**2), p) for p in points]
        heapq.heapify(l)
        res = list()
        while k:
            res.append(heapq.heappop(l)[1])
            k -= 1
        
        return res


sol = Solution()
## time complexity - O(n) for heapify and O(klogn) for popping
## space complexity - O(n) 
print(sol.kClosest(points = [[1,3],[-2,2]], k = 1))