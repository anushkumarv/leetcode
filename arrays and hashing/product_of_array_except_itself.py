from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pb = list()
        pa = [1] * len(nums)
        t = 1
        for n in nums:
            t *= n
            pb.append(t)

        t = 1
        for i in range(len(nums)-1, -1, -1):
            t *= nums[i]
            pa[i] = t

        res = list()

        for i in range(len(nums)):
            t = 1
            t = t * pb[i-1] if i-1 >= 0 else t
            t = t * pa[i+1] if i+1 < len(nums) else t
            res.append(t)

        return res


sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print(sol.productExceptSelf([1,2,3,4]))