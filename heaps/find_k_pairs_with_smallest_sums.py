from collections import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        visited = set()
        options = []
        options.append((nums1[i]+nums2[j], i, j))
        visited.add((i,j))
        res = []
        while k:
            val, i, j = heapq.heappop(options)
            res.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(options, (nums1[i+1]+nums2[j],i+1,j))
                visited.add((i+1,j))
            if j + 1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(options, (nums1[i]+nums2[j+1],i,j+1))
                visited.add((i,j+1))

            k -= 1
        return res