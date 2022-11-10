from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        bst_sorted = list()
        
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            
            dfs(root.left)
            bst_sorted.append(root.val)
            dfs(root.right)
            
        dfs(root)
        return bst_sorted[k-1]


sol = Solution()
## time complexity - O(N) Number of nodes in the tree
## space complexity - O(N) Number of nodes in the tree
print(sol.kthSmallest(TreeNode(1, None, TreeNode(2)), 2))