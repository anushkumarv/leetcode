from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        starts = list()
        for item in ns:
            if item - 1 in ns:
                continue

            starts.append(item)

        ml = 0
        for item in starts:
            count = 0
            while item in ns:
                count += 1
                item += 1
            ml = max(count, ml)

        return ml


sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))