import unittest

from tarea_38.nivel_1_tarea_38_2 import reverse_words


class Tarea382TestCase(unittest.TestCase):

    def test_reverse_words(self):
        self.assertEqual("fa do sol re la mi si", reverse_words("si mi la re sol do fa"))
        self.assertEqual("test a is this", reverse_words("this is a test"))
        self.assertEqual("foobar", reverse_words("foobar"))
        self.assertEqual("base your all", reverse_words("all your base"))


if __name__ == '__main__':
    unittest.main()
