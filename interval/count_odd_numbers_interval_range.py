class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low = low if low % 2 != 0 else low + 1
        return ((high - low) // 2 + 1)
        

sol = Solution()
## time complexity - O(1)
## space complexity - O(1)
print(sol.countOdds(3, 7))
print(sol.countOdds(8, 10))