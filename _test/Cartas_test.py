import unittest
from src.Cartas import Cartas

class TestCartas(unittest.TestCase):
    def setUp(self):
        self.carta = Cartas("Descrição", "Tipo")

    def test_get_descricao(self):
        self.assertEqual(self.carta.get_descricao(), "Descrição")

    def test_set_descricao(self):
        self.carta.set_descricao("Nova Descrição")
        self.assertEqual(self.carta.get_descricao(), "Nova Descrição")

    def test_get_tipo(self):
        self.assertEqual(self.carta.get_tipo(), "Tipo")

    def test_set_tipo(self):
        self.carta.set_tipo("Novo Tipo")
        self.assertEqual(self.carta.get_tipo(), "Novo Tipo")

    def test_trocar_carta(self):
        self.carta.trocar_carta("Carta de ataque", "Ataque")
        self.assertEqual(self.carta.get_descricao(), "Carta de ataque")
        self.assertEqual(self.carta.get_tipo(), "Ataque")

if __name__ == '__main__':
    unittest.main()