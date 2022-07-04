from typing import Optional
from common import TreeNode

class MySolution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        valid = [True]
        
        def dfs(root):
            if valid[0]:
                if not root:
                    return -1
                
                h_l = dfs(root.left)
                h_r = dfs(root.right)
                
                if valid[0]:
                    valid[0] = False if abs(h_l - h_r) > 1 else True
                return max(h_l, h_r) + 1
            
            return -2
            
        dfs(root)
        return valid[0]


sol = MySolution()
## time complexity - O(n) where n is the number of nodes in the tree
## space complexity - O(h) where h is the height of the tree
tree = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)),TreeNode(5)), TreeNode(3,right=TreeNode(6,right=TreeNode(8))))
print(sol.isBalanced(tree))