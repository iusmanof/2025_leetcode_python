import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from searchip import Solution

class TestCaseDivideTwoIntegers(unittest.TestCase):
    
    def test_1(self):
        s = Solution()
        self.assertEqual(s.searchInsert([1,3,5,6], 5), 2)