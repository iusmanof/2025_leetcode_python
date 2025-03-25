import unittest
import sys 
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from tsumclosest import Solution

class TestCaseTSumClosest(unittest.TestCase):
    
    def test_1(self):
        s = Solution()
        self.assertEqual(s.threeSumClosest([-1,2,1,-4], 1), 2)
    
    def test_2(self):
        s = Solution()
        self.assertEqual(s.threeSumClosest([0,0,0], 1), 0)