from src.Cartas import Cartas

class Territorio:
    def __init__(self, carta: Cartas, jogador: str, qnt_exercitos: int, vizinhos: list):
        if carta.get_tipo() != "Território":
            raise ValueError("A carta associada deve ser do tipo 'Território'.")
        
        self._nome = carta.get_descricao()
        self._jogador = jogador
        self._qnt_exercitos = qnt_exercitos
        self._vizinhos = vizinhos
    

    def get_nome(self) -> str:
        return self._nome

    def get_jogador(self) -> str:
        return self._jogador

    def get_qnt_exercitos(self) -> int:
        return self._qnt_exercitos

    def get_vizinhos(self) -> list:
        return self._vizinhos
    
    def set_nome(self, nome: str):
        self._nome = nome

    def set_jogador(self, jogador: str):
        self._jogador = jogador

    def set_qnt_exercitos(self, qnt: int):
        if qnt < 0:
            raise ValueError("A quantidade de exércitos não pode ser negativa.")
        self._qnt_exercitos = qnt

    def set_vizinhos(self, vizinhos: list):
        self._vizinhos = vizinhos
    
    def adicionar_exercitos(self, qnt: int):
        self._qnt_exercitos += qnt
    
    def remover_exercitos(self, qnt: int):
        if qnt > self._qnt_exercitos:
            raise ValueError("Não há tropas suficientes para remover.")
        self._qnt_exercitos -= qnt