# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """        
        resultNode = ListNode()
        cur = resultNode
        total = 0
        tmp = 0
        while l1 or l2 or tmp:
            val1 = None
            val2 = None
            if l1:
                val1 = l1.val
            else:
                val1 = 0
                
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            
            total = val1 + val2 + tmp
            tmp = total // 10
            cur.next = ListNode(total % 10)
            cur = cur.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return resultNode.next