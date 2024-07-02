from collections import Counter
from typing import List

# #####
# https://leetcode.com/problems/intersection-of-two-arrays-ii
# #####

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1c = Counter(nums1)
        n2c = Counter(nums2)
        res = []
        for n, count in n1c.items():
            if n in n2c:
                temp = [n] * min(count, n2c[n])
                res.extend(temp)
        return res