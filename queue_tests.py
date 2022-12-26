# CSC 202 Lab 3
# Nicole Arcolino

import unittest
from queue_array import Queue
# from queue_linked import Queue

class TestLab1(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_queue_full(self):
        q = Queue(5)
        q.enqueue('n')
        q.enqueue(-1)
        q.enqueue(-2)
        q.enqueue(-3)
        q.enqueue(-4)
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        self.assertRaises(IndexError, q.enqueue, 5)  # exception
        self.assertEqual(q.size(), 5)
        self.assertTrue(q.size(), 5)

    def test_queue_dequeue(self):
        q = Queue(2)
        q.enqueue(0)
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.size(), 1)

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())

        self.assertRaises(IndexError, q.dequeue)  # exception

    def test_queue_enqueue(self):
        q = Queue(4)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertFalse(q.is_empty())
        self.assertTrue(q.is_full())
        self.assertRaises(IndexError, q.enqueue, 5)  # exception
        self.assertEqual(q.size(), 4)

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 3)

    def test_queue_none(self):
        q = Queue(5)
        q.enqueue(None)
        q.enqueue(16)
        q.enqueue(2)
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 3)

    def test_queue_empty(self):
        q = Queue(0)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())

if __name__ == '__main__': 
    unittest.main()
