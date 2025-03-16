import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from palindrome import Solution

class TestSolution(unittest.TestCase):

    def test_palindrome_positive(self):
        solution = Solution()
        self.assertTrue(solution.isPalindrome(121))

    def test_palindrome_zero(self):
        solution = Solution()
        self.assertTrue(solution.isPalindrome(0))

    def test_palindrome_negative(self):
        solution = Solution()
        self.assertFalse(solution.isPalindrome(-121))

    def test_palindrome_ending_zero(self):
        solution = Solution()
        self.assertFalse(solution.isPalindrome(10))

    def test_non_palindrome(self):
        solution = Solution()
        self.assertFalse(solution.isPalindrome(123))

    def test_large_palindrome(self):
        solution = Solution()
        self.assertTrue(solution.isPalindrome(123454321))

    def test_large_non_palindrome(self):
        solution = Solution()
        self.assertFalse(solution.isPalindrome(123456789))

if __name__ == '__main__':
    unittest.main()
