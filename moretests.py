import unittest
import permgenlex
import base_convert
import teddybearpicnic

class TestProject1(unittest.TestCase):
    def test_perm_lex(self):
        self.assertEqual(permgenlex('abc', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        self.assertEqual(permgenlex('bc', ['bc', 'cb']))
        pass

    def test_base_convert(self):
        self.assertEqual(base_convert(30, 4), 132)
        self.assertEqual(base_convert(45, 2), 101101)
