from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        
        is_visited = set()
        max_area = 0
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in is_visited and grid[r][c] == 1:
                    area = self.bfs(r, c, grid, is_visited)
                    max_area  = max(max_area, area)
                    
        return max_area
    
    def bfs(self, r, c, grid, is_visited):
        q = deque()
        
        q.append((r,c))
        is_visited.add((r,c))
        count = 1
        
        while q:
            
            qr, qc = q.popleft()
            
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            
            for rc, cc in directions:
                nr = rc + qr
                nc = cc + qc
                
                if nr in range(len(grid)) and nc in range(len(grid[0])) and grid[nr][nc] == 1 and (nr,nc) not in is_visited:
                    q.append((nr,nc))
                    is_visited.add((nr,nc))
                    count += 1
                    
        return count


sol = Solution()
## time complexity - O(N^2)
## space complexity - O(N^2) as is_visited set can store upto N^2 elements 
print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))