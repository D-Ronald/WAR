from abc import ABC, abstractmethod
import src.Objetivo as Objetivo
import src.Territorio as Territorio
import src.Exercito as Exercito

class EstrategiaAcao(ABC):
    @abstractmethod
    def executar(self, jogador, *args):
        pass

class EstrategiaAtaque(EstrategiaAcao):
    def executar(self, jogador, inimigo, territorio_saida, territorio_alvo, qnt_exercito):
        if inimigo.get_id_jogador() != jogador.get_id_jogador():
            if territorio_saida in jogador.get_territorios() and territorio_alvo in inimigo.get_territorios():
                return 'Apto para atacar'
            else:
                return 'Territórios inválidos para ataque'
        else:
            return 'Você não pode atacar seus próprios territórios'

class EstrategiaMoverExercito(EstrategiaAcao):
    def executar(self, jogador, territorio_origem, territorio_destino, qnt_exercito):
        if territorio_origem in jogador.get_territorios() and territorio_destino in jogador.get_territorios():
            return f'Movendo {qnt_exercito} exércitos de {territorio_origem} para {territorio_destino}'
        else:
            return 'Territórios inválidos para movimentação'


class EstrategiaDefesa(EstrategiaAcao):
    def executar(self, jogador, territorio_defendido):
        if territorio_defendido in jogador.get_territorios():
            return f'Defendendo o território {territorio_defendido}'
        else:
            return 'Território não pertence ao jogador'


class Jogador:
    def __init__(self, id_jogador):
        self.id_jogador = id_jogador
        self.objetivo = None
        self.territorios = []
        self.exercitos = []
        self.cor_exercito = None
        self.estrategia_acao = None
  
    def set_id_jogador(self, id_jogador):
        self.id_jogador = id_jogador
    
    def get_id_jogador(self):
        return self.id_jogador
    
    def set_objetivo(self, objetivo: Objetivo):
        self.objetivo = objetivo
    
    def get_objetivo(self):
        return self.objetivo
    
    def set_territorios(self, territorio: Territorio):
        self.territorios.append(territorio)
    
    def get_territorios(self):
        return self.territorios
    
    def set_exercitos(self, exercitos: Exercito):
        self.exercitos.append(exercitos)
    
    def get_exercitos(self):
        return self.exercitos
    
    def set_cor_exercito(self, cor_exercito: str):
        self.cor_exercito = cor_exercito
        
    def get_cor_exercito(self):
        return self.cor_exercito

    
    def set_estrategia_acao(self, estrategia: EstrategiaAcao):
        self.estrategia_acao = estrategia

    def executar_acao(self, *args):
        if self.estrategia_acao:
            return self.estrategia_acao.executar(self, *args)
        else:
            return 'Nenhuma estratégia definida'
