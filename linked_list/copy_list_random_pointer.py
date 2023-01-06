from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        cur = head
        d = dict()

        while cur:
            n = Node(cur.val)
            d[cur] = n
            cur = cur.next


        head1, cur = head, d[head]

        while cur:
            cur.next = d.get(head1.next, None)
            cur.random = d.get(head1.random, None)
            cur = cur.next
            head1 = head1.next

        return d[head]


## time complexity - O(n)
## space complexity - O(n)