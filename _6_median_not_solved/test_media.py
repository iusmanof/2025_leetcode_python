import unittest
import sys
import os 

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from median import Solution

class TestCase(unittest.TestCase):
    
    def test_median_13_2(self):
        s = Solution()
        self.assertEqual(s.findMedianSortedArrays([1,3],[2]), 2.0)
    
    def test_median_12_34(self):
        s = Solution()
        self.assertEqual(s.findMedianSortedArrays([1,2],[3,4]), 2.5)