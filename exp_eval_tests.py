# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    # def test_postfix_eval_01(self):
    #     self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
    #     self.assertAlmostEqual(postfix_eval("25 5 /"), .2)
    #     self.assertAlmostEqual(postfix_eval("2 12 ** 2 -"), -142)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid Token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient Operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too Many Operands")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("15 / 3"), "15 3 /")

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")
        self.assertEqual(prefix_to_postfix("** 5 7"), "5 7 **")

    def test_01postfix_eval_add(self):
        self.assertAlmostEqual(12.0, postfix_eval("12"))
        self.assertAlmostEqual(12.0, postfix_eval("12.0"))

    def test_02_postfix_eval_sub(self):
        self.assertAlmostEqual(-2.0, postfix_eval("5 7 -"))

    def test_03_postfix_eval_mult(self):
        self.assertAlmostEqual(35.0, postfix_eval("5 7 *"))
        self.assertAlmostEqual(35.7, postfix_eval("5.1 7 *"))

    def test_04_postfix_eval_basic_div(self):
        self.assertAlmostEqual(0.714285714, postfix_eval("5 7 /"))

    def test_05_postfix_eval_mixed(self):
        self.assertAlmostEqual(25, postfix_eval("25"))
        self.assertAlmostEqual(1.234, postfix_eval("1.234"))

    def test_06_postfix_eval_complex(self):
        self.assertAlmostEqual(5589.854285714286, postfix_eval("3 2 + 8 3 / 17 * + 12 4.2 / 1.2 / 8 6 * - 6.9 17 * 23 6 / + 2.2 - 3.2 - 56 21 / 1.4 * - 2.3 4.1 * + * -"))
    #
    # def test_07_postfix_eval_test_postfix_exceptions(self):
    #     try:
    #         postfix_eval("99 38 1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - +")
    #

    def test_08_infix_to_postfix_div_(self):
        self.assertEqual("2 3 / 4 / 5 /", infix_to_postfix("2 / 3 / 4 / 5"))

    def test_09_infix_to_postfix_sub(self):
        self.assertEqual("2 3 - 4 - 5 -", infix_to_postfix("2 - 3 - 4 - 5"))

    def test_10_infix_to_postfix_mixed(self):
        self.assertEqual("3 4 + 5 +", infix_to_postfix("3 + 4 + 5"))

    def test_11_infix_to_postfix_mixed(self):
        self.assertEqual("5 4 + 3 - 6 *", infix_to_postfix("( ( ( 5 + 4 ) - 3 ) * 6 )"))

    def test_12_infix_to_postfix_pow(self):
        self.assertEqual("2 3 4 5 ** ** **", infix_to_postfix("2 ** 3 ** 4 ** 5"))
        self.assertEqual("2 3 ** 4 ** 5 **", infix_to_postfix("( ( 2 ** 3 ) ** 4 ) ** 5"))

    def test_13_infix_to_postfix_complex(self):
        self.assertEqual("3 2 + 8 3 / 17 * + 12 4.2 / 1.2 / 8 6 * - 6.9 17 * 23 6 / + 2.2 - 3.2 - 56 21 / 1.4 * - 2.3 4.1 * + * -", infix_to_postfix("( 3 + 2 ) + 8 / 3 * 17 - ( 12 / 4.2 / 1.2 - 8 * 6 ) * ( ( 6.9 * 17 + 23 / 6 - 2.2 ) - 3.2 - ( 56 / 21 * 1.4 ) + 2.3 * 4.1 )"))

    def test_14_infix_to_postfix_complex(self):
        # self.assertEqual("3 2 >> 8 >> 3 / 17 12 4.2 / 1.2 8 << / 6 * << * 6.9 17 23 >> * 6 2.2 << / 3.2 << 56 21 / 1.4 * << 2.3 >> 4.1 * *", infix_to_postfix("( ( 3 >> 2 ) >> 8 ) / 3 * 17 << ( 12 / 4.2 / ( 1.2 << 8 ) * 6 ) * ( ( 6.9 * ( 17 >> 23 ) / ( 6 << 2.2 ) ) << 3.2 << ( 56 / 21 * 1.4 ) >> 2.3 * 4.1 )"))
        self.assertEqual("38 1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - +", infix_to_postfix("( ( ( ( 38 * 1.2 + 3.6 / 2.8 - 6 ) + 3.7 / 2 / 5 - 3 + 23 ) / 1.1 + 2.2 ) - 2.4 / 5 - 1 ) + ( 1.6 / 3 / 9 * 2.8 - 3 - ( 6.2 / 4 + ( 12.8 * 2 / 1.1 - 4.4 / ( 3.2 - 1.1 / 5.2 * 9.9 ) ) ) )"))

    def test_16_prefix_to_postfix_basic(self):
        self.assertEqual(prefix_to_postfix("+ + + 5 -7.1 11 3"), "5 -7.1 + 11 + 3 +")

    def test_17_prefix_to_postfix_complex(self):
        self.assertEqual(prefix_to_postfix("- + + 3 2 * / 8 3 17 * - / / 12 4.2 1.2 * 8 6 + - - - + * 6.9 17 / 23 6 2.2 3.2 * / 56 21 1.4 * 2.3 4.1"),"3 2 + 8 3 / 17 * + 12 4.2 / 1.2 / 8 6 * - 6.9 17 * 23 6 / + 2.2 - 3.2 - 56 21 / 1.4 * - 2.3 4.1 * + * -")

    def test_18_prefix_to_postfix_single_value(self):
        self.assertEqual("25", prefix_to_postfix("25"))
        self.assertEqual("1.234", prefix_to_postfix("1.234"))

    def test_19_postfix_eval_bit_shift(self):
        self.assertEqual(16, postfix_eval('1 4 <<'))


if __name__ == "__main__":
    unittest.main()