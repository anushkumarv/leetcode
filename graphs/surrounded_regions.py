from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        visited  = set()
        capture = set()
        
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and board[r][c] == "O":
                    self.bfs(r, c, visited, capture, rows, cols, board)
                    
        for r, c in capture:
            board[r][c] = "X"
            
    
    def bfs(self, r, c, visited, capture, rows, cols, board):
        r_t, r_b = 0, rows - 1
        c_l, c_r = 0, cols - 1
        
        
        q = deque()
        temp = list()
        q.append((r,c))
        temp.append((r,c))
        visited.add((r,c))
        shld_capture = True
        if r == r_t or r == r_b or c == c_l or c == c_r:
            shld_capture = False
        
        while q:
            
            r, c = q.popleft()
            
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            
            for m_r, m_c in directions:
                n_r = r + m_r
                n_c = c + m_c
                
                if n_r in range(rows) and n_c in range(cols) and (n_r,n_c) not in visited and board[n_r][n_c] == "O":
                    q.append((n_r,n_c))
                    visited.add((n_r,n_c))
                    temp.append((n_r,n_c))
                              
                    if n_r == r_t or n_r == r_b or n_c == c_l or n_c == c_r:
                        shld_capture = False
                        print(shld_capture)
                        
                        
        if shld_capture:
            for cap_r, cap_c in temp:
                capture.add((cap_r, cap_c))
                
                
sol = Solution()
## time complexity - O(N^2)
## space complexity - O(N^2)
board =  [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol.solve(board)
print(board)
                
                    
        
        
        
        
        
        