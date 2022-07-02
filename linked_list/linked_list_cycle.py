from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class SolutionHack:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        for i in range(0, 10001):
            if head is None:
                return False
            head = head.next
            
        return True


class Solution:
## time complexity - O(n)
## space complexity - O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        node_set = set()
        
        while(head is not None):
            if head in node_set:
                return True
            node_set.add(head)
            head = head.next
            
        return False


class SolutionMemoryEfficient:
## time complexity - O(n)
## space complexity - O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast, slow = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
