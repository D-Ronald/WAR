import src.Objetivo as Objetivo, src.Territorio as Territorio , src.Exercito as Exercito

class Jogador:
    def __init__(self, id_jogador):
        self.id_jogador = id_jogador
        self.objetivo = None
        self.territorios = []
        self.exercitos = []
        self.cor_exercito = None
  
    
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

    def mover_exercito():
        pass
    
    def atacar_territorio(self, inimigo , território_saida, territorio_alvo, qnt_exercito):
       if inimigo.id_jogador != self.id_jogador:
           if território_saida in self.territorios and território_saida in inimigo.territorios:
                return 'apto'
       else: 
           return 'você não pode atacar seus próprios territórios'
           
    def receber_exercito():
        pass    
    
    def alocar_exercito():
        pass
    
    def defender():
        pass
    