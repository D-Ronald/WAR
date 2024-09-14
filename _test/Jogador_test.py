from src.Jogador import Jogador 
from src.Territorio import Territorio
from src.Exercito import Exercito
from src.Cartas import Cartas  # Certifique-se de importar a classe Cartas
import unittest

class TestJogador(unittest.TestCase):
    
    def test_new_player(self):
        self.player = Jogador('123')
        assert self.player.get_id_jogador() == '123'
        
    def test_set_objetivo(self):
        self.objetivo = "dominar a europa"
        self.jogador = Jogador('123')
        self.jogador.set_objetivo(self.objetivo)
        assert self.jogador.get_objetivo() == self.objetivo
        
    def test_set_territorios(self):
        self.jogador = Jogador('123')
        self.qnt_exercitos=0
        self.vizinhos=[]
        
        self.carta_territorio1 = Cartas(tipo="Território", descricao="Brasil")
        self.carta_territorio2 = Cartas(tipo="Território", descricao="Suk")
        self.carta_territorio3 = Cartas(tipo="Território", descricao="Argentina")
        
        self.territorio1 = Territorio(carta= self.carta_territorio1, jogador= self.jogador.get_id_jogador(), qnt_exercitos = self.qnt_exercitos, vizinhos = self.vizinhos)
        self.territorio2 = Territorio(carta= self.carta_territorio2, jogador= self.jogador.get_id_jogador(), qnt_exercitos = self.qnt_exercitos, vizinhos = self.vizinhos)
        self.territorio3 = Territorio(carta= self.carta_territorio3, jogador= self.jogador.get_id_jogador(), qnt_exercitos = self.qnt_exercitos, vizinhos = self.vizinhos)
        
        self.jogador.set_territorios(self.territorio1)
        self.jogador.set_territorios(self.territorio2)
        
        assert self.jogador.get_territorios() == [self.territorio1, self.territorio2]
        assert self.jogador.get_territorios() != [self.territorio2, self.territorio3]

    def test_set_exercitos(self):
        self.jogador = Jogador('123')
        self.exercito_a = Exercito('white', 2)
        self.exercito_b = Exercito('white', 1)
        self.exercito_c = Exercito('white', 1)
        self.jogador.set_exercitos(self.exercito_a)
        self.jogador.set_exercitos(self.exercito_b)
        assert self.jogador.get_exercitos() == [self.exercito_a, self.exercito_b]
        assert self.jogador.get_exercitos() != [self.exercito_b, self.exercito_c]
        
    def test_set_cor_exercito(self):
        self.jogador = Jogador('123')
        self.cor = 'white'
        self.jogador.set_cor_exercito(self.cor)
        assert self.jogador.get_cor_exercito() == self.cor
        assert self.jogador.get_cor_exercito() != 'black'
        assert len(self.jogador.get_cor_exercito()) == len(self.cor)

if __name__ == '__main__':
    unittest.main()