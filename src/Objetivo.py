from src.Cartas import Cartas

class Objetivo:
    def __init__(self, status: str, descricao: str):
        self.status = status
        self.descricao = descricao
        self.carta = None  

    def set_carta(self, carta: Cartas):
        if carta.get_tipo() == "Objetivo":
            self.carta = carta
        else:
            raise ValueError("A carta associada deve ser do tipo 'Objetivo'.")

    def get_carta(self) -> Cartas:
        return self.carta

    def verificar_progresso(self):
        if self.carta:
            print(f"Objetivo: {self.descricao}")
            print(f"Status: {self.status}")
            print(f"Carta associada: {self.carta.get_descricao()}, Tipo: {self.carta.get_tipo()}")
        else:
            print(f"Objetivo: {self.descricao}")
            print(f"Status: {self.status}")
            print("Nenhuma carta associada ao objetivo.")