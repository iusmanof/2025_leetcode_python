# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        
        while cur and cur.next:
            nextPair = cur.next.next
            second = cur.next
            
            second.next = cur
            cur.next = nextPair
            prev.next = second
            
            prev = cur
            cur = nextPair
            
        
        return dummy.next