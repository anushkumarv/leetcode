import collections

## Brute Force ##
class SolutionBruteForce:
    def topKFrequent(self, nums, k):
        
        counts = collections.defaultdict(lambda : 0)
        
        for num in nums:
            counts[num] += 1
            
        n = counts.items()
        n = sorted(n, key=lambda x: x[1], reverse=True)

        return [i[0] for i in n[:k]]


## Burte Force ##
sol_bf = SolutionBruteForce()
# Time complexity - O(nlogn)
# Space complexity - O(n)
print("## Brute Force ##")
print(sol_bf.topKFrequent([1,1,1,2,2,3],2))
print(sol_bf.topKFrequent([1],1))


## Using Heaps ##
import heapq
class SolutionHeapq:
    def topKFrequent(self, nums, k):
        counts = collections.defaultdict(lambda : 0)

        for num in nums:
            counts[num] += 1

        k_largest = heapq.nlargest(k, counts.items(), key=lambda x : x[1])
        return [item[0] for item in k_largest]


## Using Heaps ##
sol_hq = SolutionHeapq()
# Time complexity - O(klogn) when k is less than n 
# Space complexity - O(n)
print("## Using Heaps ##")
print(sol_hq.topKFrequent([1,1,1,2,2,3],2))
print(sol_hq.topKFrequent([1],1))


## Using Bucket Sort ##
import heapq
class SolutionBucketSort:
    def topKFrequent(self, nums, k):

        counts = collections.defaultdict(lambda : 0)
        for num in nums:
            counts[num] += 1

        counts_arr = [[] for i in range(len(nums)+1)]
        for key in counts:
            counts_arr[counts[key]].append(key)

        k_largest = list()
        items_added = 0
        for item in reversed(counts_arr):
            if len(item) > 0:
                k_largest.extend(item)

            if len(k_largest) == k:
                break

        return k_largest

    def topKFrequentAlternate(self, nums, k):

        counts = collections.defaultdict(lambda : 0)
        for num in nums:
            counts[num] += 1

        counts_arr = [[] for i in range(len(nums)+1)]
        for key in counts:
            counts_arr[len(nums) - counts[key] + 1].append(key)

        k_largest = list()
        items_added = 0
        for item in counts_arr:
            if len(item) > 0:
                k_largest.extend(item)

            if len(k_largest) == k:
                break

        return k_largest
        

        
    


## Bucket Sort ##
sol_k = SolutionBucketSort()
# Time complexity - O(n)
# Space complexity - O(n)
print("## Bucket Sort ##")
print(sol_k.topKFrequent([1,1,1,2,2,3],2))
print(sol_k.topKFrequent([1],1))
print(sol_k.topKFrequentAlternate([1,1,1,2,2,3],2))
print(sol_k.topKFrequentAlternate([1],1))