class Solution:
    def check_valid(self, sn):
        if len(sn) > 1 and sn[0] == "0":
            return False
        n = int(sn)
        return True if n>=1 and n<=26 else False
            
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
            
            
        for i in range(len(s)):
            c1 = self.check_valid(s[i])
            if c1:
                dp[i] += dp[i-1] if i-1 >=0 else 1
            c2 = self.check_valid(s[i-1:i+1]) if i-1 >= 0 else False
            if c2:
                dp[i] += dp[i-2] if i-2 >=0 else 1
                
        return dp[-1]
            


sol = Solution()
## time complexity - O(N)
## space complexity - O(N) 
print(sol.numDecodings("226"))