# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        slower, faster = head, head
        for i in range(n):
        	faster = faster.next
        if faster == None:
        	return head.next
        
        while faster.next != None:
        	slower = slower.next
        	faster = faster.next
        slower.next = slower.next.next
        return head


def print_list(head):
	while head != None:
		print head.val
		head = head.next

s = Solution()
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
head = s.removeNthFromEnd(head, 5)
print 
print_list(head)