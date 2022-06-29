class Solution:
    def isValid(self, s):
        pairs = self.init_pairs()
        stack = list()

        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
            else:
                if pairs.get(stack[-1], '') == ch:
                    stack.pop()
                else:
                    stack.append(ch)

        return True if len(stack) == 0 else False
        
    def init_pairs(self):
        pairs = {'(': ')',
                 '[': ']',
                 '{': '}'}

        return pairs


sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))