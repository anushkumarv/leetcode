from heapq import heappush, heappop
from typing import List


class SolutionWorksButN2Complexity:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        res = self.mergesort(matrix, 0, len(matrix)-1, k)
        return res[-1]
        
    def mergesort(self, matrix, l, r, k):
        if r - l == 1:
            res = self.merge(matrix[l],matrix[r],k)            
        elif r - l == 0:
            res = matrix[l]
        else:
            mid = (l+r) // 2
            res1 = self.mergesort(matrix, l,mid,k)
            res2 = self.mergesort(matrix, mid+1,r,k)
            res = self.merge(res1,res2,k)
        return res

    def merge(self, l1, l2, k):
        i, j = 0, 0
        options = []
        heappush(options, (l1[i], 0))
        heappush(options, (l2[j], 1))
        res = []
        while len(res) < k and (0 <= i < len(l1) or 0 <= j < len(l2)):
            val, id_ = heappop(options)
            res.append(val)
            if id_ == 0:
                i += 1                
                heappush(options, (l1[i], 0)) if i < len(l1) else None
            else:
                j += 1
                heappush(options, (l2[j], j)) if j < len(l2) else None                

        return res

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        options = []
        for r in range(len(matrix)):
            heappush(options, (matrix[r][0], r, 0))
        val = 0
        while k:
            val, r, c = heappop(options)
            if c + 1 < len(matrix[0]):
                heappush(options, (matrix[r][c+1], r, c+1))
            k -= 1
        return val
