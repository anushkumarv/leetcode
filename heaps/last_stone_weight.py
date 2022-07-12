import heapq
from typing import List

class SolutionBruteForce:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones.sort()
            x = stones.pop()
            y = stones.pop()
            if x - y > 0:
                stones.append(x-y)

        return stones[0] if len(stones) == 1 else 0


sol = SolutionBruteForce()
## time complexity - O(n^2logn) - ???
## space complexity - O(1)
print(sol.lastStoneWeight([2,7,4,1,8,1]))
print(sol.lastStoneWeight([1]))


class SolutionHeap:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            res = abs(x) - abs(y)
            if res > 0:
                heapq.heappush(stones, -res)
                
            
        return -stones[0] if len(stones) == 1 else 0


sol = SolutionHeap()
## time complexity - O(logn * logn)
## space complexity - O(1)
print(sol.lastStoneWeight([2,7,4,1,8,1]))
print(sol.lastStoneWeight([1]))