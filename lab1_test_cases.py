# CPE 202 Lab 1
# Nicole Arcolino

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter1(self):
        int_list = None
        with self.assertRaises(ValueError):  # used to check for exception, list is None
            max_list_iter(int_list)
        self.assertEqual(max_list_iter([]), None)  # 2nd exception, list is empty

    def test_max_list_inter2(self):
        self.assertEqual(max_list_iter([12, 31, 4, 3]), 31)    # check valid list with a max
        self.assertEqual(max_list_iter([10, 11, 12]), 12)    # check valid list with a max

    def test_reverse_rec(self):
        int_list = []
        with self.assertRaises(ValueError):  # exception if list is None/empty
            reverse_rec(int_list)

    def test_reverse_rec2(self):
        self.assertEqual(reverse_rec([]),[])   # check the reverse for a valid list
        self.assertEqual(reverse_rec([1, 2, 3]),[3, 2, 1])   # check the reverse for a valid list
        self.assertEqual(reverse_rec([5, 2, 7]), [7, 2, 5])    # check the reverse for a valid list
        self.assertEqual(reverse_rec([12, 31, 4, 66]), [66, 4, 31, 12])    # check the reverse for a valid list

    def test_bin_search1(self):
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]  # check for a valid binary search
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

        list_val =[2, 4, 7, 8, 12, 14, 18, 22, 25]  # check for a valid binary search
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(7, 0, len(list_val)-1, list_val), 2)

    def test_bin_search2(self):  # exception, when target is not found, return None
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(30, 0, len(list_val) - 1, list_val), None)
        self.assertRaises(ValueError, bin_search, 1, 0, 5, None)

if __name__ == "__main__":
        unittest.main()