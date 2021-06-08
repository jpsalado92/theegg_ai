import unittest

from nivel_1_tarea_52_1 import get_frequency_list, filter_list, get_val_and_remove_if_exist


class Tarea521TestCase(unittest.TestCase):
    def test_get_frequency_list_as_in_example(self):
        input_list = [5, 16, 2, 5, 57, 5, 2]
        freq_list = get_frequency_list(input_list)
        self.assertEqual([(5, 3), (2, 2), (16, 1), (57, 1)], freq_list)

    def test_get_frequency_list_unique_elements(self):
        input_list = [5, 5, 5, 5, 5, 5, 5]
        freq_list = get_frequency_list(input_list)
        self.assertEqual([(5, 7)], freq_list)

    def test_get_frequency_list(self):
        input_list = [1]
        freq_list = get_frequency_list(input_list)
        self.assertEqual([(1, 1)], freq_list)

    def test_filter_list(self):
        input_list = [1, 2, 3, 4, 5, 6]
        filtered_list = filter_list(input_list, 4)
        self.assertEqual([1, 2, 3], filtered_list)

    def test_get_val_and_remove_if_exists(self):
        input_list = [1, 2, 3, 4, 5, 6]
        input_value = 2
        get_val_and_remove_if_exist(input_list, input_value)
        self.assertEqual([1, 3, 4, 5, 6], input_list)


if __name__ == '__main__':
    unittest.main()
