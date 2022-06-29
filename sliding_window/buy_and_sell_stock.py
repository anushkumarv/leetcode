## Brute Froce ##
class SolutionBruteForce:
    def maxProfit(self, prices):
        
        max_profit = 0
        for i in range(0,len(prices)):
            for j in range(i,len(prices)):
                temp_profit = prices[j] - prices[i]
                max_profit = max(max_profit, temp_profit)
                
        return max_profit
                

## Optimised ##
class SolutionOptimized:
    def maxProfit(self, prices):
        max_profit = 0

        if len(prices) < 1:
            return max_profit

        left, right  = 0, 1

        while left < len(prices) and right < len(prices):
            if left == right:
                right += 1
                continue
            print(left, right)
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
            
            if profit < 0:
                left += 1
            else:
                right += 1

        return max_profit


## Brute Force ##
sol = SolutionBruteForce()
## time completxity - O(n^2)
## space complextity - O(1)
print("## Brute Force ##") 
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))

## Optimised ##
sol = SolutionOptimized()
## time complexity - O(n)
## space complexity - O(1)
print("## Optimised ##")
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))

