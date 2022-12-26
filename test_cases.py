import unittest
import perm_lex
import base_convert
import bears

class TestProject1(unittest.TestCase):
    def test_perm_lex(self):
        self.assertEqual(perm_lex('abc', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        self.assertEqual(perm_lex('bc', ['bc', 'cb']))
        pass



    # def test_base_convert(self):
    #     self.assertEqual(base_convert(30, 4), 132)
    #     self.assertEqual(base_convert(45, 2), 101101)






if __name__ == "__main__":
    unittest.main()