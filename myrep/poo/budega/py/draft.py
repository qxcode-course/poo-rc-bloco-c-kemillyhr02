class Pessoa:
    def __init__(self, nome: str):
        self.nome = nome
    
    def __str__(self)-> str:
            return self.nome
    def getNome(self) -> str:
         return self.nome

class Market:
    def __init__(self, caixas: int):
        self.espera = []
        self.caixas = [None]*caixas

    def __str__(self) -> str:
        ans = "Caixas: ["
        for n, p in enumerate(self.caixas):
            if p is None:
                ans+="-----"
            else:
                ans+=p.getNome()
            if n <len(self.caixas)-1:
                ans+= ", "
        ans+="]\nEspera: ["
        for n, p in enumerate(self.espera):
            if p is None: 
                ans+="-----"
            else:
                ans+=p.getNome()
            if n<len(self.espera)-1:
                ans+=", "
        ans +="]"
        return ans
    
    def arrive(self, person:Pessoa):
        self.espera.append(person)

    def call(self, index:int):
        if not self.espera:
            print(f"fail: sem clientes")
            return 
        if self.caixas[index] is not None:
            print(f"fail: caixa ocupado")
            return
        self.caixas[index]=self.espera[0]
        self.espera.pop(0)   


    def finish(self, index:int):
        if len(self.caixas) <= index:
            print(f"fail: caixa inexistente")
            return 
        if self.caixas[index] is None:
            print(f"fail: caixa vazio")
            return
        pessoa = self.caixas[index]
        self.caixas[index] = None
        return pessoa

def main():
    market= None
    while True:
        line = input()
        print(f"${line}")
        args=line.split()

        if args[0]=="end":
            break
        elif args[0]=="init":
            market=Market(int(args[1]))
        elif args[0]=="show":
            print(market)
        elif args[0]=="arrive":
            pessoa=Pessoa(str(args[1]))
            market.arrive(pessoa)
        elif args[0]=="call":
            market.call(int(args[1]))
        elif args[0]=="finish":
            market.finish(int(args[1]))
        else:
            print(f"fail: comando invalido")
main()

    
            



