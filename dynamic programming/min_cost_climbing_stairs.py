from typing import List

class SolutionBruteForce:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.minCost(cost, 0)
        
    
    def minCost(self, cost: List[int], i: int) -> int:
        if i >= len(cost) - 1:
            return 0
        else:
            one_step = cost[i] + self.minCost(cost, i+1)
            two_step = cost[i+1] + self.minCost(cost, i+2)
            return min(one_step, two_step)
        

sol = SolutionBruteForce()
## time complexity - O(n^2) where n is length of cost array 
## space complexity - O(n) where n is length of cost array
print("## Brute Force ##")
print(sol.minCostClimbingStairs([10,15,20]))
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))


class SolutionMemo:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.minCost(cost, 0)
        
    
    def minCost(self, cost: List[int], i: int, memo=None) -> int:
        if memo == None:
            memo = dict()
            
        if i in memo:
            return memo[i]
        elif i >= len(cost) - 1:
            return 0
        else:
            one_step = cost[i] + self.minCost(cost, i+1, memo)
            two_step = cost[i+1] + self.minCost(cost, i+2, memo)
            memo[i] = min(one_step, two_step)
            return memo[i]


sol = SolutionMemo()
## time complexity - O(n^2) where n is length of cost array 
## space complexity - O(n) where n is length of cost array
print("## Memoisation ##")
print(sol.minCostClimbingStairs([10,15,20]))
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))


class SolutionIterative:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
            
        return min(cost[0], cost[1])


sol = SolutionIterative()
## time complexity - O(n^2) where n is length of cost array 
## space complexity - O(1) 
print("## Iterative ##")
print(sol.minCostClimbingStairs([10,15,20]))
print(sol.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))