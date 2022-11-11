from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = list()
        
        for tk in tokens:
            if tk == '+' or tk == '-' or tk == '*' or tk == '/':
                op2 = int(stk.pop())
                op1 = int(stk.pop())
                
                res = 0
                if tk == '+':
                    res = op1 + op2
                elif tk == '-':
                    res = op1 - op2
                elif tk == '*':
                    res = op1 * op2
                else:
                    res = int(op1 / op2)
                    
                stk.append(str(res))
            else:
                stk.append(str(tk))
                
        return stk[-1]


sol = Solution()
## time complexity - O(N)
## space complexity - O(N)
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))