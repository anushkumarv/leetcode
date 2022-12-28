from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] * (amount + 1)

        for i in range(1, len(dp)):
            temp = list()
            for j in range(len(coins)):
                if i - coins[j] in range(len(dp)) and dp[i - coins[j]] != -1:
                    temp.append(dp[i - coins[j]] + 1)

            dp[i] = min(temp) if temp else -1

        return dp[-1]


sol = Solution()
## time complexity - O(n^2)
## space complexity - O(n)
print(sol.coinChange([1,2,5], 11))
