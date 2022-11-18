from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1
        
        while l < r:
            s = numbers[l] + numbers[r] 
            if s == target:
                return [l+1, r+1]
            
            elif s > target:
                r -= 1
            
            elif s < target:
                l += 1
                
        return [l,r]


sol = Solution()
## time complexity - O(N)
## space complexity - O(1) 
print(sol.twoSum([2,7,11,15], 9))