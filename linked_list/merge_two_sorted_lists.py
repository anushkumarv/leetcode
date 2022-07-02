
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
            