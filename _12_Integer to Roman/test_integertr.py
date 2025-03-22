import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from integertr import Solution

class TestCase (unittest.TestCase):
    
    def test_integertr_3749(self):
        s = Solution()
        self.assertEqual(s.intToRoman(3749), "MMMDCCXLIX")
    
    def test_integertr_58(self):
        s = Solution()
        self.assertEqual(s.intToRoman(58), "LVIII")
        
    def test_integertr_1994(self):
        s = Solution()
        self.assertEqual(s.intToRoman(1994), "MCMXCIV")