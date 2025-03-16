import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from roman import Solution

class TestSolution(unittest.TestCase):

    def test_roman_3(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt('III'), 3)
    
    def test_roman_58(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt('LVIII'), 58)
    
    def test_roman_9(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt('IX'), 9)

    def test_roman_1900(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt('MCM'), 1900)
        
    def test_roman_1994(self):
        solution = Solution()
        self.assertEqual(solution.romanToInt('MCMXCIV'), 1994)

if __name__ == '__main__':
    unittest.main()
