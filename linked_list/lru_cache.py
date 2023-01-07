class DNode:
    def __init__(self, k: int, x: int, next: 'DNode' = None, prev: 'DNode' = None):
        self.key = int(k)
        self.val = int(x)
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = DNode(-1,-1), DNode(-1,-1)
        self.c = capacity
        self.d = dict()
        self.left.next = self.right
        self.right.prev = self.left

    def rmv(self, key):
        n = self.d[key]
        n.prev.next = n.next
        n.next.prev = n.prev
        self.d.pop(key)
        return n

    def ins(self, key, val):
        n = DNode(key, val)
        self.d[key] = n
        n.prev = self.right.prev
        n.next = self.right
        self.right.prev.next = n
        self.right.prev = n

    def get(self, key: int) -> int:
        if key in self.d:
            n = self.rmv(key)
            self.ins(key, n.val)
            return self.d[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
            _ = self.rmv(key)
        elif len(self.d) == self.c:
            _  = self.rmv(self.left.next.key)
        self.ins(key, value)