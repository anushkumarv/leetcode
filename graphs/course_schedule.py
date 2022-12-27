from typing import List
from collections import defaultdict

class SolutionRecursopm:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(crs, graph, visiting):
            if crs in visiting:
                return False
            if not graph[crs]:
                return True

            visiting.add(crs)
            for nghr in graph[crs]:
                if not dfs(nghr, graph, visiting):
                    return False
            visiting.remove(crs)
            graph[crs] = []
            return True

        graph = defaultdict(lambda: [])
        visiting = set()

        for req in prerequisites:
            src = req[1]
            tgt = req[0]
            graph[src].append(tgt)

        for crs in range(numCourses):
            if not dfs(crs, graph, visiting):
                return False

        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
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
            for nghr in graph[node]:
                indegree[nghr] -= 1
                if not indegree[nghr]:
                    start.append(nghr)

        return len(visited) == numCourses


sol = Solution()
## time complexity - O(V + E)
## space complexity - O(V + E)
print(sol.canFinish(2,[[1,0]]))