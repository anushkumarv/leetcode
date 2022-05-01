### Brute Force ###
class SolutionBruteForce:
    def fourSum(self, nums, target):

        op = []
        nums.sort()
        processed_comb = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                    for l in range(k+1, len(nums)):
                        s = nums[i] + nums[j] + nums[k] + nums[l]
                        if s == target:
                            key = str(nums[i]) + str(nums[j]) + str(nums[k]) + str(nums[l])
                            if key not in processed_comb:
                                op.append([nums[i], nums[j], nums[k], nums[l]])
                                processed_comb.add(key)
        
        return op


## Two Pointer ##
class Solution:
    def fourSum(self, nums, target):

        op = []
        nums.sort()
        processed_comb = set()

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left  = j+1
                right = len(nums) - 1
                while(left < right):
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if (s > target):
                        right -= 1
                        continue
                    elif (s < target):
                        left += 1
                        continue
                    else:
                        key = str(nums[i]) + str(nums[j]) + str(nums[left]) + str(nums[right])
                        if key not in processed_comb:
                            op.append([nums[i], nums[j], nums[left], nums[right]])
                            processed_comb.add(key)
        
                        left  += 1
                        right -= 1
        return op


## Example test cases 
## Brute Force ##
sol_bf = SolutionBruteForce()
## Time complexity - O(N^4)
## Space complexity - O(N)
print("## Brute Force ##")
print(sol_bf.fourSum([1,0,-1,0,-2,2],0))
print(sol_bf.fourSum([2,2,2,2,2],8))


## Two Pointer ##
sol = Solution()
## Time complexity - O(N^3)
## Space complexity - O(N)
print("## Two Pointer ##")
print(sol.fourSum([1,0,-1,0,-2,2],0))
print(sol.fourSum([2,2,2,2,2],8))