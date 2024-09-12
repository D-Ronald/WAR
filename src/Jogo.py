from typing import List
from src.Jogador import Jogador
from src.Territorio import Territorio
from src.Exercito import Exercito
from src.Objetivo import Objetivo

class Jogo:
    def __init__(self, jogadores: List[Jogador], turno_atual: int = 0):
        self.jogadores = jogadores
        self.turno_atual = turno_atual
        self.territorios = []

    def iniciar_jogo(self):
        self.ordenar_jogadores()
        self.distribuir_territorios()
        self.distribuir_exercitos()

    def ordenar_jogadores(self):
        import random
        random.shuffle(self.jogadores)

    def distribuir_exercitos(self):
        for jogador in self.jogadores:
            jogador.set_exercitos(Exercito(jogador.get_cor_exercito(), 10))

    def distribuir_territorios(self):
        num_territorios = len(self.territorios)
        num_jogadores = len(self.jogadores)

        if num_jogadores == 0:
            raise ValueError("Não há jogadores para distribuir territórios.")

        for i, territorio in enumerate(self.territorios):
            jogador = self.jogadores[i % num_jogadores]
            territorio.set_jogador(jogador.get_id_jogador())
            jogador.set_territorios(territorio)

    def avancar_turno(self):
        self.turno_atual += 1

    def adicionar_territorio(self, territorio: Territorio):
        self.territorios.append(territorio)
