# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        dumb_head = ListNode(0)
        dumb_head.next = head
        previous, current = dumb_head, dumb_head
        counter = 0
        while current:
        	if counter == k:
        		counter = 0

        		target = self.reverse_list(previous.next, current)
        		previous.next = current
        		previous = target
        		current = target
        	else:
        		counter += 1
        		current = current.next
        return dumb_head.next


    def reverse_list(self, head, tail):
    	previous = head
    	current = head.next
    	head.next = tail.next
    	while previous != tail:
    		temp = current.next
    		current.next = previous
    		previous = current
    		current = temp
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
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
head.next = a
a.next = b
b.next = c
c.next = d

s = Solution()
print list_to_string(s.reverseKGroup(head, 3))
