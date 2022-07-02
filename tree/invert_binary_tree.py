# Definition for a binary tree node.
from typing import Optional
from common import TreeNode, print_tree

        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

    
sol = Solution()
## time complexity - O(n) where n is the number of nodes in the tree
## space complexity - O(h) where h is the height of the tree
tree = TreeNode(4, TreeNode(2,TreeNode(1), TreeNode(3)), TreeNode(7,TreeNode(6), TreeNode(9)))
print("## Before Inverting ##")
print_tree(tree)
print("## After Inverting ##")
print_tree(sol.invertTree(tree))
