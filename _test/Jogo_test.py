import unittest
from src.Jogo import Jogo
from src.Jogador import Jogador
from src.Territorio import Territorio
from src.Exercito import Exercito
from src.Objetivo import Objetivo
from src.Cartas import Cartas

class TestJogo(unittest.TestCase):
    def setUp(self):
        # Configuração inicial para os testes
        self.jogador1 = Jogador(id_jogador="Jogador1")
        self.jogador2 = Jogador(id_jogador="Jogador2")
        self.jogo = Jogo(jogadores=[self.jogador1, self.jogador2])  # A primeira instância de Jogo é criada aqui

        carta_territorio1 = Cartas(tipo="Território", descricao="Território 1")
        carta_territorio2 = Cartas(tipo="Território", descricao="Território 2")

        self.territorio1 = Territorio(carta=carta_territorio1, jogador=None, qnt_exercitos=0, vizinhos=[])
        self.territorio2 = Territorio(carta=carta_territorio2, jogador=None, qnt_exercitos=0, vizinhos=[])

        self.jogo.adicionar_territorio(self.territorio1)
        self.jogo.adicionar_territorio(self.territorio2)

    def tearDown(self):
       
        Jogo._instance = None

    def test_singleton_instance(self):
        # Testa se o Singleton está funcionando corretamente
        jogo2 = Jogo(jogadores=[self.jogador1, self.jogador2])
        self.assertIs(self.jogo, jogo2)  

    def test_set_territorios(self):
        jogador = Jogador('123')
        carta_territorio = Cartas(tipo="Território", descricao="Brasil")
        territorio = Territorio(carta=carta_territorio, jogador=jogador.get_id_jogador(), qnt_exercitos=0, vizinhos=[])
        self.assertEqual(territorio.get_nome(), "Brasil")
        self.assertEqual(territorio.get_jogador(), jogador.get_id_jogador())
        self.assertEqual(territorio.get_qnt_exercitos(), 0)
        self.assertEqual(territorio.get_vizinhos(), [])

    def test_iniciar_jogo(self):
        self.jogo.iniciar_jogo()
        self.assertEqual(self.jogo.turno_atual, 0)
        self.assertTrue(any(jogador.get_exercitos() for jogador in self.jogo.jogadores))

    def test_distribuir_territorios(self):
        self.jogo.distribuir_territorios()
        self.assertEqual(self.territorio1.get_jogador(), self.jogador1.get_id_jogador())
        self.assertEqual(self.territorio2.get_jogador(), self.jogador2.get_id_jogador())

    def test_avancar_turno(self):
        self.jogo.avancar_turno()
        self.assertEqual(self.jogo.turno_atual, 1)

if __name__ == "__main__":
    unittest.main()
