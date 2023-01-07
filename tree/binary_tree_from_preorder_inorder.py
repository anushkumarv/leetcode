from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def recursion(pre, ino, pl, il, ir):
            if pl == len(pre):
                return None, pl
            
            if il > ir:
                return None, pl

            t = TreeNode(pre[pl])
            pl += 1
            idx = il
            for i in range(il, ir+1):
                if ino[i] == pre[pl-1]:
                    idx = i
                    break

            t.left, pl = recursion(pre, ino, pl, il, idx - 1)
            t.right, pl = recursion(pre, ino, pl, idx + 1, ir)
            return t, pl

        return recursion(preorder, inorder, 0, 0, len(inorder) - 1)[0]


