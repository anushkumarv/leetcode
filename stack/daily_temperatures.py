from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = list()
        ans = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                _, idx = stk.pop() 
                ans[idx] = i - idx
            stk.append((t,i))

        return ans


sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))