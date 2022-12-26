# Nicole Arcolino
# CSC 202 Lab 6

import unittest
import sorts
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple01(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_ss01(self):
        nums = [3, -3, 2, 10, 77, -1]
        comps = selection_sort(nums)
        self.assertEqual(comps, 15)
        self.assertEqual(nums, [-3, -1, 2, 3, 10, 77])

    def test_ss02(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 45)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_ss03(self):
        nums = [0, 0]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [0, 0])

    def test_simple02(self):
        nums = [23, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_is01(self):
        nums = [3, -3, 2, 10, 77, -1]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 8)
        self.assertEqual(nums, [-3, -1, 2, 3, 10, 77])

    def test_is02(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 9)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_is03(self):
        nums = [0, 0]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [0, 0])

if __name__ == '__main__': 
    unittest.main()
