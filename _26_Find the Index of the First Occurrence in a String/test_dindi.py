import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from findi import Solution

class TestCaseFindTheIndexOfTheFirstOccurrenceInString(unittest.TestCase):
    
    def test_1(self):
        s = Solution()
        self.assertEqual(s.strStr("sadbutsad", "sad" ), 0)