import unittest

set_secundaria = {'Pocoyo', 'Eddy', 'Pocotú', 'Tacatabro', 'Heiachi', 'Paco'}
set_primaria = {'Mr.Jagger', 'Jin', 'Paco', 'Eddy', 'Paul', 'Lei', 'Law', 'Mr.Worlwide', 'Heiachi'}


class Tarea522TestCase(unittest.TestCase):

    def test_set_intersection(self):
        self.assertEqual({'Heiachi', 'Paco', 'Eddy'}, set_primaria.intersection(set_secundaria))

    def test_set_difference(self):
        self.assertEqual({'Paul', 'Law', 'Lei', 'Mr.Worlwide', 'Jin', 'Mr.Jagger'},
                         set_primaria.difference(set_secundaria))


if __name__ == '__main__':
    unittest.main()
