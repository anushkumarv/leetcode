from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        t = list()
        while cur:
            t.append(cur)
            cur = cur.next

        n = len(t)
        l, r = 0, len(t) - 1
        while l < r:
            t[l].next = t[r]
            t[r].next = t[l+1]
            l += 1
            r -= 1

        last = n // 2
        t[last].next = None

        return t[0]

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.val,end="->")
        temp = temp.next
    print()


sol = Solution()
## time complexity - O(n)
## space complexity - O(n)
print_linked_list(sol.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))


class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return head


sol = Solution()
## time complexity - O(n)
## space complexity - O()
print_linked_list(sol.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))