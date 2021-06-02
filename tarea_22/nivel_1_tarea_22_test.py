"""
# Unittest para tarea_24
# Autor: Juan Pablo Salado
# Realizado: 2021-05-16

Básicamente probamos que para las entradas dadas se den los outputs esperados, basándonos en el apartado `Entradas y
salidas de ejemplo` de la referencia del ejercicio en http://www.nachocabanes.com/retos/reto.php?n=07
"""

import unittest

from nivel_1_tarea_22 import find_best_set


class Tarea22TestCase(unittest.TestCase):
    def test_output_sample_a(self):
        max_cap = 700
        item_list = [('1', 360, 40), ('2', 250, 35), ('3', 400, 43), ('4', 180, 28), ('5', 50, 12), ('6', 90, 13)]
        find_best_set(item_list, max_cap)
        self.assertEqual(93, find_best_set(item_list, max_cap)[0])

    def test_output_sample_b(self):
        max_cap = 1000
        item_list = [('1', 223, 30), ('2', 243, 34), ('3', 100, 28), ('4', 200, 45), ('5', 200, 31), ('6', 155, 50),
                     ('7', 300, 29), ('8', 150, 1)]
        find_best_set(item_list, max_cap)
        self.assertEqual(188, find_best_set(item_list, max_cap)[0])

    def test_output_sample_c(self):
        max_cap = 2000
        item_list = [('1', 340, 45), ('2', 355, 50), ('3', 223, 34), ('4', 243, 39), ('5', 130, 29), ('6', 240, 40),
                     ('7', 260, 30), ('8', 155, 52), ('9', 302, 31), ('10', 130, 1)]
        find_best_set(item_list, max_cap)
        self.assertEqual(320, find_best_set(item_list, max_cap)[0])


if __name__ == '__main__':
    unittest.main()
