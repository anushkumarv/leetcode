from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])
        
        pac, atl = set(), set()
        
        
        def dfs(r, c, prev_height, visited):
            
            if (r,c) in visited or r < 0 or r == ROWS or c < 0 or c == COLS or heights[r][c] < prev_height:
                return
            
            visited.add((r,c))
            
            dfs(r+1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)
        
        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS - 1, c, heights[ROWS - 1][c], atl)
            
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS - 1, heights[r][COLS - 1], atl)
            
        
        res = []
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
                    
        return res


sol = Solution()
## time complexity - O(2 * ROWS * COLS)
## space complexity - O(Max(ROWS, COLS)) as is_visited set can store upto N^2 elements 
print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
