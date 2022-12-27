from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def bfs(gr, gc, rooms, visited, ipq, count):
            opq = deque()
            while ipq:
                r, c = ipq.popleft()
                d = [[1,0],[-1,0],[0,1],[0,-1]]
                for x, y in d:
                    rc = r + x
                    cc = c + y
                    if rc in range(gr) and cc in range(gc) and rooms[rc][cc] == 2147483647 and (rc,cc) not in visited:
                        rooms[rc][cc] = count
                        visited.add((rc,cc))
                        opq.append((rc,cc))

            return opq

        gr, gc = len(rooms), len(rooms[0])
        visited = set()
        ipq = deque()
        for r in range(gr):
            for c in range(gc):
                if rooms[r][c] == 0:
                    ipq.append((r,c))

        count = 1
        while ipq:
            ipq = bfs(gr,gc,rooms,visited,ipq,count)
            count += 1

sol = Solution()
## time complexity - O(N^2)
## space complexity - O(N^2)
rooms =  [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
sol.wallsAndGates(rooms)
print(rooms)