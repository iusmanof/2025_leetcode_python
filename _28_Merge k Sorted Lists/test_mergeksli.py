import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from mergeksl import Solution, ListNode

class TestCaseMergeKSL(unittest.TestCase):
    
    def list_to_linked_list(self, arr):
        if not arr:
            return None
        dummy = ListNode(0)
        current = dummy
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def test_two_lists(self):
        s = Solution()
        l1 = self.list_to_linked_list([1, 4, 5])
        l2 = self.list_to_linked_list([1, 3, 4])
        expected = self.list_to_linked_list([1, 1, 3, 4, 4, 5])
        self.assertEqual(s.mergeKLists([l1, l2]), expected)