import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from longestcpr import Solution

class TestCaseLongestCommonPrefix(unittest.TestCase):
    
    def test_flowers_flow_flight(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(["flower","flow","flight"]),"fl")
        
    def test_flowers_dog_race(self):
        s = Solution()
        self.assertEqual(s.longestCommonPrefix(["dog","racecar","car"]),"")