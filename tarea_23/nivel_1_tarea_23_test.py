"""
# Solución de tarea_23
# Autor: Juan Pablo Salado
# Fecha creación: 2021-05-15
# Fecha última revisión: 2021-06-02

Testing: Comprobar que ante ciertos inputs los outputs son los esperados.
"""
import unittest

from nivel_1_tarea_23 import normalize_text, get_value_from_letter, get_letter_from_value, PokerDeck, codificador, \
    decodificador, format_text


class Tarea23TestCase(unittest.TestCase):

    def test_normalize_text(self):
        self.assertEqual(normalize_text("Érase ,.!?-@()12345678\\/9\n una vez un 123 año...!?"), 'ERASEUNAVEZUNANO')

    def test_format_text(self):
        self.assertEqual(['DONOT', 'REPEA', 'TYOUR', 'SELFX'], format_text(normalize_text("Do not repeat yourself")))

    def test_get_value_from_letter(self):
        self.assertEqual(1, get_value_from_letter('A'))
        self.assertEqual(26, get_value_from_letter('Z'))

    def test_get_letter_from_value(self):
        self.assertEqual('A', get_letter_from_value(1))
        self.assertEqual('Z', get_letter_from_value('26'))

    def test_codificador(self):
        emisor_test_deck = PokerDeck(1)
        coded_text = codificador("Do not repeat yourself", emisor_test_deck)
        self.assertEqual(['BIMIC', 'GIJFS', 'YAVBB', 'HMRLU'], coded_text)

    def test_decodificador_success(self):
        """Testar situación en la que ambas terminaciones tienen el mismo mazo"""
        emisor_test_deck = PokerDeck(1)
        receptor_test_deck = PokerDeck(1)
        coded_text = codificador("Do not repeat yourself", emisor_test_deck)
        decoded_text = decodificador(coded_text, receptor_test_deck)
        self.assertEqual(['DONOT', 'REPEA', 'TYOUR', 'SELFX'], decoded_text)

    def test_decodificador_failure(self):
        """Testar situación en la que ambas terminaciones no tienen el mismo mazo"""
        emisor_test_deck = PokerDeck(1)
        receptor_test_deck = PokerDeck(2)
        coded_text = codificador("Do not repeat yourself", emisor_test_deck)
        decoded_text = decodificador(coded_text, receptor_test_deck)
        self.assertNotEqual(['DONOT', 'REPEA', 'TYOUR', 'SELFX'], decoded_text)


if __name__ == '__main__':
    unittest.main()
