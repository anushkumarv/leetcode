from typing import  Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_bst(root: Optional[TreeNode], left_ref, right_ref) -> bool:
            if not root:
                return True
            
            if not(left_ref < root.val < right_ref):
                return False
            
            return is_valid_bst(root.left, left_ref, root.val) and is_valid_bst(root.right, root.val, right_ref)
        
        return is_valid_bst(root, -math.inf, math.inf)


sol = Solution()
## time complexity - O(n) where n = nodes in tree
## space complexity - O(d) where d = depth of the tree
root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
print(sol.isValidBST(root))