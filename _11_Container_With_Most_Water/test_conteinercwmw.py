import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from containerwmw import Solution

class TestCase(unittest.TestCase):
    
    def test_containerwmw_186254837(self):
        s = Solution()
        self.assertEqual(s.maxArea([1,8,6,2,5,4,8,3,7]), 49)
    
    def test_containerwmw__11(self):
        s = Solution()
        self.assertEqual(s.maxArea([1,1]), 1)