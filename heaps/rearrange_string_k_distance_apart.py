from collections import Counter, deque, heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        f = Counter(s)
        q = deque()
        fc = [(-f, c) for c, f in f.items()]
        heapq.heapify(fc)
        res = []
        i = -1
        while fc:
            freq, ch = heapq.heappop(fc)
            res.append(ch)
            i += 1
            freq += 1
            if freq:
                q.append((freq,ch,i))
            if q and i - q[0][2] >= k -1:
                freq, ch, _ = q.popleft()
                heapq.heappush(fc, (freq,ch))
        
        return ''.join(res) if not q else ""