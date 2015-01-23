# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            if l2:
                return l2
            else:
                return l1
        elif not l2:
            return l1
        
        head = None
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        previous = head
        while l1 and l2:
            if l1.val < l2.val:
                previous.next = l1
                previous = l1
                l1 = l1.next
            else:
                previous.next = l2
                previous = l2
                l2 = l2.next

        while l1:
            previous.next = l1
            previous = l1
            l1 = l1.next
        while l2:
            previous.next = l2
            previous = l2
            l2 = l2.next

        return head


def print_list(head):
    while head != None:
        print head.val
        head = head.next


head = ListNode(1)
a = ListNode(2)
b = ListNode(10)
c = ListNode(4)
d = ListNode(5)
head.next = b
a.next = c
c.next = d

s = Solution()
print_list(s.mergeTwoLists(head, a))
