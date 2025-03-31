import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from divideti import Solution

class TestCaseDivideTwoIntegers(unittest.TestCase):
    
    def test_1(self):
        s = Solution()
        self.assertEqual(s.divide(10, 3), 3)