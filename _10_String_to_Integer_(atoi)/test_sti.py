import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from sti import Solution

class TestCase(unittest.TestCase):
    
    def test_sti_strip42(self):
        s = Solution()
        self.assertEqual(s.myAtoi(" 42"), 42)
    
    def test_sti_plus42(self):
        s = Solution()
        self.assertEqual(s.myAtoi(" +42"), 42)
    
    def test_sti_minus42(self):
        s = Solution()
        self.assertEqual(s.myAtoi(" -42"), -42)
        
    def test_sti_alphabet_42(self):
        s = Solution()
        self.assertEqual(s.myAtoi("42wer"), 42)
    
    def test_sti_alphabet_0_minus_1(self):
        s = Solution()
        self.assertEqual(s.myAtoi("0-1"), 0)
    
    def test_sti_alphabet_1234_alphabet(self):
        s = Solution()
        self.assertEqual(s.myAtoi("1234c0d3"), 1234)    
        