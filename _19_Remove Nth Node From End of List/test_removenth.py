import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from removenth import Solution, ListNode

class TestCaseRemoveNthNode(unittest.TestCase):


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
        head = self.list_to_linked([1, 2, 3, 4, 5])
        result = s.removeNthFromEnd(head, 2)
        self.assertEqual(self.linked_to_list(result), [1, 2, 3, 5])
    
    def test_2(self):
        s = Solution()
        head = self.list_to_linked([1])
        result = s.removeNthFromEnd(head, 1)
        self.assertEqual(self.linked_to_list(result), [])

    def test_3(self):
        s = Solution()
        head = self.list_to_linked([1,2])
        result = s.removeNthFromEnd(head, 1)
        self.assertEqual(self.linked_to_list(result), [1])
        
