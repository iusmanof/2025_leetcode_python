import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from removedub import Solution

class TestCaseRemoveDuplicatesFromSortedArray(unittest.TestCase):
    
    def test_1(self):
        s = Solution()
        self.assertEqual(s.removeDuplicates([1,1,2]), 2)