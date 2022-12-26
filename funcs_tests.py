import unittest
import funcs

class TestCases(unittest.TestCase):

    def test_f(self):
        self.assertEqual(funcs.f(1), 9)
        self.assertEqual(funcs.f(3), 69)
        pass

    def test_g(self):
        self.assertEqual(funcs.g(1, 2), 5)
        self.assertEqual(funcs.g(3, 4), 25)
        pass

    def test_hypotenuse(self):
        self.assertEqual(funcs.hypotenuse(2, 3), 0.0)
        self.assertEqual(funcs.hypotenuse(4, 5), 0.0)
        pass

    def test_is_positive(self):
        self.assertTrue(funcs.is_positive(2), True)
        self.assertFalse(funcs.is_positive(0), False)
        
# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
