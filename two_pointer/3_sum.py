### Brute Force Approach ###
class SolutionBruteForce:
    def threeSum(self, nums):
        
        op = []

        sorted_nums = sorted(nums)
        for i in range(0, len(sorted_nums)):
            for j in range(i+1, len(sorted_nums)):
                for k in range(j+1, len(sorted_nums)):
                    if (sorted_nums[i] + sorted_nums[j] + sorted_nums[k] == 0):
                        temp = []
                        temp.append(sorted_nums[i])
                        temp.append(sorted_nums[j])
                        temp.append(sorted_nums[k])
                        if temp not in op:
                            op.append(temp)
                        continue
        
        return op
                
    

### Two Pointer Approach ###
class Solution:
    def threeSum(self,nums):

        op = []
        processed_triplet = set()
        sorted_nums = sorted(nums)
        for i, item in enumerate(sorted_nums):
            left = i + 1
            right = len(sorted_nums) - 1
            while (left < right):
                if (item + sorted_nums[left] + sorted_nums[right]) > 0:
                    right -= 1
                    continue
                elif (item + sorted_nums[left] + sorted_nums[right]) < 0:
                    left += 1
                    continue
                else:
                    if (str(item) + str(sorted_nums[left]) + str(sorted_nums[right]) not in processed_triplet):
                        processed_triplet.add(str(item) + str(sorted_nums[left]) + str(sorted_nums[right]))
                        op.append([item, sorted_nums[left], sorted_nums[right]])
                        while (left + 1 < len(sorted_nums) and sorted_nums[left] == sorted_nums[left + 1]):
                            left += 1
                        while (right - 1 > 0 and sorted_nums[right] == sorted_nums[right - 1]):
                            right -= 1
                        
                    left += 1
                    right -= 1

        return op


# Example test cases
## Brute Force ##
sol_bf = SolutionBruteForce()
## time complexity - O(n^3)
## space complexity - O(n)
print(sol_bf.threeSum([-1,0,1,2,-1,-4]))
print(sol_bf.threeSum([0,0,0]))

## Two Pointer 
sol = Solution()
## time complexity - O(n^2)
## space complexity - O(n)
print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([0,0,0]))

# Output 
# [[-1, -1, 2], [-1, 0, 1]]
# [[0, 0, 0]]