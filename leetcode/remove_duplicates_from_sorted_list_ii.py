# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        fake_head = ListNode(0)
        fake_head.next = head

        previous, current = fake_head, head
        while current:
            while current.next and (current.val == current.next.val):
                current = current.next
            
            if previous.next == current:
                previous = current
            else:
                previous.next = current.next
            current = current.next

        return fake_head.next


def list_to_string(head):
    result = "["
    iterator = head
    while iterator:
        result += str(iterator.val) + ", "
        iterator = iterator.next
    result += "]"
    return result


head = ListNode(1)
a = ListNode(1)
b = ListNode(2)
c = ListNode(2)
d = ListNode(3)
head.next = a
a.next = b
b.next = c
c.next = d

s = Solution()
print list_to_string(s.deleteDuplicates(None))