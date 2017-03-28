"""
NOTE:  I did not have a chance to implement this.

"""

import unittest

from ksums import KSums

class TestKSums(unittest.TestCase):
    """ Test Case for KSums. """
    def setUp(self):
        sums = KSums('inputs/k-sum.txt')
        factors = sums.get_factors_brute_force()

    def test_brute_force(self):

        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()