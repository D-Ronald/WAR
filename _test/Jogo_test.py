import unittest
from src.Jogador import Jogador
from src.Territorio import Territorio
from src.Exercito import Exercito
from src.Objetivo import Objetivo
from src.Cartas import Cartas
from src.Jogo import Jogo  

class TestJogo(unittest.TestCase):

    def setUp(self):
        self.jogo = Jogo()
        self.jogador1 = Jogador(1)
        self.jogador1.cor_exercito = 'PRETO'
        self.jogador2 = Jogador(2)
        self.jogador2.cor_exercito = 'BRANCO'
        self.jogador3 = Jogador(3)
        self.jogador3.cor_exercito = 'VERDE'
        self.jogo.jogadores = [self.jogador1, self.jogador2]
        
    def tearDown(self):
        # Reseta a instância Singleton após cada teste
        Jogo._instance = None

    def test_singleton_instance(self):
        jogo2 = Jogo()
        self.assertIs(self.jogo, jogo2)  # Verifica se as duas instâncias são a mesma

    def test_iniciar_jogo(self):
        self.jogo.iniciar_jogo()
        self.assertEqual(self.jogo.turno_atual, 0)
        self.assertTrue(any(jogador.get_exercitos() for jogador in self.jogo.jogadores)) 

    def test_distribuir_exercitos(self):
        self.jogo.iniciar_jogo()
        for jogador in self.jogo.jogadores:
            self.assertEqual(len(jogador.get_exercitos()), 1) 
            self.assertEqual(jogador.get_exercitos()[0].quantidade, 10) 

    def test_distribuir_objetivos_jogadores(self):
        self.jogo.iniciar_jogo()
        for jogador in self.jogo.jogadores:
            self.assertIsNotNone(jogador.get_objetivo())

    def test_adicionar_territorio(self):
        novo_territorio = Territorio(Cartas('Novo Território', 'Território'), None, 0, [])
        self.jogo.adicionar_territorio(novo_territorio)
        self.assertIn(novo_territorio, self.jogo.territorios) 
    
    def test_avancar_turno(self):
        self.jogo.avancar_turno()
        self.assertEqual(self.jogo.turno_atual, 1)
if __name__ == '__main__':
    unittest.main()
