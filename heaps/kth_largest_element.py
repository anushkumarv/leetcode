import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
            

sol = KthLargest(3, [4, 5, 8, 2])
## time complexity - O(nlogn) for inserting, poping is in O(log n)
## space complexity - O(k)
print(sol.add(3))   # return 4
print(sol.add(5))   # return 5
print(sol.add(10))  # return 5
print(sol.add(9))   # return 8
print(sol.add(4))   # return 8