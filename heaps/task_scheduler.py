import heapq
from collections import deque, Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        q = deque()
        time = 0

        while max_heap or q:
            time += 1
            cnt = 0
            if q and not max_heap:
                time = q[0][1] + 1
                heapq.heappush(max_heap, q.popleft()[0])
            cnt = heapq.heappop(max_heap)
            if cnt + 1 < 0:
                q.append((cnt+1, time + n))
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])


        return time 

sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print(sol.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))