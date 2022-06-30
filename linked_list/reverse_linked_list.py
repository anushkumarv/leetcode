# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if head is None:
            return head
        
        cur = head
        nxt = head.next
        cur.next = None
        
        while(nxt is not None):
            temp = nxt
            nxt = nxt.next
            temp.next = cur
            cur = temp
            
        return cur


def print_linked_list(head):
    temp = head
    while(temp is not None):
        print(temp.val)
        temp = temp.next

def init_linked_list():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    return head


sol = Solution()
print("Input")
head = init_linked_list()
print_linked_list(head)
print("Output")
head = sol.reverseList(head)
print_linked_list(head)