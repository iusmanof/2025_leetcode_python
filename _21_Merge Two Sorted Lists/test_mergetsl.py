import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from mergetsl import Solution, ListNode

class TestCaseMergeTwoSortedLists(unittest.TestCase):
    
    def list_to_linked(self, lst):
        dummy = ListNode(0)
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
    
    def linked_to_list(self, node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
    
    def test_1(self):
        s = Solution()  
        list1 = self.list_to_linked([1,2,4])
        list2 = self.list_to_linked([1,3,4])
        result_list = [1,1,2,3,4,4]
        self.assertEqual(self.linked_to_list(s.mergeTwoLists(list1,list2)), result_list)
        
