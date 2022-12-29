from typing import List

class Solution:

    def get_box_idx(self, r, c):
        return 3 * (r // 3) + (c // 3)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nr, nc = len(board), len(board[0])
        
        r_set = [set() for i in range(9)]
        c_set = [set() for i in range(9)]
        cube_set = [set() for i in range(9)]

        for r in range(nr):
            for c in range(nc):
                elem = board[r][c]
                if elem == ".":
                    continue 
                elem = int(elem)
                    
                r_idx, c_idx, cube_idx = r, c, self.get_box_idx(r,c)
                if elem in r_set[r_idx]:
                    return False
                else:
                    r_set[r_idx].add(elem)
                if elem in c_set[c_idx]:
                    return False
                else:
                    c_set[c_idx].add(elem)
                if elem in cube_set[cube_idx]:
                    return False
                else:
                    cube_set[cube_idx].add(elem)

        return True


sol = Solution()
## time complexity - O(n^2)
## space complexity - O(n^2)
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))
