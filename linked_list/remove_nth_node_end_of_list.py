from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next

        n = l - n + 1
        
        if n == 1:
            return head.next

        cur = head
        prev = None
        while n > 1:
            prev = cur
            cur = cur.next
            n -= 1

        prev.next = cur.next
        
        return head


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.val,end="->")
        temp = temp.next
    print()


sol = Solution()
## time complexity - O(n)
## space complexity - O(1)
print_linked_list(sol.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2))