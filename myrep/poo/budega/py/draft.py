class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
    
    def __str__(self)-> str:
        def toString(Pessoa: Pessoa | None)->str:
            if Pessoa is None:
                return "---"
        return str(Pessoa)
    def getNome(self):
        return self.nome

class Market:
    def __init__(self, caixas: int):
        self.espera: list[Pessoa] = []
        self.caixas: list[Pessoa | None] = []

    def toString(self):
        if self.caixas is []:
            return "self.caixas: -----, -----"
        return ""
            



