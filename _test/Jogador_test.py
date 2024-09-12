from src.Jogador import Jogador 
from src.Territorio import Territorio
from src.Exercito import Exercito
from src.Cartas import Cartas  # Certifique-se de importar a classe Cartas

def test_new_player():
    player = Jogador('123')
    assert player.get_id_jogador() == '123'
    
def test_set_objetivo():
    objetivo = "dominar a europa"
    jogador = Jogador('123')
    jogador.set_objetivo(objetivo)
    assert jogador.get_objetivo() == objetivo
    
def test_set_territorios():
    jogador = Jogador('123')
    
    carta_territorio1 = Cartas(tipo="Território", descricao="Brasil")
    carta_territorio2 = Cartas(tipo="Território", descricao="Suk")
    carta_territorio3 = Cartas(tipo="Território", descricao="Argentina")
    
    territorio1 = Territorio(carta=carta_territorio1, jogador=jogador.get_id_jogador(), qnt_exercitos=0, vizinhos=[])
    territorio2 = Territorio(carta=carta_territorio2, jogador=jogador.get_id_jogador(), qnt_exercitos=0, vizinhos=[])
    territorio3 = Territorio(carta=carta_territorio3, jogador=jogador.get_id_jogador(), qnt_exercitos=0, vizinhos=[])
    
    jogador.set_territorios(territorio1)
    jogador.set_territorios(territorio2)
    
    assert jogador.get_territorios() == [territorio1, territorio2]
    assert jogador.get_territorios() != [territorio2, territorio3]

def test_set_exercitos():
    jogador = Jogador('123')
    exercito_a = Exercito('white', 2)
    exercito_b = Exercito('white', 1)
    exercito_c = Exercito('white', 1)
    jogador.set_exercitos(exercito_a)
    jogador.set_exercitos(exercito_b)
    assert jogador.get_exercitos() == [exercito_a, exercito_b]
    assert jogador.get_exercitos() != [exercito_b, exercito_c]
    
def test_set_cor_exercito():
    jogador = Jogador('123')
    cor = 'white'
    jogador.set_cor_exercito(cor)
    assert jogador.get_cor_exercito() == cor
    assert jogador.get_cor_exercito() != 'black'
    assert len(jogador.get_cor_exercito()) == len(cor)
