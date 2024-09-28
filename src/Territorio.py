from src.Cartas import Cartas

class Territorio:
    def __init__(self, carta: Cartas, jogador: str, qnt_exercitos: int, vizinhos: list):
        if carta.get_tipo() != "Território":
            raise ValueError("A carta associada deve ser do tipo 'Território'.")
        
        self.nome = carta.get_descricao()
        self.jogador = jogador
        self.qnt_exercitos = qnt_exercitos
        self.vizinhos = vizinhos
    

    def get_nome(self) -> str:
        return self.nome

    def get_jogador(self) -> str:
        return self.jogador

    def get_qnt_exercitos(self) -> int:
        return self.qnt_exercitos

    def get_vizinhos(self) -> list:
        return self.vizinhos
    
    def set_nome(self, nome: str):
        self.nome = nome

    def set_jogador(self, jogador: str):
        self.jogador = jogador

    def set_qnt_exercitos(self, qnt: int):
        if qnt < 0:
            raise ValueError("A quantidade de exércitos não pode ser negativa.")
        self.qnt_exercitos = qnt

    def set_vizinhos(self, vizinhos: list):
        self.vizinhos = vizinhos
    
    def adicionar_exercitos(self, qnt: int):
        self.qnt_exercitos += qnt
    
    def remover_exercitos(self, qnt: int):
        if qnt > self.qnt_exercitos:
            raise ValueError("Não há tropas suficientes para remover.")
        self.qnt_exercitos -= qnt