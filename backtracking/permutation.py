from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = list()
        subset = list()
        s = set()

        def recursion():
            if len(subset) == len(nums):
                res.append(subset[:])
                return

            for num in nums:
                if num not in s:
                    subset.append(num)
                    s.add(num)
                    recursion()
                    subset.pop()
                    s.remove(num)

        recursion()
        return res


sol = Solution()
## time complexity - O(n*n!)
## space complexity - O(n)
print(sol.permute([1,2,3]))