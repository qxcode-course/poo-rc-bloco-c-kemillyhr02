class Pessoa:
    def __init__(self, nome: str):
        self.__nome: str = nome

    def getNome(self):
        return self.__nome
    
    def setNome(self, nome:str):
        self.__nome = nome
    
    def __str__(self):
        return f"{self.__nome}"


class Market:

    def __init__(self, caixas: int =0 ):
        self.__caixas: list[Pessoa | None]= [None]*caixas
        self.__espera: list[Pessoa | None] = []
        self.__index: int = caixas

    def __str__(self):
        caixas = ", ".join("-----" if i is None else i.getNome() for i in self.__caixas)
        espera = ", ".join("-----" if i is None else i.getNome() for i in self.__espera )
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"

    def arrive(self, pessoa:Pessoa):
        self.__espera.append(pessoa)

    def call(self, index: int):
        if self.__espera== []:
            print(f"fail: sem clientes")
            return
        if self.__caixas[index] is not None:
            print("fail: caixa ocupado")
            return
            
        self.__caixas[index]=self.__espera[0]
        self.__espera.pop(0)
           
    def finish(self, index: int):
        if index <0 or index >= self.__index:
            print(f"fail: caixa inexistente")
            return
        if self.__caixas[index] is None:
            print("fail: caixa vazio")
            return

        self.__caixas[index]= None
                


def main():
    market=Market()
    while True:
        line= input()
        print(f"${line}")
        args=line.split()

        if args[0]=="end":
            break
        elif args[0]=="init":
            market=Market(int(args[1]))
        elif args[0]=="show":
            print(market)
        elif args[0]=="arrive":
            pessoa=Pessoa(args[1])
            market.arrive(pessoa)
        elif args[0]=="call":
            market.call(int(args[1]))
        elif args[0]=="finish":
            market.finish(int(args[1]))
        else:
            print("fail: comando inválido")

main()
        