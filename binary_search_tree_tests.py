import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertEqual(bst.level_order_list(), [10])

    def test_1(self):
        bst = BinarySearchTree()
        bst.insert(22, 'number')
        bst.insert(-3, 'negative')
        self.assertFalse(bst.search(4))
        self.assertEqual(bst.find_min(), (-3, 'negative'))
        bst.insert(23, 'number')
        self.assertEqual(bst.find_max(), (23, 'number'))
        self.assertEqual(bst.preorder_list(), [22, -3, 23])
        self.assertEqual(bst.level_order_list(), [22, -3])
        self.assertFalse(bst.is_empty())
        self.assertEqual(bst.tree_height(), 1)

    def test_2(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.inorder_list(), [])
        self.assertTrue(bst.is_empty())
        bst.insert(0, 'number')
        bst.insert(0, 'number')
        bst.insert(0, 'number')
        self.assertEqual(bst.find_max(), (0, 'number'))
        self.assertEqual(bst.level_order_list(), [0])

    def test_3(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(12, 'stuff')
        bst.insert(13, 'stuff')
        bst.insert(14, 'stuff')
        bst.insert(11, 'stuff')
        bst.insert(17, 'stuff')
        bst.insert(10, 'stuff')
        bst.insert(9, 'stuff')
        self.assertTrue(bst.search(11))
        self.assertEqual(bst.find_min(), (9, 'stuff'))
        self.assertEqual(bst.find_max(), (17, 'stuff'))
        self.assertEqual(bst.tree_height(), 3)
        self.assertEqual(bst.inorder_list(), [9, 10, 11, 12, 13, 14, 17])
        self.assertEqual(bst.preorder_list(), [12, 11, 10, 9, 13, 14, 17])
        self.assertEqual(bst.level_order_list(), [12, 11, 10, 9])

    def test_4(self):
        bst = BinarySearchTree()
        bst.insert(-2, 'negative')
        bst.insert(-3, 'negative')
        bst.insert(-4, 'negative')
        self.assertFalse(bst.search(4))
        self.assertEqual(bst.find_min(), (-4, 'negative'))
        self.assertEqual(bst.find_max(), (-2, 'negative'))
        self.assertEqual(bst.preorder_list(), [-2, -3, -4])
        self.assertFalse(bst.is_empty())


if __name__ == '__main__':
    unittest.main()
