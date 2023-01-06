from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                break

        return slow


sol = Solution()
## time complexity - O(n)
## space complexity - O(1)
print(sol.findDuplicate([3,1,3,4,2]))