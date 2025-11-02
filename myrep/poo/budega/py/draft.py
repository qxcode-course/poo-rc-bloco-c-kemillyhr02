class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
    
    def __str__(self)-> str:
            return self.nome
    def getNome(self):
         

class Market:
    def __init__(self, caixas: int):
        self.espera: list[Pessoa] = []
        self.caixas: list[Pessoa | None] = []

    def toString(self):
        if self.caixas is []:
            return f"self.caixas:[-----, -----]"
        return f"[self.nome, self.nome, self.nome]"
    
            



