from tkinter.tix import Tree
from traceback import print_tb
from typing import Optional
from common import TreeNode

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif not p and not q:
            return True
        else:
            return False


sol = Solution()
## time complexity - O(n) where n is the number of nodes in the tree
## space complexity - O(h) where h is the height of the tree
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
print(sol.isSameTree(p,q))
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(3), TreeNode(2))
print(sol.isSameTree(p, q))