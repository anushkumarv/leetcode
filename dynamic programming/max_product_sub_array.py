from typing import List

class SolutionDP:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        dp = list()
        dp.append((nums[0], nums[0]) if nums[0] else (1,1))

        for i in range(1,len(nums)):
            if nums[i] == 0:
                dp.append((1,1))
                continue

            c_max = max(nums[i], nums[i]*dp[i-1][0], nums[i]*dp[i-1][1])
            c_min = min(nums[i], nums[i]*dp[i-1][0], nums[i]*dp[i-1][1])
            dp.append((c_max, c_min))

            res = max(c_max, res)

        return res


sol = SolutionDP()
## time complexity - O(n)
## space complexity - O(n)
print(sol.maxProduct([-3,-1,-1]))


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        cur_max, cur_min = 1, 1
        
        for n in nums:
            if n == 0:
                cur_max, cur_min = 1, 1
                continue

            t1 = max(n*cur_max, n*cur_min, n)
            t2 = min(n*cur_max, n*cur_min, n)
            cur_max, cur_min = t1, t2
            res = max(cur_max, res)

        return res


sol = Solution()
## time complexity - O(n)
## space complexity - O(1)
print(sol.maxProduct([-3,-1,-1]))