from typing import Optional
from common import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root and not subRoot:
            return True
        
        if not root:
            return False
        
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)
        
        is_sub_tree = l or r or self.isSameTree(root, subRoot)
        
        return is_sub_tree
        
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif not p and not q:
            return True
        else:
            return False


sol = Solution()
## time complexity - O(n*m) where n = nodes in root, m = nodes in subroot
## space complexity - O(h1 + h2) where h1 = height of root, h2 = height of subroot 
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
print(sol.isSubtree(root, subRoot))