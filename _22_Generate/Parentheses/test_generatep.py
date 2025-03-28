import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from generatep import Solution

class TestCaseGenerateParentheses(unittest.TestCase):
    
    def test_1(self):
        s = Solution()
        self.assertEqual(s.generateParenthesis(3), ["((()))","(()())","(())()","()(())","()()()"])

    def test_2(self):
        s = Solution()
        self.assertEqual(s.generateParenthesis(1),  ["()"])
    