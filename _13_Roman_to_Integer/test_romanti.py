import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from romanti import Solution

class TestCaseRomanToIteger(unittest.TestCase):
    
    def test_romanti_14(self):
        s = Solution()
        self.assertEqual(s.romanToInt("XIV"), 14)
        
    def test_romanti_3(self):
        s = Solution()
        self.assertEqual(s.romanToInt("III"), 3)
    
    def test_romanti_58(self):
        s = Solution()
        self.assertEqual(s.romanToInt("LVIII"), 58)
        
    def test_romanti_1994(self):
        s = Solution()
        self.assertEqual(s.romanToInt("MCMXCIV"), 1994)