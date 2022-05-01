### Brute Force ###
class SolutionBruteForce:
    def threeSumClosest(self, nums, target):
        
        nums.sort()
        min_diff = float("inf")
        closest_sum = 0
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    diff = abs(target - sum)
                    if diff < min_diff:
                        min_diff= diff
                        closest_sum = sum

        return closest_sum 


### Two Pointer ###
class Solution:
    def threeSumClosest(self, nums, target):
        
        nums.sort()
        min_diff = float("inf")
        closest_sum = 0
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if min_diff == 0:
                break
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(target - sum)
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = sum
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    while( left < len(nums) - 1 and nums[left] == nums[left + 1]):
                        left += 1
                    while( right > 0 and nums[right] == nums[right - 1]):
                        right -= 1
                    left += 1
                    right -= 1
        
        return closest_sum 


# Example test cases
## Brute Force ##
sol_bf = SolutionBruteForce()
## time complexity - O(n^3)
## space complexity - O(n)
print("### Brute Force ###")
print(sol_bf.threeSumClosest([-1,2,1,-4],1))
print(sol_bf.threeSumClosest([0,0,0],1))
print(sol_bf.threeSumClosest([0,2,1,-3],1))
print(sol_bf.threeSumClosest([1,2,3,4],5))

## Two Pointer 
sol = Solution()
## time complexity - O(n^2)
## space complexity - O(n)
print("### Two Pointer ###")
print(sol.threeSumClosest([-1,2,1,-4],1))
print(sol.threeSumClosest([0,0,0],1))
print(sol.threeSumClosest([0,2,1,-3],1))
print(sol.threeSumClosest([1,2,3,4],5))

# Output
# 2
# 0
# 0
# 6