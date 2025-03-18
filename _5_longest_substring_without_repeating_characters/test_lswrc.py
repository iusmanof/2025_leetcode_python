import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from lswrc import Solution

class TestCase(unittest.TestCase):
    def test_lswrc_abcabcbb(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring("abcabcbb"),3)
        
    def test_lswrc_bbbbb(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring("bbbbb"), 1)
        
    def test_lswrc_pwwkew(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring("pwwkew"), 3)
        