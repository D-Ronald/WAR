import random
from src.Exercito import Exercito
def test_new_exercito():
    cor = 'white'
    quantidade = 3
    exercito = Exercito(cor, quantidade)
    assert exercito.get_cor() == cor
    assert exercito.get_quantidade() == quantidade

def test_set_cor():
    cor = 'black'
    quantidade = 3
    exercito = Exercito(None, quantidade)
    exercito.set_cor(cor)
    assert exercito.get_cor() == cor
    
def test_set_quantidade():
    cor = 'black'
    quantidade = 3
    exercito = Exercito(cor, None)
    exercito.set_quantidade(quantidade)
    assert exercito.get_quantidade() == quantidade
    assert exercito.get_quantidade() <4 and exercito.get_quantidade() >0
    assert type(exercito.get_quantidade()) != float
