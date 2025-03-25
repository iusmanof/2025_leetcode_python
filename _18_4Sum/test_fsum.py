import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from fsum import Solution

class TestCase4Sum(unittest.TestCase):
    
    def test_1(self):
        s = Solution()
        self.assertEqual(s.fourSum([1,0,-1,0,-2,2],0),  [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
    
    def test_2(self):
        s = Solution()
        self.assertEqual(s.fourSum([2,2,2,2,2], 8), [[2,2,2,2]])