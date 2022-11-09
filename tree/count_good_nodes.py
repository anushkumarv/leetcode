# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def __init__(self):
        self.goodnodes = 0
    
    def goodNodes(self, root: TreeNode) -> int:
        
        self.dfs(root, -1 * 10 ** 4)
        return self.goodnodes
        
    
    def dfs(self, root: TreeNode, max_val) -> None:
        
        if not root:
            return
        
        if root.val >= max_val:
            self.goodnodes += 1
            max_val = root.val
            
        self.dfs(root.left, max_val)
        self.dfs(root.right, max_val)



sol = Solution()
## time complexity - O(n) where n = nodes in tree
## space complexity - O(d) where d = depth of the tree
root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
print(sol.goodNodes(root))