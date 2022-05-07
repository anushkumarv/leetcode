## Brute Froce ##
class SolutionBruteForce:
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j]
                if s == target:
                    return [i,j]
                
        return None


## Optimised ##
class Solution:
    def twoSum(self, nums, target):
        nums_dict = {}
        for i, num in enumerate(nums):
            if target - num in nums_dict:
                return [nums_dict[target - num], i]

            else:
                nums_dict[num] = i

        return None


## Brute Force ##
sol_bf = SolutionBruteForce()
## time completxity - O(n^2)
## space complextity - O(n)
print("## Brute Force ##") 
print(sol_bf.twoSum([2,7,11,15],9))
print(sol_bf.twoSum([3,2,4],6))
print(sol_bf.twoSum([3,3], 6))


## Optimised ##
sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print("## Optimised ##")
print(sol.twoSum([2,7,11,15],9))
print(sol.twoSum([3,2,4],6))
print(sol.twoSum([3,3], 6))

# Output
# [0, 1]
# [1, 2]
# [0, 1]