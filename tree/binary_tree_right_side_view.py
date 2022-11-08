import collections
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        
        q = collections.deque()
        
        if root:
            q.append(root)
            
        while q:
            level = []
            
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
            
        ret_val = [item[-1] for item in res]
        
        return ret_val


sol = Solution()
## time complexity - O(n) where n = nodes in tree
## space complexity - O(n) where n = nodes in tree
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(sol.rightSideView(root))