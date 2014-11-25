# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
    	length = len(lists)
    	if length == 0:
    		return None
        elif length == 1:
        	return lists[0]
        elif length == 2:
        	if lists[0]==None and lists[1]!=None:
        		return lists[1]
        	if lists[0]!=None and lists[1]==None:
        		return lists[0]
        	if lists[0]==None and lists[1]==None:
        		return None

        	result = ListNode(0)
        	previous = result
        	A, B = lists[0], lists[1]
        	while A and B:
        		if A.val < B.val:
        			current = ListNode(A.val)
        			previous.next = current
        			previous = current
        			A = A.next
        		else:
        			current = ListNode(B.val)
        			previous.next = current
        			previous = current
        			B = B.next

        	while A:
    			current = ListNode(A.val)
        		previous.next = current
        		previous = current
        		A = A.next
    		while B:
    			current = ListNode(B.val)
        		previous.next = current
        		previous = current
        		B = B.next
        	return result.next
        else:
        	a = self.mergeKLists(lists[0:length/2])
        	b = self.mergeKLists(lists[length/2:length])
        	return self.mergeKLists([a, b])


def print_list(head):
	while head != None:
		print head.val
		head = head.next


lists = []

head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)
head.next = a
a.next = b
b.next = c
c.next = d
lists.append(head)

head = ListNode(6)
a = ListNode(7)
b = ListNode(8)
c = ListNode(9)
d = ListNode(10)
head.next = a
a.next = b
b.next = c
c.next = d
lists.append(head)

head = ListNode(11)
a = ListNode(12)
b = ListNode(13)
c = ListNode(14)
d = ListNode(15)
head.next = a
a.next = b
b.next = c
c.next = d
lists.append(head)

head = ListNode(6)
a = ListNode(7)
b = ListNode(8)
c = ListNode(9)
d = ListNode(10)
head.next = a
a.next = b
b.next = c
c.next = d
lists.append(head)

head = ListNode(6)
a = ListNode(7)
b = ListNode(8)
c = ListNode(9)
d = ListNode(10)
head.next = a
a.next = b
b.next = c
c.next = d
lists.append(head)

s = Solution()
print_list(s.mergeKLists(lists))