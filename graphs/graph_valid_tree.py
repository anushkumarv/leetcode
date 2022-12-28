from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            p = parent[n]

            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return False

        all_parents = [find(i) for i in range(n)]

        return len(set(all_parents)) == 1 


sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print(sol.validTree(4, [[0,1],[2,3]]))