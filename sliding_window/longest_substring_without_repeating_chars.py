class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        l, r = 0, 0
        res = 0 
        n = len(s)
        while l < n and r < n:
            if s[r] in d:
                n_l = d[s[r]] + 1
                while l < n_l:
                    d.pop(s[l])
                    l += 1

            d[s[r]] = r
            res = max(res, r - l + 1)
            r += 1

        return res
        

sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print(sol.lengthOfLongestSubstring("abba"))