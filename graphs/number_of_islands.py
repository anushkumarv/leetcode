from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        
        is_visited = set()
        islands = 0
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in is_visited:
                    self.bfs(grid, is_visited, (r, c), rows, cols)
                    islands = islands + 1
                    
        return islands
                    
                    
                    
    def bfs(self, grid, is_visited, v, rows, cols):
        q = deque()
        q.append(v)
        while q:
            rv, cv = q.popleft()
            is_visited.add((rv,cv))
            directions = [[-1,0],[1,0],[0,-1],[0,1]]
            for dr, dc in directions:
                r = rv + dr
                c = cv + dc
                if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in is_visited:
                    q.append((r,c))
                    is_visited.add((r,c))


sol = Solution()
## time complexity - O(N^2)
## space complexity - O(N^2) as is_visited set can store upto N^2 elements 
print(sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
