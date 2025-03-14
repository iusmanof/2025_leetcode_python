import unittest

from twosum import twosum_func

class TwoSumTestCase(unittest.TestCase):
    def test_twosum_func(self):
        result = twosum_func([2,7,11,15], 9)
        self.assertEqual(result, [0, 1])
    

if __name__ == '__main__':
    unittest.main()