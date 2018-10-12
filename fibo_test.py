import unittest
from fibo_fct import fibonacci


class fibo_test(unittest.TestCase):

    def test_1st_fibo(self):
            self.assertEqual(fibonacci(5), 5)

    def test_2nd_fibo(self):
            self.assertEqual(fibonacci(6), 8)


if __name__ == '__name__':
    unittest.main()