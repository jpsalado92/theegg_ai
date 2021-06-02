"""
# Solución de tarea_21
# Autor: Juan Pablo Salado
# Fecha creación: 2021-05-08
# Fecha última revisión: 2021-06-02

Testing: Comprobar que ante ciertos inputs los outputs son los esperados.
"""
import unittest

from nivel_1_tarea_21 import validate_input, get_fraction


class Tarea21TestCase(unittest.TestCase):
    def test_valores_fuera_de_rango(self):
        """Comprueba que los valores fuera de rango sean invalidados"""
        self.assertEqual(False, validate_input(5.0))

    def test_valores_limite(self):
        """Comprueba que los valores límites funcionen correctamente"""
        self.assertEqual(True, validate_input(0.9999))
        self.assertEqual(True, validate_input(0.0001))

    def test_valores_tipo(self):
        """Comprueba el comportamiento ante distintos formatos de entrada"""
        self.assertEqual(False, validate_input(False))
        self.assertEqual(False, validate_input("String"))
        self.assertEqual(True, validate_input("0.005"))
        self.assertEqual(False, validate_input("1"))

    def test_valores_formato(self):
        """Comprueba que no vengan decimales de más"""
        self.assertEqual(False, validate_input(0.00001))
        self.assertEqual(False, validate_input(0.99999))

    def test_fracciones(self):
        """Comprueba que el resultado de las fracciones es el esperado"""
        self.assertEqual('1/4', get_fraction(0.25))
        self.assertEqual('1/2', get_fraction(0.5))
        self.assertEqual('1/10000', get_fraction(0.0001))
        self.assertEqual('9999/10000', get_fraction(0.9999))
        self.assertEqual('41152/218107', get_fraction(0.1886780341758861476247896674568))


if __name__ == '__main__':
    unittest.main()
