import unittest

from tarea_38.nivel_1_tarea_38_1 import get_major_common_substring


class Tarea381TestCase(unittest.TestCase):

    def test_get_major_common_substring(self):
        self.assertEqual("CTTCCT", get_major_common_substring("ATGTCTTCCTCGA", "TGCTTCCTATGAC"))
        self.assertEqual("actga", get_major_common_substring("ctgactga", "actgagc"))
        self.assertEqual("cgta", get_major_common_substring("cgtaattgcgat", "cgtacagtagc"))
        self.assertEqual("actg", get_major_common_substring("ctgggccttgaggaaaactg", "gtaccagtactgatagt"))
        self.assertEqual("ola", get_major_common_substring("hola", "ola"))


if __name__ == '__main__':
    unittest.main()
