import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from swapnip import Solution, ListNode

class TestCaseSwapNodesInPairs(unittest.TestCase):
    
    def list_to_linked(self, lst):
        dummy = ListNode(0)
        current = dummy
        for v in lst:
            current.next = ListNode(v)
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
        head = self.list_to_linked([1,2,3,4])

        self.assertEqual(self.linked_to_list(s.swapPairs(head)), [2,1,4,3])