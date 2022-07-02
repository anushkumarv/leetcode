# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root


def print_tree(node):
    l = list()
    traverse(node, l)
    print(l)

def traverse(node, l):

    if not node:
        return  
    
    l.append(node.val)
    if node.left:
        l.append(node.left.val)
    if node.right:
        l.append(node.right.val)
        
    traverse(node.left, l)
    traverse(node.right, l)
    
    
sol = Solution()
## time complexity - O(n) where n is the number of nodes in the tree
## space complexity - O(h) where h is the height of the tree
tree = TreeNode(4, TreeNode(2,TreeNode(1), TreeNode(3)), TreeNode(7,TreeNode(6), TreeNode(9)))
print("## Before Inverting ##")
print_tree(tree)
print("## After Inverting ##")
print_tree(sol.invertTree(tree))
