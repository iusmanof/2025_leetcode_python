import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from validp import Solution

class TestCaseValidParentheses(unittest.TestCase):

    def test_1(self):
        s = Solution()
        self.assertEqual(s.isValid("()"), True)
    
    def test_2(self):
        s = Solution()
        self.assertEqual(s.isValid("()[]{}"), True)
    
    def test_3(self):
        s = Solution()
        self.assertEqual(s.isValid("(]"), False)