# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
    	if head==None:
    		return None
        
        length = self.get_lentgh(head)
        k %= length
        if k==0:
            return head

        slower, faster = head, head
        for i in range(k):
            if not faster.next:
                return head
            faster = faster.next

        while faster.next:
            slower = slower.next
            faster = faster.next

        result = slower.next
        slower.next = faster.next
        faster.next = head
        return result


    def get_lentgh(self, head):
        result = 0
        while head:
            result += 1
            head = head.next
        return result

def print_list(head):
    while head != None:
        print head.val
        head = head.next


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
print_list(s.rotateRight(a, 3))