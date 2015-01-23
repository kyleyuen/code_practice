# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        fake_head = ListNode(0)
        fake_head.next = head

        outside_head = fake_head
        for i in range(m-1):
            outside_head = outside_head.next
        inside_head = outside_head.next

        inside_tail = inside_head
        for j in range(n-m):
            inside_tail = inside_tail.next
        print outside_head.val, inside_tail.val
        outside_head.next = self.reverse_list(inside_head, inside_tail)

        return fake_head.next

    def reverse_list(self, head, tail):
        previous = head
        current = head.next
        head.next = tail.next
        while previous != tail:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return tail


def list_to_string(head):
    result = "["
    iterator = head
    while iterator:
        result += str(iterator.val) + ", "
        iterator = iterator.next
    result += "]"
    return result


head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
head.next = a
a.next = b
b.next = c
c.next = d

s = Solution()
print list_to_string(s.reverseBetween(head, 1, 5))