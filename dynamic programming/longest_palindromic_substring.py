class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True
            
            
        max_len = 1
        st,en = 0, 0
        
        for start in range(len(s) -1, -1, -1):
            for end in range(len(s) - 1, start, -1):
                # print(start, " ", end)
                # print(start + 1, " ", end -1)
                if end - start > 1:
                    res = dp[start + 1][end - 1] and s[start] == s[end]
                else:
                    res = s[start] == s[end]
                dp[start][end] = res
                if dp[start][end]:
                    if max_len < end - start + 1:
                        max_len = end - start + 1
                        st = start
                        en = end
                    
            
        # print(dp)
        # print(st," ", en)
        return s[st:en+1]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                
        return res
            
            