# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        first_head, second_head = None, None
        first_iterator, second_iterator = ListNode(0), ListNode(0)
        
        iterator = head
        while iterator:
            if iterator.val < x:
                first_iterator.next = iterator
                first_iterator = iterator
                if first_head == None:
                    first_head = iterator
            else:
                second_iterator.next = iterator
                second_iterator = iterator
                if second_head == None:
                    second_head = iterator
            iterator = iterator.next

        if first_head == None:
            first_head = second_head
        else:
            first_iterator.next = second_head
            second_iterator.next = None
        return first_head


def list_to_string(head):
    result = "["
    iteartor = head
    while iteartor:
        result += str(iteartor.val) + ", "
        iteartor = iteartor.next
    result += "]"
    return result


head = ListNode(1)
# a = ListNode(4)
# b = ListNode(3)
# c = ListNode(2)
# d = ListNode(5)
# e = ListNode(2)
# #f = ListNode(2)

# head.next = a
# a.next = b
# b.next = c
# c.next = d
# d.next = e
# #e.next = f

s = Solution()
print list_to_string(s.partition(head, 0))