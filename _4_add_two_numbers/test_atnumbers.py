import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from atnumbers  import Solution, ListNode

def lists_are_equal(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1, l2 = l1.next, l2.next
    return l1 is None and l2 is None

class TestCase(unittest.TestCase):

    def test_add_two_numbers_243_564(self):
        s = Solution()
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)
        
        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)
        
        l3 = ListNode(7)
        l3.next = ListNode(0)
        l3.next.next = ListNode(8)
        
        result = s.addTwoNumbers(l1, l2)
        self.assertTrue(lists_are_equal(s.addTwoNumbers(l1, l2), l3))
    
    def test_add_two_numbers_9999999_9999(self):
        s = Solution()
        l1 = ListNode(9)
        l1.next = ListNode(9)
        l1.next.next = ListNode(9)
        l1.next.next.next = ListNode(9)
        l1.next.next.next.next = ListNode(9)
        l1.next.next.next.next.next = ListNode(9)
        l1.next.next.next.next.next.next = ListNode(9)
        
        l2 = ListNode(9)
        l2.next = ListNode(9)
        l2.next.next = ListNode(9)
        l2.next.next.next = ListNode(9)
        
        l3 = ListNode(8)
        l3.next = ListNode(9)
        l3.next.next = ListNode(9)
        l3.next.next.next = ListNode(9)
        l3.next.next.next.next = ListNode(0)
        l3.next.next.next.next.next = ListNode(0)
        l3.next.next.next.next.next.next = ListNode(0)
        l3.next.next.next.next.next.next.next = ListNode(1)
        
        result = s.addTwoNumbers(l1, l2)
        self.assertTrue(lists_are_equal(s.addTwoNumbers(l1, l2), l3))
        
if __name__ == '__main__':
    unittest.main()