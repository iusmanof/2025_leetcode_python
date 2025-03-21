import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from revint import Solution 

class TestCase(unittest.TestCase):
    
    def test_revint_123(self):
        s = Solution()
        self.assertEqual(s.reverse(123), 321)
        
    def test_revint_minus__123(self):
        s = Solution()
        self.assertEqual(s.reverse(-123), -321)
    
    def test_revint_minus_120(self):
        s = Solution()
        self.assertEqual(s.reverse(120), 21)
    
    def test_revint_minus_2147483648(self):
        s = Solution()
        self.assertEqual(s.reverse(-2147483650), -563847412)  
        
    def test_revint_2147483648(self):
        s = Solution()
        self.assertEqual(s.reverse(2147483640), 463847412)  
        
        