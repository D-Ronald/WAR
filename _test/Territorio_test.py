import unittest
from io import StringIO
import sys
from src.Territorio import Territorio
from src.Cartas import Cartas

class TestTerritorio(unittest.TestCase):
    def setUp(self):
        self.carta_territorio = Cartas("Nome do Território", "Território")
        self.territorio = Territorio(self.carta_territorio, "Jogador 1", 5, ["Território A", "Território B"])
        
        self.log = StringIO()
        sys.stdout = self.log

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_criacao_territorio_valido(self):
        self.assertEqual(self.territorio.get_nome(), "Nome do Território")
        self.assertEqual(self.territorio.get_jogador(), "Jogador 1")
        self.assertEqual(self.territorio.get_qnt_exercitos(), 5)
        self.assertEqual(self.territorio.get_vizinhos(), ["Território A", "Território B"])

    def test_adicionar_exercitos(self):
        self.territorio.adicionar_exercitos(3)
        self.assertEqual(self.territorio.get_qnt_exercitos(), 8)

    def test_remover_exercitos(self):
        self.territorio.remover_exercitos(2)
        self.assertEqual(self.territorio.get_qnt_exercitos(), 3)

    def test_remover_exercitos_excedente(self):
        with self.assertRaises(ValueError) as context:
            self.territorio.remover_exercitos(10)
        self.assertEqual(str(context.exception), "Não há tropas suficientes para remover.")

    def test_set_nome(self):
        self.territorio.set_nome("Novo Nome")
        self.assertEqual(self.territorio.get_nome(), "Novo Nome")

    def test_set_jogador(self):
        self.territorio.set_jogador("Jogador 2")
        self.assertEqual(self.territorio.get_jogador(), "Jogador 2")

    def test_set_qnt_exercitos(self):
        self.territorio.set_qnt_exercitos(7)
        self.assertEqual(self.territorio.get_qnt_exercitos(), 7)
    
    def test_set_qnt_exercitos_negativo(self):
        with self.assertRaises(ValueError) as context:
            self.territorio.set_qnt_exercitos(-3)
        self.assertEqual(str(context.exception), "A quantidade de exércitos não pode ser negativa.")

    def test_set_vizinhos(self):
        self.territorio.set_vizinhos(["Território C", "Território D"])
        self.assertEqual(self.territorio.get_vizinhos(), ["Território C", "Território D"])

    def test_set_carta_invalida(self):
        carta_invalida = Cartas("Descrição - Carta de ataque", "Ataque")
        with self.assertRaises(ValueError) as context:
            Territorio(carta_invalida, "Jogador 1", 5, ["Território A"])
        self.assertEqual(str(context.exception), "A carta associada deve ser do tipo 'Território'.")

if __name__ == '__main__':
    unittest.main()