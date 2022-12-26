# CPE 202 Lab 1
# Nicole Arcolino

import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

    def test_repr2(self):
        loc = Location("Austin", 68.9, 12.4)
        self.assertEqual(repr(loc), "Location('Austin', 68.9, 12.4)")

    def test_eq(self):
        loc1 = Location("SLO", 25, -120)
        loc2 = Location("AUS", 25, -120)
        self.assertFalse(loc1 == loc2)

    def test_eq(self):
        loc1 = Location("LAX", 44, -80)
        loc2 = Location("LAX", 44, -80)
        self.assertTrue(loc1 == loc2)



if __name__ == "__main__":
    unittest.main()
