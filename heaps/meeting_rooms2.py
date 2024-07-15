from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heapify(intervals)
        endtimes = []
        res = 0
        while intervals:
            start, end = heappop(intervals)
            if endtimes and endtimes[0] <= start:
                _ = heappop(endtimes)
            heappush(endtimes, end)
            res = max(res, len(endtimes))
        return res     