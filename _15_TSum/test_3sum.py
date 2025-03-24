import unittest
import sys
import os 

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from tsum import Solution

class TestCase3Sum(unittest.TestCase):
    
    def test_1(self):
        s = Solution()
        self.assertEqual(s.threeSum([0,1,1]), [])
    
    def test_1(self):
        s = Solution()
        self.assertEqual(s.threeSum([0,0,0]), [[0,0,0]])