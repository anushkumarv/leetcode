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
            if num in nums_dict:
                nums_dict[num].append(i)
            else:
                nums_dict[num] = [i]

        for i, num in enumerate(nums):
            req_num  = target - num
            if req_num in nums_dict and req_num != num:
                return [i, nums_dict[req_num][0]]
            elif req_num in nums_dict and req_num == num:
                if len(nums_dict[num]) > 1:
                    return [nums_dict[num][0], nums_dict[num][-1]]
            else:
                continue 

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