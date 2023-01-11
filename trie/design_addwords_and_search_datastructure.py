class Node:
    def __init__(self, ch, end = False):
        self.ch = ch
        self.end = end
        self.children = dict()

class WordDictionary:

    def __init__(self):
        self.root = Node("")

    def addWord(self, word: str) -> None:
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

        def dfs(node, word, start):

            for i in range(start, len(word)):
                if word[i] == '.':
                    flg = False
                    for ch in node.children:
                        flg = dfs(node.children[ch], word, i+1)
                        if flg:
                            break
                    return flg
                    
                elif word[i] in node.children:
                    node = node.children[word[i]]
                else:
                    return False

            return True if node.end else False

        node = self.root
        return dfs(node, word, 0)