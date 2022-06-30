class Solution:
    def search(self, nums, target):
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        left, right = 0, len(nums) - 1
        
        while(left<=right):
            center = (left+right) // 2
            
            if nums[center] == target:
                return center
            
            elif nums[center] > target:
                right = center - 1
                
            else:
                left = center + 1
                
                
        return -1


sol = Solution()
## time complexity O(log n)
## space complexity - O(1)
print(sol.search([-1,0,3,5,9,12], 9))
print(sol.search([-1,0,3,5,9,12], 2))