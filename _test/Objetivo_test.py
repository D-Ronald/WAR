import unittest
from io import StringIO
import sys
from src.Objetivo import Objetivo
from src.Cartas import Cartas

class TestObjetivo(unittest.TestCase):
    def setUp(self):
        self.objetivo = Objetivo("Em progresso", "Complete a missão")
        self.carta_objetivo = Cartas("Descrição - Carta de objetivo", "Objetivo")
        self.carta_ataque = Cartas("Descrição - Carta de ataque", "Ataque")

        
        self.log = StringIO()
        sys.stdout = self.log

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_set_carta_valida(self):
        self.objetivo.set_carta(self.carta_objetivo)
        self.assertEqual(self.objetivo.get_carta(), self.carta_objetivo)

    def test_set_carta_invalida(self):
        with self.assertRaises(ValueError) as context:
            self.objetivo.set_carta(self.carta_ataque)
        self.assertEqual(str(context.exception), "A carta associada deve ser do tipo 'Objetivo'.")

    def test_verificar_progresso(self):
        self.objetivo.set_carta(self.carta_objetivo)
        self.objetivo.verificar_progresso()
        self.log.seek(0)  # Volta ao início do StringIO para leitura
        self.assertIn("Objetivo: Complete a missão", self.log.getvalue())
        self.assertIn("Carta associada: Descrição - Carta de objetivo", self.log.getvalue())


if __name__ == '__main__':
    unittest.main()