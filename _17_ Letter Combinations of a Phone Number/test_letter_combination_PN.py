import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from letter_combination_PN import Solution

class TestCaseLetterCombinations(unittest.TestCase):
    
    def test_1(self):
        s = Solution()
        self.assertEqual(s.letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])
    
    def test_2(self):
        s = Solution()
        self.assertEqual(s.letterCombinations(""), [])
        
    def test_3(self):
        s = Solution()
        self.assertEqual(s.letterCombinations("2"), ["a", "b", "c"])