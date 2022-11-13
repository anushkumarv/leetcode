class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        
        for i in range(n):
            l,r = i,i
            
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
                
            l,r = i, i+1
            
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
                
        return count


sol = Solution()
## time complexity - O(N^2) Number of nodes in the tree
## space complexity - O(1) 
print(sol.countSubstrings("aaa"))