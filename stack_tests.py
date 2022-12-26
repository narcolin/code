# Lab 2
# Nicole Arcolino

import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
# from stack_array import Stack
from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

    def test_1(self):
        stack = Stack(11)
        stack.push(2)
        stack.pop()
        with self.assertRaises(IndexError): stack.pop()
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 0)
        with self.assertRaises(IndexError): stack.peek()

    def test_2(self):
        stack = Stack(2)
        stack.push(None)
        self.assertFalse(stack.is_full())

    def test_3(self):
        stack = Stack(0)
        self.assertTrue(stack.is_empty())
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(), 0)
        with self.assertRaises(IndexError): stack.pop()

    def test_4(self):
        stack = Stack(4000)
        stack.push(3999)
        self.assertEqual(stack.size(), 1)
        stack.push(1)
        self.assertFalse(stack.is_full())
        stack.pop()
        self.assertEqual(stack.peek(), 3999)

    def test_5(self):
        stack = Stack(2)
        stack.push(2)
        stack.push(5)
        with self.assertRaises(IndexError): stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.pop(), 5)

    def test_6(self):
        stack = Stack(5)
        stack.push(5)
        stack.push(1.11)
        stack.push(-8)
        self.assertEqual(stack.peek(), -8)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 3)
        stack.pop()
        self.assertEqual(stack.peek(), 1.11)
        stack.pop()
        stack.pop()
        self.assertTrue(stack.is_empty())
        self.assertFalse(stack.is_full())
        with self.assertRaises(IndexError): stack.pop()


if __name__ == '__main__': 
    unittest.main()
