import unittest

from tarea_45.nivel_1_tarea_45 import sequential_search


class Tarea45TestCase(unittest.TestCase):
    def test_sequential_search(self):
        iterable = [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
        search_value = 874
        self.assertEqual(4, sequential_search(iterable, search_value))

    def test_binary_search(self):
        iterable = [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
        search_value = 874
        self.assertEqual(4, sequential_search(iterable, search_value))


if __name__ == '__main__':
    unittest.main()
