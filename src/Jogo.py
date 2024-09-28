from typing import List
import random
from src.Jogador import Jogador
from src.Territorio import Territorio
from src.Exercito import Exercito
from src.Objetivo import Objetivo

class Jogo:
    _instance = None  # armazena uma unica instancia da classe

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Jogo, cls).__new__(cls)
        return cls._instance

    def __init__(self, jogadores: List[Jogador], objetivos: List[Objetivo], turno_atual: int = 0):
        if not hasattr(self, "initialized"):  # Impede reexecução do __init__
            self.jogadores = jogadores
            self.turno_atual = turno_atual
            self.territorios = []
            self.jogadores_id = []
            self.objetivos = objetivos
            self.initialized = True  # Inicializa o objeto

    def iniciar_jogo(self):
        self.ordenar_jogadores()    
        self.distribuir_territorios()
        self.distribuir_exercitos()
        self.distribuir_objetivos()  # Distribui os objetivos aos jogadores

    def ordenar_jogadores(self):
        random.shuffle(self.jogadores_id)

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

    def distribuir_objetivos(self):
        if len(self.objetivos) < len(self.jogadores):
            raise ValueError("Não há objetivos suficientes para todos os jogadores.")

        random.shuffle(self.objetivos)  # Embaralha a lista de objetivos
        for i, jogador in enumerate(self.jogadores):
            jogador.set_objetivo(self.objetivos[i])  # Atribui um objetivo a cada jogador

    def avancar_turno(self):
        self.turno_atual += 1

    def adicionar_territorio(self, territorio: Territorio):
        self.territorios.append(territorio)
