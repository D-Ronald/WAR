class Cartas:

    def __init__(self, descricao: str, tipo: str):
        self.descricao = descricao
        self.tipo = tipo

    def get_descricao(self) -> str:
        return self.descricao

    def get_tipo(self) -> str:
        return self.tipo
    
    def set_descricao(self, descricao: str):
        self.descricao = descricao

    def set_tipo(self, tipo: str):
        self.tipo = tipo

    def trocar_carta(self, nova_descricao: str, novo_tipo: str):
        self.descricao = nova_descricao
        self.tipo = novo_tipo

