from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = list()
        subset = list()

        def recursion(s,start,target):
            if s == target:
                res.append(subset[:])

            for i in range(start, len(candidates)):
                if candidates[i] + s <= target:
                    subset.append(candidates[i])
                    s += candidates[i]
                    recursion(s, i, target)
                    subset.pop()
                    s -= candidates[i]

        recursion(0, 0, target)
        return res


sol = Solution()
## time complexity - O(n^n)
## space complexity - O(n)
print(sol.combinationSum(candidates = [2,3,6,7], target = 7))