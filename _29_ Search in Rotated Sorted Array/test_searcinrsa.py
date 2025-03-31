import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from searchinrsa import Solution

class TestCaseDivideTwoIntegers(unittest.TestCase):
    
    def test_1(self):
        s = Solution()
        self.assertEqual(s.search([4,5,6,7,0,1,2], 0), 4)