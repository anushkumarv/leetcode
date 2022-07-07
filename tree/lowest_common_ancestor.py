from typing import Optional
from common import TreeNode

class ElegantSolution:
## time complexity - O(log n) where n is the number of nodes in the tree
## space complexity - O(1)
    def lowestCommonAncestor(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root


class MySolution:
## time complexity - O(log n) where n is the number of nodes in the tree 
## space complexity - O(h) where h is the height of the tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root, node, node_anc):
            node_anc.append(root)
            if root.val == node.val:
                return
            if node.val < root.val:
                dfs(root.left, node, node_anc)
            else:
                dfs(root.right, node, node_anc)
            
        p_anc= list()
        q_anc = list()
        
        dfs(root, p, p_anc)
        dfs(root, q, q_anc)
        
        lca = root
        for i in range(min(len(p_anc), len(q_anc))):
            if p_anc[i] == q_anc[i]:
                lca = p_anc[i]
                
        return lca