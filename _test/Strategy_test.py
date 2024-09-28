import unittest
from src.Jogador import Jogador
from src.Territorio import Territorio
from src.Exercito import Exercito
from src.Objetivo import Objetivo
from src.Jogador import EstrategiaAtaque, EstrategiaMoverExercito, EstrategiaDefesa  

class TestEstrategias(unittest.TestCase):

    def setUp(self):
        self.jogador1 = Jogador(1)
        self.jogador2 = Jogador(2)
        self.jogador1.set_territorios('Territorio A')
        self.jogador1.set_territorios('Territorio B')
        self.jogador2.set_territorios('Territorio C')
        self.jogador2.set_territorios('Territorio D')

    def test_estrategia_ataque(self):
        estrategia_ataque = EstrategiaAtaque()

        # Teste de ataque válido
        resultado = estrategia_ataque.executar(self.jogador1, self.jogador2, 'Territorio A', 'Territorio C', 5)
        self.assertEqual(resultado, 'Apto para atacar')

        # Teste de ataque em território próprio
        resultado = estrategia_ataque.executar(self.jogador1, self.jogador1, 'Territorio A', 'Territorio B', 5)
        self.assertEqual(resultado, 'Você não pode atacar seus próprios territórios')

        # Teste de territórios inválidos
        resultado = estrategia_ataque.executar(self.jogador1, self.jogador2, 'Territorio A', 'Territorio B', 5)
        self.assertEqual(resultado, 'Territórios inválidos para ataque')

    def test_estrategia_mover_exercito(self):
        estrategia_mover = EstrategiaMoverExercito()

        # Teste de movimentação válida
        resultado = estrategia_mover.executar(self.jogador1, 'Territorio A', 'Territorio B', 5)
        self.assertEqual(resultado, 'Movendo 5 exércitos de Territorio A para Territorio B')

        # Teste de territórios inválidos
        resultado = estrategia_mover.executar(self.jogador1, 'Territorio A', 'Territorio C', 5)
        self.assertEqual(resultado, 'Territórios inválidos para movimentação')

    def test_estrategia_defesa(self):
        estrategia_defesa = EstrategiaDefesa()

        # Teste de defesa válida
        resultado = estrategia_defesa.executar(self.jogador1, 'Territorio A')
        self.assertEqual(resultado, 'Defendendo o território Territorio A')

        # Teste de defesa em território que não pertence ao jogador
        resultado = estrategia_defesa.executar(self.jogador1, 'Territorio C')
        self.assertEqual(resultado, 'Território não pertence ao jogador')

if __name__ == '__main__':
    unittest.main()
