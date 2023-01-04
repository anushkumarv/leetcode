from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            if nums[mid] < nums[r]:
                if target > nums[mid] and target < nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1


        return -1

    
sol = Solution()
## time complexity - O(log n)
## space complexity - O(1)
print(sol.search([8,1,2,3,4,5,6,7], 6))