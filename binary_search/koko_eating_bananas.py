from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat_time(k):
            return sum([ceil(piles[i]/k) for i in range(len(piles))])

        l = ceil(sum(piles) / h)
        r = max(piles)
        res = r
        while l<=r:
            mid = (l+r) // 2
            et = eat_time(mid)
            if et > h:
                l = mid + 1
            elif et <= h:
                res = mid
                r = mid - 1

        return res


sol = Solution()
## time complexity - O(n log n)
## space complexity - O(1)
print(sol.minEatingSpeed(piles = [3,6,7,11], h = 8))