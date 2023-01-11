import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = list()
        heapq.heapify(l)
        for n in nums:
            if len(l) < k:
                heapq.heappush(l, n)
            else:
                heapq.heappushpop(l, n)

        return l[0]


sol = Solution()
## time complexity - O(nlogn)
## space complexity - O(n)
print(sol.findKthLargest(nums = [3,2,1,5,6,4], k = 2))


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        k = len(nums) - k
        
        def quickselect(l,r):
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickselect(l, p-1)
            elif p < k:
                return quickselect(p+1, r)
            else:
                return nums[p]

        return quickselect(0, len(nums) - 1)


sol = Solution()
## time complexity - O(n) average case
## space complexity - O(n)
print(sol.findKthLargest(nums = [3,2,1,5,6,4], k = 2))