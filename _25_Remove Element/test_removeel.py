import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from removeel import Solution

class TestCaseRemoveDuplicatesFromSortedArray(unittest.TestCase):
    
    def test_1(self):
        s = Solution()
        self.assertEqual(s.removeElement([3,2,2,3], 3), 2)