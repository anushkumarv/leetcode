class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        l = list()
        while(list1 is not None or list2 is not None):
            if list1 is None:
                l.append(list2)
                list2 = list2.next
            elif list2 is None:
                l.append(list1)
                list1 = list1.next
            elif list1.val <= list2.val:
                l.append(list1)
                list1 = list1.next
            else:
                l.append(list2)
                list2 = list2.next
                
        if l:
            for i in range(len(l)-1):
                l[i].next = l[i+1]
            l[-1].next = None
            return l[0]
        else:
            return None
            

class SolutionInOrder:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        dummy_head = dummy
        
        while(l1 is not None and l2 is not None):
            
            if (l1.val <= l2.val):
                dummy.next = l1
                dummy = l1
                l1 = l1.next
            else:
                dummy.next = l2
                dummy = l2
                l2 = l2.next

        dummy.next = l1 if l2 is None else l2
        
        return dummy_head.next


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.val,end="->")
        temp = temp.next
    print()


sol = Solution()
## time complexity - O(m+n)
## space complexity - O(m+n)
print_linked_list(sol.mergeTwoLists(ListNode(1,ListNode(2,ListNode(4))), ListNode(1,ListNode(3, ListNode(4)))))


sol = SolutionInOrder()
## time complexity - O(m+n)
## space complexity - O(1)
print_linked_list(sol.mergeTwoLists(ListNode(1,ListNode(2,ListNode(4))), ListNode(1,ListNode(3, ListNode(4)))))
            