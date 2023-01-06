from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def list_to_int(l):
            d = 1
            s = 0
            while l:
                s += l.val * d
                l = l.next
                d *= 10

            return s

        def int_to_list(n):
            if n == 0:
                return ListNode(0)
            c = n
            prev = None
            head = None
            while c > 0:
                u = c % 10            
                node = ListNode(u)
                if not head:
                    head = node
                if prev:
                    prev.next = node
                prev = node
                c = c // 10

            return head

        n1, n2 = list_to_int(l1), list_to_int(l2)
        return int_to_list(n1 + n2)


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.val,end="->")
        temp = temp.next
    print()


sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print_linked_list(sol.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))