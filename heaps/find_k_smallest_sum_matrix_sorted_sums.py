from heapq import heappush, heappop
from typing import List

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        rows, cols = len(mat), len(mat[0])
        indices = [0] * rows
        s = sum((mat[i][0] for i,idx in enumerate(indices)))
        visited = {tuple(indices):s}
        res = s
        options = [(s, indices)]
        while k:
            res, indices = heappop(options)
            for i, idx in enumerate(indices):
                new_indices = indices[:i] + [idx+1] + indices[i+1:]
                if idx+1 < cols and tuple(new_indices) not in visited:
                    temp = res
                    temp -= mat[i][idx]
                    temp += mat[i][idx+1]
                    heappush(options, (temp, new_indices))
                    visited[tuple(new_indices)] = temp
            k -= 1
        return res