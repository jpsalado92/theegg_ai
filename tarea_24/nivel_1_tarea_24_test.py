"""
# Solución de tarea_23
# Autor: Juan Pablo Salado
# Fecha creación: 2021-05-15
# Fecha última revisión: 2021-06-02

Testing: Comprobar que ante ciertos inputs los outputs son los esperados.
"""
import unittest

from nivel_1_tarea_24 import convertidor_digital


class Tarea24TestCase(unittest.TestCase):

    def test_convertidor_digital(self):
        self.assertEqual('1', convertidor_digital(1))
        self.assertEqual('1', convertidor_digital(-1))
        self.assertEqual('0', convertidor_digital(0))
        self.assertEqual('10', convertidor_digital(2))
        self.assertEqual('11', convertidor_digital(3))
        self.assertEqual('100', convertidor_digital(4))
        self.assertEqual('101', convertidor_digital(5))
        self.assertEqual('110', convertidor_digital(6))
        self.assertEqual('111', convertidor_digital(7))
        self.assertEqual('11001', convertidor_digital(25))
        self.assertEqual('10111011100', convertidor_digital(1500))


if __name__ == '__main__':
    unittest.main()
