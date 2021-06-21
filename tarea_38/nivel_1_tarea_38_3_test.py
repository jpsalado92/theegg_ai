import unittest

from tarea_38.nivel_1_tarea_38_3 import is_prime, is_palindrome, get_closest_higher_or_equal_prime_palindrome_number


class Tarea383TestCase(unittest.TestCase):

    def test_is_prime(self):
        self.assertEqual(False, is_prime(10))
        self.assertEqual(False, is_prime(50))
        self.assertEqual(False, is_prime(56187165417842))
        self.assertEqual(True, is_prime(1009))
        self.assertEqual(True, is_prime(10007))
        self.assertEqual(True, is_prime(100003))

    def test_is_palindrome(self):
        self.assertEqual(False, is_palindrome(456))
        self.assertEqual(False, is_palindrome(5511555))
        self.assertEqual(False, is_palindrome(1231233213215))
        self.assertEqual(True, is_palindrome(111))
        self.assertEqual(True, is_palindrome(110011))
        self.assertEqual(True, is_palindrome(101))

    def test_get_closest_higher_or_equal_prime_palindrome_number(self):
        self.assertEqual(1003001, get_closest_higher_or_equal_prime_palindrome_number(456789))
        self.assertEqual(101, get_closest_higher_or_equal_prime_palindrome_number(31))


if __name__ == '__main__':
    unittest.main()
