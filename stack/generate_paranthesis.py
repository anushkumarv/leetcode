from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = list()
        def rec(oc, max_oc, s):
            if len(s) > 2*n:
                return
            if len(s) == 2*n and oc == 0:
                res.append(s)
                return
            if oc > 0:
                rec(oc - 1, max_oc, s + ')')
                if oc + 1 <= max_oc:
                    rec(oc + 1, max_oc, s + '(')

            elif oc == 0 and len(s) < 2*n:
                rec(oc + 1, max_oc, s + '(')

        rec(1, n, "(")
        return res


sol = Solution()
## time complexity - O(2^n)
## space complexity - O(n)
print(sol.generateParenthesis(3))

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


sol = Solution()
## time complexity - O(2^n)
## space complexity - O(n)
print(sol.generateParenthesis(3))
