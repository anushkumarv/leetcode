from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        order = list()
        graph = defaultdict(lambda: list())
        indegree = defaultdict(lambda: 0)
        for req in prerequisites:
            graph[req[1]].append(req[0])
            indegree[req[0]] += 1

        visited = set()
        start = [i for i in range(numCourses) if not indegree[i]]

        while start:
            node = start.pop()
            if node in visited:
                continue
            visited.add(node)
            order.append(node)
            for nghr in graph[node]:
                indegree[nghr] -= 1
                if not indegree[nghr]:
                    start.append(nghr)

        return order if len(visited) == numCourses else []



sol = Solution()
## time complexity - O(V + E)
## space complexity - O(V + E)
print(sol.findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))