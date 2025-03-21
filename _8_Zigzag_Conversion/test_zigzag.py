import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from zigzag import Solution

class TestCase(unittest.TestCase):
    
    def test_zigzag_PAYPALISHIRING3(self):
        s = Solution()
        self.assertEqual(s.convert("PAYPALISHIRING",3),"PAHNAPLSIIGYIR")
    
    def test_zigzag_PAYPALISHIRING4(self):
        s = Solution()
        self.assertEqual(s.convert("PAYPALISHIRING",4), "PINALSIGYAHRPI")
        
    def test_zigzag_A(self):
        s = Solution()
        self.assertEqual(s.convert("A",1),"A")
        