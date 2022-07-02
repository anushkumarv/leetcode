from typing import Optional
from common import print_tree, TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        max_depth = max(self.maxDepth(root.left),self.maxDepth(root.right))
        return max_depth + 1


sol = Solution()
## time complexity - O(n) where n is the max depth
## space complexity - O(n) where n represents stack lenght (which should equal the max depth of the tree)
tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(sol.maxDepth(tree))