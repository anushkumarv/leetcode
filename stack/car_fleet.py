from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = [target - p for p in position]
        ds = list(zip(d,speed))
        ds.sort(key=lambda pair: pair[0])
        time = [pair[0]/pair[1] for pair in ds]
        stk = list()
        count = 0
        for t in time:
            if (stk and t <= stk[0]):
                stk.append(t)
                continue
            elif stk and t > stk[0]:
                count += 1
                stk = list()
            stk.append(t)
        
        return count if not stk else count + 1


sol = Solution()
## time complexity - O(nlogn)
## space complexity - O(n)
print(sol.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))