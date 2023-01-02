class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def count_chars(s):
            c = [0] * 26
            for ch in s:
                c[ord(ch) - 97] += 1
            return c

        def compare(s1_c, s2_c):
            flg = True
            for i in range(len(s1_c)):
                if s1_c[i] != s2_c[i]:
                    flg = False
                    break
            return flg

        s1_c = count_chars(s1)
        l, r = 0, len(s1) - 1
        w = r - l + 1
        n1, n2 = len(s1), len(s2)
        s2_w_c = count_chars(s2[:r+1])

        while l < n2 and r < n2:
            if compare(s1_c, s2_w_c):
                return True
            s2_w_c[ord(s2[l]) - 97] -= 1
            l += 1
            if r + 1 < n2:
                r += 1
                s2_w_c[ord(s2[r]) - 97] += 1

        return False


sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print(sol.checkInclusion('ab', 'eidbaooo'))