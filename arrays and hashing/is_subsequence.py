class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        ls, lt = 0, 0 
        flg = False
        while lt < len(t):
            if s[ls] == t[lt]:
                ls += 1
                lt += 1
            else:
                lt += 1

            if ls == len(s):
                break

        return True if ls == len(s) else False