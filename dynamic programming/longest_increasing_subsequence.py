from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = 1

        for i in range(len(dp)):
            dp[i] = 1
            for j in range(i-1,-1,-1):
                dp[i] = max(dp[i], dp[j] + 1) if nums[i] > nums[j] else dp[i]

        # print(dp)
        return max(dp)


sol = Solution()
## time complexity - O(n^2)
## space complexity - O(n)
print(sol.lengthOfLIS([1,3,6,7,9,4,10,5,6]))
