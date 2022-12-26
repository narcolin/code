import unittest
from bears import bears

from base_convert import convert_helper
from base_convert import convert

class TestLab1(unittest.TestCase):

    def test_bears(self):
        self.assertEqual(bears(30), True)
        self.assertEqual(bears(24), False)
        self.assertEqual(bears(49827), False)

    def test_convert(self):
        self.assertEqual(convert(324508639,16),"13579BDF")

    def test_base_all_01(self):
        for i in range(2, 17):
            for j in range(0, min(i, 10)):
                self.assertEqual(convert(j, i), str(j))

    def test_base10_01(self):
        for i in range(10000):
           self.assertEqual(convert(i, 10),str(i))

if __name__ == "__main__":
        unittest.main()