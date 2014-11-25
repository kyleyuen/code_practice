# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        result = ListNode(0)
        previous = result
        carry = 0

        # add list l1 and l2
        while (l1 is not None) and (l2 is not None):
            current = ListNode(0)
            current.val = l1.val + l2.val + carry
            carry = 0
            if current.val >= 10:
                current.val -= 10
                carry = 1

            previous.next = current
            previous = current
            l1 = l1.next
            l2 = l2.next

        # process l1 and carry
        while l1 is not None:
            current = ListNode(0)
            current.val = l1.val + carry
            carry = 0
            if current.val >= 10:
                current.val -= 10
                carry = 1

            previous.next = current
            previous = current
            l1 = l1.next

        # process l2 and carry
        while l2 is not None:
            current = ListNode(0)
            current.val = l2.val + carry
            carry = 0
            if current.val >= 10:
                current.val -= 10
                carry = 1

            previous.next = current
            previous = current
            l2 = l2.next

        if carry == 1:
            current = ListNode(1)
            previous.next = current

        return result.next


def print_list(l):
    while l != None:
        print l.val
        l = l.next


s = Solution()
a = ListNode(2)
b = ListNode(4)
a.next = b
c = ListNode(3)
b.next = c

x = ListNode(5)
y = ListNode(6)
x.next = y
z = ListNode(6)
y.next = z
print_list(s.addTwoNumbers(a, x))