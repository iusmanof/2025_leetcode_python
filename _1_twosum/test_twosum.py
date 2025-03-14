import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '1_twosum')))

from _1_twosum.twosum import twosum_func

class TwoSumTestCase(unittest.TestCase):
    def test_twosum(self):
        result = twosum_func([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])

    def test_no_solution(self):
        result = twosum_func([1, 2, 3], 10)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
