from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = list()
        subset = list()
        s = set()

        def recursion(i):

            if i > len(nums) - 1:
                if tuple(subset) not in s:
                    res.append(subset[:])
                    s.add(tuple(subset))
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
print(sol.subsetsWithDup([1,2,2]))


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res


sol = Solution()
## time complexity - O(2^n)
## space complexity - O(n)
print(sol.subsetsWithDup([1,2,2]))