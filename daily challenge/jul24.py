from collections import Counter
from heapq import heappush, heappop
from typing import List, Optional

# #####
# https://leetcode.com/problems/intersection-of-two-arrays-ii
# #####

class Solution1Jul:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1c = Counter(nums1)
        n2c = Counter(nums2)
        res = []
        for n, count in n1c.items():
            if n in n2c:
                temp = [n] * min(count, n2c[n])
                res.extend(temp)
        return res
    

# #####
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves
# #####

class Solution2Jul:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        small_4 = list()
        big_4 = list()
        for _, num in enumerate(nums):
            heappush(small_4, -num)
            if len(small_4) > 4:
                heappop(small_4)

            heappush(big_4, num)
            if len(big_4) > 4:
                heappop(big_4)

        res = float("inf")
        small_4 = [-1*num for num in small_4]
        small_4.sort()
        big_4.sort()
        for i in range(4):
            res = min(res, big_4[i] - small_4[i])

        return res
    

# #####
# https://leetcode.com/problems/merge-nodes-in-between-zeros
# #####

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution3Jul:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        cur = head.next
        prev = dummy
        s = 0
        while cur:
            if cur.val == 0:
                prev.next = ListNode(s)
                prev = prev.next
                s = 0
            else:
                s += cur.val
            cur = cur.next
        return dummy.next