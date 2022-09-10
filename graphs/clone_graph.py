# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        visited = set()
        nd = dict()
        s = list()
        fn = node.val
        
        s.append(node)
        
        while(s):
            n = s.pop()
            if n not in visited:
                if n.val not in nd:
                    nd[n.val] = Node(n.val)
                visited.add(n)
                for nghr in n.neighbors:
                    if nghr.val not in nd:
                        nd[nghr.val] = Node(nghr.val)
                    nd[n.val].neighbors.append(nd[nghr.val]) 
                    s.append(nghr)
                
        return nd[fn]


## time complexity - O(V + E) This is depth first search
## space complexity - O(V) using Stack and Visited for number of vertices


class SolutionAlternate:
    def cloneGraph(self, node: "Node") -> "Node":
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None