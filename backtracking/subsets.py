from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = list()
        subset = list()

        def recursion(i):
            if i > len(nums) - 1:
                res.append(subset[:])
                return

            subset.append(nums[i])
            recursion(i+1)

            subset.pop()
            recursion(i+1)

        recursion(0)
        return res


sol = Solution()
## time complexity - O(2^n)
## space complexity - O(n)
print(sol.subsets([1,2,3]))