# CSC 202 Lab 4
# Nicole Arcolino

import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_1(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(8)
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.size(), 1)
        t_list.add(8)
        self.assertEqual(t_list.size(), 1)
        t_list.add(14)
        self.assertEqual(t_list.size(), 2)
        t_list.add(11)
        t_list.add(4)
        t_list.add(1)
        self.assertEqual(t_list.python_list(), [1, 4, 8, 11, 14])
        self.assertEqual(t_list.python_list_reversed(), [14, 11, 8, 4, 1])
        self.assertEqual(t_list.pop(2), 8)
        self.assertFalse(t_list.remove(3))
        self.assertFalse(t_list.search(8))
        self.assertTrue(t_list.search(4))
        t_list.add(90)
        t_list.add(80)
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list(), [1, 4, 11, 14, 80, 90])
        self.assertEqual(t_list.index(4), 1)
        self.assertEqual(t_list.index(90), 5)
        self.assertEqual(t_list.index(14), 3)
        self.assertEqual(t_list.index(-144), None)

    def test_2(self):
        t_list = OrderedList()
        self.assertFalse(t_list.remove(0))
        with self.assertRaises(IndexError): t_list.pop(0)
        with self.assertRaises(IndexError): t_list.pop(-1)
        t_list.add(13)
        t_list.add(-7)
        self.assertEqual(t_list.pop(0), -7)
        self.assertEqual(t_list.pop(0), 13)
        self.assertTrue(t_list.is_empty())
        self.assertFalse(t_list.search(10))
        t_list.add(-7)
        self.assertFalse(t_list.search(8))
        self.assertEqual(t_list.python_list(), [-7])
        self.assertEqual(t_list.python_list_reversed(), [-7])
        t_list.add(144)
        t_list.add(-144)
        self.assertEqual(t_list.python_list(), [-144, -7, 144])
        with self.assertRaises(IndexError): t_list.pop(5)

if __name__ == '__main__': 
    unittest.main()
