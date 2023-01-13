from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited = set()

        def recursion(r, c, br, bc, s, word):
            # print(r,c,s,len(word))
            if s == len(word):
                return True

            dir = [[1,0],[-1,0],[0,1],[0,-1]]
            for rc, cc in dir:
                nr = r + rc
                nc = c + cc
                if nr in range(br) and nc in range(bc) and (nr,nc) not in visited and board[nr][nc] == word[s]:
                    visited.add((nr,nc))
                    flg = recursion(nr, nc, br, bc, s+1, word)
                    if flg:
                        return True
                    visited.remove((nr,nc))

            return False

        br, bc = len(board), len(board[0])
        s = 0
        flg = False
        w_set, b_set = set(), set()

        for i in range(br):
            for j in range(bc):
                b_set.add(board[i][j])

        for i in range(len(word)):
            w_set.add(word[i])

        if len(b_set) < len(w_set):
            return False

        for i in range(br):
            for j in range(bc):
                if board[i][j] == word[s]:
                    visited.add((i,j))
                    flg = recursion(i, j, br, bc, s+1, word)
                    if flg:
                        return True
                    visited.remove((i,j))

        return flg


sol = Solution()
## time complexity - O(n*m*n)
## space complexity - O(n^2)
print(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))