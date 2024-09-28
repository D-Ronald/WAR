import unittest
from src.Cartas import Cartas
from src.FactoryCartas import FactoryCartas

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


    def test_criar_carta_objetivo(self):
        carta = FactoryCartas.criar_carta("objetivo", descricao="Conquistar 18 territórios")
        self.assertEqual(carta.get_descricao(), "Conquistar 18 territórios")
        self.assertEqual(carta.get_tipo(), "Objetivo")

    def test_criar_carta_territorio(self):
        carta = FactoryCartas.criar_carta("territorio", territorio="Brasil")
        self.assertEqual(carta.get_descricao(), "Território: Brasil")
        self.assertEqual(carta.get_tipo(), "Território")

    def test_criar_carta_bonus(self):
        carta = FactoryCartas.criar_carta("bonus", bonus=10)
        self.assertEqual(carta.get_descricao(), "Receba 10 exércitos")
        self.assertEqual(carta.get_tipo(), "Bônus")

    def test_criar_carta_invalida(self):
        with self.assertRaises(ValueError):  
            FactoryCartas.criar_carta("invalido")


if __name__ == '__main__':
    unittest.main()