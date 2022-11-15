class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [chr(ord(ch) - 32) if ord(ch) >= 65 and ord(ch) <= 90 else ch for ch in s]
        s = [ch for ch in s if ord(ch) in range(97,123) or ord(ch) in range(48,58)]
        l, r = 0, len(s) - 1
        while l<=r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
            
        return True
        

sol = Solution()
## time complexity - O(N)
## space complexity - O(N) 
print(sol.isPalindrome("A man, a plan, a canal: Panama"))