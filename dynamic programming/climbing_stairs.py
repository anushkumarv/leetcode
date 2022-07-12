class SolutionBruteForce:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


sol = SolutionBruteForce()
## time complexity - O(2^n)
## space complexity - O(n)
print(sol.climbStairs(2))
print(sol.climbStairs(10))

class Solution:
    def climbStairs(self, n: int, memo=None) -> int:
        if memo == None:
            memo = dict()
        
        if n in memo:
            return memo[n]
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
            return memo[n]


sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print(sol.climbStairs(2))
print(sol.climbStairs(40))


class SolutionIterative:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        n1, n2 = 1, 2
        for i in range(2, n):
            res = n1 + n2 
            n1, n2 = n2, res 

        return res


sol = SolutionIterative()
## time complexity - O(n)
## space complexity - O(1)
print(sol.climbStairs(2))
print(sol.climbStairs(40))