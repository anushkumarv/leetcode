from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = list()
        subset = list()

        def recursion(s, start, target):
            if s == target:
                res.append(subset[:])
                return

            i = start

            while i < len(candidates):
                num = candidates[i]
                if s + num <= target:
                    s += num
                    subset.append(num)
                    recursion(s, i+1, target)
                    while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                        i += 1
                    s -= num
                    subset.pop()
                i += 1

        recursion(0, 0, target)
        return res


sol = Solution()
## time complexity - O(n^n)
## space complexity - O(n)
print(sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))