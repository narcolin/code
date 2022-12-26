import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), [5])

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_02(self):
        ht = HashTable(5)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 2)
        ht.insert("f", 0)
        self.assertEqual(ht.get_index("f"), 3)
        ht.insert("k", 0) #causes rehash
        self.assertEqual(ht.get_index("a"), 9)
        self.assertEqual(ht.get_index("f"), 3)
        self.assertEqual(ht.get_index("k"), 8)


    def test_02_one_item(self):
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash("cat"), 3)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)
        self.assertEqual(ht.get_num_items(), 1)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)
        self.assertEqual(ht.get_all_keys(), ["cat"])
        self.assertEqual(ht.in_table("cat"), True)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_03_multiple_same_key(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("cat", 10)
        ht.insert("cat", 15)
        ht.insert("cat", 20)
        self.assertEqual(ht.get_index("cat"), 3)

        self.assertEqual(ht.get_value("cat"), 20)

    def test_05_quad_wrap_around(self):
        table = HashTable(211)

        for i in range(10, 101):
            table.insert(chr(i), 10 * i)
        key = chr(1) + 'E'
        table.insert(key, 'cat')  # Hashes to 100, goes to 101
        self.assertTrue(table.in_table(key))
        self.assertEqual(table.get_index(key), 101)

        self.assertEqual(table.get_value(key), 'cat')
if __name__ == '__main__':
   unittest.main()
