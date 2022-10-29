from typing import List
from collections import defaultdict


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        m = defaultdict(lambda: 0)
        
        for i in range(len(arr)):
            arr[i] = arr[i] % k
            m[arr[i]] += 1
            
        res = True

        for key in m:
            inv = k - key if key != 0 else 0
            if inv!=key and m[inv] != m[key]:
                res = False
                break
            elif inv == key and m[key]%2 != 0:
                res = False
                break
                
                
        return res


sol = Solution()
## time complexity - O(N)
## space complexity - O(N)
print(sol.canArrange([1,2,3,4,5,10,6,7,8,9], 5))
print(sol.canArrange([1,2,3,4,5,6], 10))