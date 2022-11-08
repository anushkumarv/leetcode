from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __init__(self):
    
        self.depth = 0
        self.ret_val = [[] for i in range(self.depth)]
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        def max_depth(root: Optional[TreeNode], level: int) -> None:
            if root == None:
                return
            
            self.depth = self.depth + 1 if level > self.depth else self.depth
            
            max_depth(root.left, level + 1)
            max_depth(root.right, level + 1)
            
        max_depth(root, 1)
        
        # print(self.depth)
        
        self.ret_val = [[] for i in range(self.depth)]
        
        def level_order(root: Optional[TreeNode], level: int) -> None:
            if root == None:
                return
            
            self.ret_val[level].append(root.val)
            
            level_order(root.left, level + 1)
            level_order(root.right, level + 1)
        
        
        level_order(root, 0)
        return self.ret_val


sol = Solution()
## time complexity - O(n) where n = nodes in tree
## space complexity - O(n + l) where n = nodes in tree, l = number of levels in tree
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(sol.levelOrder(root))