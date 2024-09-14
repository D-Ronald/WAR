from fastapi import FastAPI, Response
from src.Jogador import Jogador
from src.Jogo import Jogo
from src.Territorio import Territorio
from src.Cartas import Cartas
from src.Objetivo import Objetivo

cores = [
    'VERMELHO',
    'AZUL',
    'BRANCO',
    'PRETO',
    'AMARELO',
    'VERDE'
]

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

jogo = Jogo([], 0)
jogo.territorios = territorios
global jogadores_id
jogadores_id = []
jogadores = []

app = FastAPI()

@app.post('/criar_jogador', summary='cria jogador', description = 'Escolha a cor escrevendo: "VERMELHO", "AZUL", "BRANCO", "PRETO", "AMARELO" ou "VERDE"')
def criar_jogador(Id: int, cor: str):
    if cor.upper() not in cores:
        return Response("Cor inválida, digite uma cor entre as opções: 'VERMELHO', 'AZUL', 'BRANCO', 'PRETO', 'AMARELO' ou 'VERDE'")
    else:
        cores.append(cor)
        if Id > 6 or Id <0:
            return Response("Id inválido, digite um id entre 1 e 6")
        else:
            if Id not in jogadores_id:
                jogador = Jogador(Id)
                jogo.jogadores.append(jogador)   
                jogadores.append(jogador)          
                jogador.set_cor_exercito(cor)
                jogadores_id.append(Id)
                jogo.jogadores_id = jogadores_id
                
                return Response(f"Jogador criado com sucesso, {len(jogadores)}")
            else: 
                return Response("Jogador já existe")

@app.post('/iniciar_jogo')
def iniciar_jogo():
    jogo.iniciar_jogo()
    return Response("Jogo iniciado")

@app.post('/definir_ordem')
def definir_ordem():
    ordenar = jogo.ordenar_jogadores() 
    return Response("A ordem de jogadas seguirá a seguinte sequencia de a cordo com o id", )

@app.post('/distribuir_territorios')
def distribuir_territorios():
    jogo.distribuir_territorios()
    return Response(f'{jogo.jogadores[0].get_territorios()}')

@app.post('/distribuir_objetivos')
def distribuir_objetivos():
    for jogador in jogo.jogadores:
        jogador.set_objetivo(objetivos[jogador.get_id_jogador()])
    return Response(jogo.jogadores[0].get_objetivo())

@app.post('/distribuir_exércitos')
def distribuir_exercitos():
    jogo.distribuir_exercitos()
    return Response('os exércitos foram distribuídos')