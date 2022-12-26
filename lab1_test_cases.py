import unittest
from lab1 import *

# Nicole Arcolino
# CSC 202-07

# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter0(self):
        """find the largest value in an Empty list"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter1(self):
        """find the largest value in a list of 4"""
        self.assertEqual(max_list_iter([1, 4, 77, 2]), 77)

    def test_max_list_iter2(self):
        """find the largest value in a list with negative numbers"""
        self.assertEqual(max_list_iter([-1, 0, -3]), 0)

    def test_max_list_iter3(self):
        """find the largest value in a list with decimals"""
        self.assertEqual(max_list_iter([0.00001, 0.000001, .0000001]), 0.00001)

    def test_max_list_iter4(self):
        """find the largest value in a list with fractions"""
        self.assertEqual(max_list_iter([5/2, 4/2, 3/2]), 5/2)

    def test_max_list_iter5(self):
        """find the largest value in a list with repeating values"""
        self.assertEqual(max_list_iter([9, 9, 9, 8, 7]), 9)

    def test_reverse_rec0(self):
        """unit testing to reverse a list, recursively"""
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])

    def test_reverse_rec1(self):
        """reverse the list with repeated values and a decimal"""
        self.assertEqual(reverse_rec([0, 0, 0, 4, .33]), [.33, 4, 0, 0, 0])

    def test_reverse_rec2(self):
        """reverse the list that is the same"""
        self.assertEqual(reverse_rec([5, 2, 3, 2, 5]), [5, 2, 3, 2, 5])

    def test_reverse_rec3(self):
        """revers the list with negative values"""
        self.assertEqual(reverse_rec([-10, -3, 7, -1]), [-1, 7, -3, -10])

    def test_reverse_rec4(self):
        """reverse the list with all the same values"""
        self.assertEqual(reverse_rec([0, 0, 0]), [0, 0, 0])

    def test_reverse_rec5(self):
        """reverse the list with negative and fraction values"""
        self.assertEqual(reverse_rec([-1, 5/2, -1]), [-1, 5/2, -1])

    def test_bin_search0(self):
        """unit testing for binary search"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

    def test_bin_search1(self):
        """binary search in ordered list"""
        list_val =[2, 4, 7, 8, 12, 14, 18, 22, 25]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(7, 0, len(list_val)-1, list_val), 2)

    def test_bin_search2(self):
        """binary search when the target is not in the list"""
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(30, 0, len(list_val) - 1, list_val), None)
        self.assertRaises(ValueError, bin_search, 1, 0, 5, None)

    def test_bin_search3(self):
        """binary search with negative, decimals, and fraction values"""
        list_val = [-1, 0, .5, 5/2, 99, 300000]
        low = -1
        high = len(list_val) - 1
        self.assertEqual(bin_search(.5, -1, len(list_val) - 1, list_val), 2)

    def test_bin_search4(self):
        """binary search"""
        list_val = [-2, 5, 66, 77, 90, 678, 8000]
        low = -2
        high = len(list_val) - 1
        self.assertEqual(bin_search(678, -2, len(list_val) - 1, list_val), 5)

    def test_reverse_mutate0(self):
        """unit testing to reverse a list, iteratively"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_list_mutate(tlist)

    def test_reverse_mutate1(self):
        """reverse an unordered list"""
        self.assertEqual(reverse_list_mutate([6, 19, 4, 25, 17]), [17, 25, 4, 19, 6])

    def test_reverse_mutate2(self):
        """reverse a list with all the same values"""
        self.assertEqual(reverse_list_mutate([0, 0, 0]), [0, 0, 0])

    def test_reverse_mutate3(self):
        """reverse a list with negative and fraction values"""
        self.assertEqual(reverse_list_mutate([-1, 5/2, -1]), [-1, 5/2, -1])

    def test_reverse_mutate4(self):
        """reverse a list with only one value"""
        self.assertEqual(reverse_list_mutate([7]), [7])

    def test_reverse_mutate5(self):
        """reverse a list with decimal values"""
        self.assertEqual(reverse_list_mutate([.8, .7, .9]), [.9, .7, .8])


if __name__ == "__main__":
        unittest.main()

    
