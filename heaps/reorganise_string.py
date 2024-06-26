from collections import Counter, heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        f = Counter(s)
        fc = [(-f,c) for c, f in f.items()]
        heapq.heapify(fc)
        prev = None
        res = []
        while fc:            
            freq, ch = heapq.heappop(fc)
            if prev and prev[0] != 0:
                heapq.heappush(fc,(prev[0], prev[1]))
            if res and res[-1] == ch:
                return ""
            res.append(ch)
            prev = (freq+1,ch)

        if prev and prev[0] == 0:
            prev = None
        if prev and (prev[1] == res[-1] or -prev[0] > 1):
            return ""

        return "".join(res)