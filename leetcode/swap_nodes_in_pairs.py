# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(head):
	while head != None:
		print head.val
		head = head.next

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
    	previous, current = head, head
        if head and head.next:
        	temp = head.next
        	target = temp.next
        	head.next = target
        	temp.next = head

        	previous = head
        	current = previous.next
        	head = temp
        else:
        	return head

        while current and current.next:
        	temp = current.next
        	target = temp.next        	
        	previous.next = temp
        	temp.next = current
        	current.next = target

        	previous = current
        	current = previous.next
        return head


head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
head.next = a
a.next = b
b.next = c
c.next = d
print_list(head)
print

s = Solution()
print_list(s.swapPairs(head))
