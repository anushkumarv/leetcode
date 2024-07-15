from heapq import heappush, heappop
from typing import List

# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        times = []
        for emp in schedule:
            for interval in emp:
                heappush(times, (interval.start, interval.end))

        res = []
        _, e = heappop(times)
        while times:
            s1, e1 = heappop(times)
            if s1 > e:
                res.append(Interval(e, s1))
            e = max(e, e1)
                
        return res