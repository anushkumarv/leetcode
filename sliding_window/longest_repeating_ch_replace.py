from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, = 0, 0
        n = len(s)
        res = 0
        d = defaultdict(lambda : 0)
        while l < n and r < n:
            d[s[r]] += 1
            mx_f = max(d.values())
            w = r - l + 1
            if w - mx_f <= k:
                res = max(res, w)
            else:
                d[s[l]] -= 1
                l += 1
            r += 1

        return res


sol = Solution()
## time complexity - O(26n)
## space complexity - O(n)
print(sol.characterReplacement('AABABBA', 1))