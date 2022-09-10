from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        sol = [0] * len(nums)
        
        
        for i in range(len(nums)):
            sol[i] = nums[i]
            for j in range(i-1):
                # print(i,j)
                # print(nums[i],nums[j])
                sol[i] = max(sol[i], nums[i] + sol[j])
                
            # print(sol)
                
        return max(sol)
        
        
sol = Solution()
## time complexity - O(N^2)
## space complexity - O(N)
print(sol.rob([1,2,3,1]))
print(sol.rob([2,1,1,2]))


class SolutionAlternate:
    def rob(self, nums: List[int]) -> int:
        sol = [0] * len(nums)
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1], nums[0])
        
        sol[0] = nums[0]
        sol[1] = max(nums[1], nums[0])
        
        for i in range(2, len(nums)):
                sol[i] = max(sol[i-2] + nums[i], sol[i-1])
                
                
        return max(sol)