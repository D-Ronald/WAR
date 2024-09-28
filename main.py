from fastapi import FastAPI, Response
from src.Jogador import Jogador
from src.Jogo import Jogo
from src.Territorio import Territorio
from src.Cartas import Cartas
from src.Objetivo import Objetivo
import random

cores = [
    'VERMELHO',
    'AZUL',
    'BRANCO',
    'PRETO',
    'AMARELO',
    'VERDE'
]

jogo = Jogo()
jogadores_id = []
cores_escolhidas= []
jogadores = []

app = FastAPI()

@app.post('/criar_jogador', summary='cria jogador', description = 'Escolha a cor escrevendo: "VERMELHO", "AZUL", "BRANCO", "PRETO", "AMARELO" ou "VERDE"')
def criar_jogador(Id: int, cor: str):
    if cor.upper() not in cores:
        return Response("Cor inválida, digite uma cor entre as opções: 'VERMELHO', 'AZUL', 'BRANCO', 'PRETO', 'AMARELO' ou 'VERDE'")
    else:
        
        if Id > 6 or Id <0:
            return Response("Id inválido, digite um id entre 1 e 6")
        else:
            if Id not in jogadores_id:
                if cor not in cores_escolhidas:
                    cores_escolhidas.append(cor)
                    jogador = Jogador(Id)
                    jogador.set_cor_exercito(cor)
                    jogo.jogadores.append(jogador)   
                    jogadores.append(jogador)          
                    jogador.set_cor_exercito(cor)
                    jogadores_id.append(Id)
                    jogo.jogadores_id = jogadores_id
                    
                else:
                    return Response("Cor já escolhida, escolha outra cor")
                return f"Jogador criado com sucesso.", jogador
            else: 
                return Response(f"Jogador com id = {Id} já existe")
    

@app.post('/iniciar_jogo',
          summary='Inicia o jogo',
          description = 'Se já existirem 3 jogadores criados, é realizada a distribuição '
          'dos exércitos, a atribuição de um objetivo para cada jogador, a distribuição '
          'dos territórios e a ordenação dos jogadores, tudo de forma automática, '
          'retornando a lista de jogadores já ordenados com todas as informações.')
def iniciar_jogo():
    if len(jogadores) < 3:
        return Response("Número de jogadores insuficiente, adicione mais jogadores")
    else:
        jogo.iniciar_jogo()
    return jogo.jogadores

@app.post('/definir_ordem')
def definir_ordem():
    ordenar = jogo.ordenar_jogadores() 
    return Response("A ordem de jogadas seguirá a seguinte sequencia de a cordo com o id", )

@app.post('/distribuir_territorios')
def distribuir_territorios(id: int):
    if id in jogadores_id:
        jogo.distribuir_territorios()
        for jogador in jogo.jogadores:
            if jogador.id_jogador == id:
                return "Territórios distribuidos com sucesso", jogador.get_territorios()
    else:
        return f"jogador com id = {id} não existe, tente novamete."

@app.post('/distribuir_objetivos')
def distribuir_objetivos(Id: int):
    if Id in jogadores_id:
        jogo.distribuir_objetivo_jogador(Id)
        for jogador in jogo.jogadores:
            if jogador.id_jogador == Id:
                return f'Objetivo distribuido para o jogador {Id}', jogador.get_objetivo()
    else:
        return 'Jogador não encontrado'

@app.post('/distribuir_exércitos')
def distribuir_exercitos(id:int):
    if id in jogadores_id:
        jogo.distribuir_exercitos()
        for jogador in jogo.jogadores:
            if jogador.id_jogador == id:
                return "Exércitos distribuidos com sucesso", jogador.get_exercitos()
    else:
        return f"jogador com id = {id} não existe, tente novamete."

@app.post('/exibir_jogador')
def exibir_jogador(id: int):
    if id in jogo.jogadores_id:
        for jogador in jogo.jogadores:
            if jogador.get_id_jogador() == id:
                return jogador
    else:
        return 'Jogador não encontrado'