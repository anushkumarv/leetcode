from typing import List


class SolutionBruteForce:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        
        for i in range(0, len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                max_sum = max(cur_sum, max_sum)
                
        return max_sum


sol = SolutionBruteForce()
## time complexity - O(n^2)
## space complexity - O(1)
print('## Brute Force ##')
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.maxSubArray([1]))


class SolutionGreedy:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        cur_sum = 0 
        
        for i in range(0, len(nums)):
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[i]
            max_sum = max(max_sum, cur_sum)
        
        return max_sum


sol = SolutionGreedy()
## time complexity - O(n)
## space complexity - O(1)
print('## Greedy ##')
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(sol.maxSubArray([1]))