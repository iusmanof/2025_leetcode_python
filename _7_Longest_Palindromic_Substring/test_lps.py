import unittest
import sys
import os 

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from lps import Solution

class TestCase(unittest.TestCase):
    
    def test_lps_babad(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("babad"), "bab")

    def test_lps_cbbd(self):
        s = Solution()
        self.assertEqual(s.longestPalindrome("cbbd"), "bb")