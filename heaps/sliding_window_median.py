from collections import defaultdict
from heapq import heappush, heappop, heappushpop
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = []
        large = []
        for i in range(k):
            heappush(small, -nums[i])
            heappush(large, -heappop(small))
            if len(large) > len(small) + 1:
                heappush(small, -heappop(large))

        res = []
        if k & 1:
            res.append(large[0])
        else:
            res.append((-small[0] + large[0]) / 2)

        deleted_num_dict = defaultdict(lambda:0)
        l_small, l_large = len(small), len(large)
        for i in range(k, len(nums)):
            # remove element
            deleted_num = nums[i-k]
            deleted_num_dict[deleted_num] += 1
            if small and deleted_num <= -small[0]:
                l_small -= 1
            elif large and deleted_num >= large[0]:
                l_large -= 1

            # add element 
            heappush(large, -heappushpop(small, -nums[i]))
            l_large += 1

            # balance 
            while l_large > l_small + 1:
                heappush(small, -heappop(large))
                l_large -= 1
                l_small += 1

            # pop elements
            while small and deleted_num_dict[-small[0]] > 0:
                deleted_num_dict[-small[0]] -= 1
                heappop(small)     

            while large and deleted_num_dict[large[0]] > 0:
                deleted_num_dict[large[0]] -= 1
                heappop(large)

            # median
            if k & 1:
                res.append(large[0])
            else:
                res.append((-small[0] + large[0]) / 2)
            
        return res