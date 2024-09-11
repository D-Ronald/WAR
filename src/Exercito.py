class Exercito:
    def __init__(self, cor, quantidade):
        self.cor = cor
        self.quantidade = quantidade
        self.territorio = None
    
    def get_cor(self):
        return self.cor
    
    def get_quantidade(self):
        return self.quantidade
    
    def set_cor(self, cor: str):
        self.cor = cor
    
    def set_quantidade(self, quantidade: int):
        self.quantidade = quantidade
    
    
    def reforçar(self, quantidade):
        pass
    
    def reduzir(self, quantidade):
        pass