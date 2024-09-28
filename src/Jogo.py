from typing import List
import random
from src.Jogador import Jogador
from src.Territorio import Territorio
from src.Exercito import Exercito
from src.Objetivo import Objetivo
from src.Cartas import Cartas

cartas_objetivo = [
    Cartas('Você deve conquistar toda a Europa.', 'objetivo'),
    Cartas('Você deve conquistar toda a Ásia e a América do Sul.', 'objetivo'),
    Cartas('Você deve conquistar toda a América do Norte e a África.', 'objetivo'),
    Cartas('Você deve conquistar toda a América do Sul e 18 territórios à sua escolha.', 'objetivo'),
    Cartas('Você deve conquistar toda a Oceania e 18 territórios à sua escolha.', 'objetivo'),
    Cartas('Você deve conquistar toda a América do Norte e a Oceania.', 'objetivo'),
    Cartas('Você deve conquistar toda a Europa, a América do Sul e um território da Ásia.', 'objetivo'),
    Cartas('Você deve destruir as forças vermelhas.', 'objetivo'),
    Cartas('Você deve destruir as forças amarelas.', 'objetivo'),
    Cartas('Você deve destruir as forças azuis.', 'objetivo'),
    Cartas('Você deve destruir as forças pretas.', 'objetivo'),
    Cartas('Você deve destruir as forças verdes.', 'objetivo'),
    Cartas('Você deve conquistar 24 territórios à sua escolha.', 'objetivo'),
    Cartas('Você deve conquistar 18 territórios e deixar dois exércitos em cada um.', 'objetivo'),
    Cartas('Você deve conquistar 2 continentes à sua escolha.', 'objetivo')
]
cartas_territorio = [
    
    Cartas('Brasil', 'Território'),
    Cartas('Estados Unidos', 'Território'),
    Cartas('Canadá', 'Território'),
    Cartas('Argentina', 'Território'),
    Cartas('França', 'Território'),
    Cartas('Alemanha', 'Território'),
    Cartas('África do Sul', 'Território'),
    Cartas('Egito', 'Território'),
    Cartas('Austrália', 'Território'),
    Cartas('China', 'Território'),
    Cartas('Japão', 'Território'),
    Cartas('Índia', 'Território'),
    Cartas('México', 'Território'),
    Cartas('Itália', 'Território'),
    Cartas('Reino Unido', 'Território'),
    
]

objetivos = [
    Objetivo(status='a concluir', descricao='Você deve conquistar toda a Europa.'),
    Objetivo(status='a concluir', descricao='Você deve conquistar toda a Ásia e a América do Sul.'),
    Objetivo(status='a concluir', descricao='Você deve conquistar toda a América do Norte e a África.'),
    Objetivo(status='a concluir', descricao='Você deve conquistar toda a América do Sul e 18 territórios à sua escolha.'),
    Objetivo(status='a concluir', descricao='Você deve conquistar toda a Oceania e 18 territórios à sua escolha.'),
    Objetivo(status='a concluir', descricao='Você deve conquistar toda a América do Norte e a Oceania.'),
    Objetivo(status='a concluir', descricao='Você deve conquistar toda a Europa, a América do Sul e um território da Ásia.'),
    Objetivo(status='a concluir', descricao='Você deve destruir as forças vermelhas.'),
    Objetivo(status='a concluir', descricao='Você deve destruir as forças amarelas.'),
    Objetivo(status='a concluir', descricao='Você deve destruir as forças azuis.'),
    Objetivo(status='a concluir', descricao='Você deve destruir as forças pretas.'),
    Objetivo(status='a concluir', descricao='Você deve destruir as forças verdes.'),
    Objetivo(status='a concluir', descricao='Você deve conquistar 24 territórios à sua escolha.'),
    Objetivo(status='a concluir', descricao='Você deve conquistar 18 territórios e deixar dois exércitos em cada um.'),
    Objetivo(status='a concluir', descricao='Você deve conquistar 2 continentes à sua escolha.')

]

territorios = [
    Territorio(cartas_territorio[0], None, 0, [cartas_territorio[1],cartas_territorio[5]]),
    Territorio(cartas_territorio[1], None, 0, [cartas_territorio[2],cartas_territorio[3]]),
    Territorio(cartas_territorio[2], None, 0, [cartas_territorio[5],cartas_territorio[6]]),
    Territorio(cartas_territorio[3], None, 0, [cartas_territorio[4],cartas_territorio[9]]),
    Territorio(cartas_territorio[4], None, 0, [cartas_territorio[10]]),
    Territorio(cartas_territorio[4], None, 0, [cartas_territorio[11],cartas_territorio[7]]),
    Territorio(cartas_territorio[5], None, 0, [cartas_territorio[14],cartas_territorio[6]]),
    Territorio(cartas_territorio[6], None, 0, [cartas_territorio[12],cartas_territorio[0],cartas_territorio[10]]),
    Territorio(cartas_territorio[7], None, 0, [cartas_territorio[0]]),
    Territorio(cartas_territorio[8], None, 0, [cartas_territorio[10],cartas_territorio[3]]),
    Territorio(cartas_territorio[9], None, 0, [cartas_territorio[1],cartas_territorio[5]]),
    Territorio(cartas_territorio[10], None, 0, [cartas_territorio[0]]),
    Territorio(cartas_territorio[11], None, 0, [cartas_territorio[7],cartas_territorio[2],cartas_territorio[8]]),
    Territorio(cartas_territorio[12], None, 0, [cartas_territorio[1],cartas_territorio[6]]),
    Territorio(cartas_territorio[13], None, 0, [cartas_territorio[10],cartas_territorio[5]]),
    Territorio(cartas_territorio[14], None, 0, [cartas_territorio[8],cartas_territorio[2]])
               ]

class Jogo:
    _instance = None  

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Jogo, cls).__new__(cls)
        return cls._instance

    def __init__(self, turno_atual: int = 0):
        if not hasattr(self, "initialized"):  
            self.jogadores = []
            self.turno_atual = turno_atual
            self.territorios = territorios
            self.jogadores_id = []
            self.objetivos = objetivos
            self.initialized = True  # Inicializa o objeto

    def iniciar_jogo(self):
        self.ordenar_jogadores()    
        self.distribuir_territorios()
        self.distribuir_exercitos()
        self.distribuir_objetivos_jogadores()# Distribui os objetivos aos jogadores

    def ordenar_jogadores(self):
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
            if territorio.jogador == jogador.get_id_jogador():
                jogador.set_territorios(territorio)

    def distribuir_objetivo_jogador(self, jogador_id):
        if len(self.objetivos) < len(self.jogadores):
            raise ValueError("Não há objetivos suficientes para todos os jogadores.")

        for jogador in self.jogadores:
            if jogador.get_id_jogador() == jogador_id:
                jogador.set_objetivo(self.objetivos[random.randint(0,len(self.objetivos)-1)])
                
    def distribuir_objetivos_jogadores(self):
        for jogador in self.jogadores:
            self.distribuir_objetivo_jogador(jogador.get_id_jogador())

    def avancar_turno(self):
        self.turno_atual += 1

    def adicionar_territorio(self, territorio: Territorio):
        self.territorios.append(territorio)
