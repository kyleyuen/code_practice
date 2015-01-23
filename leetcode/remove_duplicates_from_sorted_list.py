# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        previous, current = head, head
        while current:
            if previous.val != current.val:
                previous.next = current
                previous = current
            current = current.next

        if previous:
            previous.next = None
        return head


def list_to_string(head):
    result = "["
    iteartor = head
    while iteartor:
        result += str(iteartor.val) + ", "
        iteartor = iteartor.next
    result += "]"
    return result


head = ListNode(1)
a = ListNode(1)
b = ListNode(2)
head.next = a
#a.next = b

s = Solution()
print list_to_string(s.deleteDuplicates(head))