from Cartas import Cartas

class FactoryCartas:
    @staticmethod
    def criar_carta(tipo: str, **kwargs) -> Cartas:
        tipo = tipo.lower()  

        if tipo == "objetivo":
            descricao = kwargs.get('descricao', "Conquistar 24 territórios")
            return Cartas(descricao=descricao, tipo="Objetivo")

        elif tipo == "territorio":
            territorio = kwargs.get('territorio', "Brasil")
            descricao = f"Território: {territorio}"
            return Cartas(descricao=descricao, tipo="Território")

        elif tipo == "bonus":
            bonus = kwargs.get('bonus', 5)
            descricao = f"Receba {bonus} exércitos"
            return Cartas(descricao=descricao, tipo="Bônus")

        else:
            raise ValueError(f"Tipo de carta '{tipo}' não é válido.")