# Unit tests
import unittest


class TestFibonacci(unittest.TestCase):
    def test_positive_even(self):
        result = fibonacci(4)
        self.assertEqual(result, 3)

    def test_positive_odd(self):
        result = fibonacci(5)
        self.assertEqual(result, 5)

    def test_negative_even(self):
        # result = fibonacci(-6)
        # self.assertEqual(result, 8)
        # self.assertRaises(ValueError)
        with self.assertRaises(ValueError) as ve:
            fibonacci(-6)

        self.assertEqual(str(ve.exception),"Input must be a non-negative integer")

    def test_negative_odd(self):
        with self.assertRaises(ValueError) as ve:
            fibonacci(-7)

        self.assertEqual(str(ve.exception), "Input must be a non-negative integer")

    def test_zero(self):
        result = fibonacci(0)
        self.assertEqual(result, 0)

    def test_one(self):
        result = fibonacci(1)
        self.assertEqual(result, 1)

    def test_invalid_input_string(self):
        with self.assertRaises(ValueError):
            fibonacci("invalid")

    def test_invalid_input_float(self):
        with self.assertRaises(ValueError):
            fibonacci(3.14)

