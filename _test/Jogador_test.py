from src.Jogador import Jogador 
from src.Territorio import Territorio
from src.Exercito import Exercito


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
    territorio = Territorio('Brasil', jogador, 0, None)
    territorio2 = Territorio('suk', jogador, 0, None) 
    territorio3 = Territorio('Argentina', jogador, 0, None) 
    
    jogador.set_territorios(territorio)
    jogador.set_territorios(territorio2)
    assert jogador.territorios == [territorio,territorio2]
    assert jogador.territorios != [territorio2,territorio3]

    
def test_set_exercitos():
    jogador = Jogador('123')
    exercito_a = Exercito('white', 2)
    exercito_b = Exercito('white', 1)
    exercito_c = Exercito('white', 1)
    jogador.set_exercitos(exercito_a)
    jogador.set_exercitos(exercito_b)
    assert jogador.exercitos == [exercito_a,exercito_b]
    assert jogador.exercitos != [exercito_b,exercito_c]
    
def test_set_cor_exercito():
    jogador = Jogador('123')
    cor = 'white'
    jogador.set_cor_exercito(cor)
    assert jogador.get_cor_exercito() == cor
    assert jogador.get_cor_exercito() != 'black'
    assert len(jogador.get_cor_exercito()) == len(cor)