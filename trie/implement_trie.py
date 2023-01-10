class Node:
    def __init__(self, ch, end = False):
        self.ch = ch
        self.end = end
        self.children = dict()

class Trie:

    def __init__(self):
        self.root = Node("") 

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                new_node = Node(ch)
                node.children[ch] = new_node
                node = new_node

        node.end = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False

        return True if node.end else False
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch in node.children:
                node = node.children[ch]
            else:
                return False

        return True
        