class Pessoa:
    def __init__(self, nome: str):
        self.__nome = nome
    
    def __str__(self)-> str:
            return self.__nome
    def getNome(self) -> str:
         return self.__nome

class Market:
    def __init__(self, caixas: int):
        self.__espera = []
        self.__caixas = [None]*caixas

    def __str__(self) -> str:
        ans = "Caixas: ["
        for n, p in enumerate(self.__caixas):
            if p is None:
                ans+="-----"
            else:
                ans+=p.getNome()
            if n <len(self.__caixas)-1:
                ans+= ", "
        ans+="]\nEspera: ["
        for n, p in enumerate(self.__espera):
            if p is None: 
                ans+="-----"
            else:
                ans+=p.getNome()
            if n<len(self.__espera)-1:
                ans+=", "
        ans +="]"
        return ans
    
    def arrive(self, person:Pessoa):
        self.__espera.append(person)

    def call(self, index:int):
        if not self.__espera:
            print(f"fail: sem clientes")
            return 
        if self.__caixas[index] is not None:
            print(f"fail: caixa ocupado")
            return
        self.__caixas[index]=self.__espera[0]
        self.__espera.pop(0)   


    def finish(self, index:int):
        if len(self.__caixas) <= index:
            print(f"fail: caixa inexistente")
            return 
        if self.__caixas[index] is None:
            print(f"fail: caixa vazio")
            return
        pessoa = self.__caixas[index]
        self.__caixas[index] = None
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

    
            



