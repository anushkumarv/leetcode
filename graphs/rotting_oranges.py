from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        fresh, time = 0, 0
        
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0:
            
            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if (nr >= 0 and nr < rows) and (nc >= 0 and nc < cols) and (grid[nr][nc] == 1):
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1
                        
            time += 1
            
        return time if fresh == 0 else -1


sol = Solution()
## time complexity - O(N^2)
## space complexity - O(N^2)
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))