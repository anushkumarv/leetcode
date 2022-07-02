class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

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
    

