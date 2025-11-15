class Grafite:
    def __init__(self, thickness:float, hardness:str, size:int):
        self.__thickness: float = thickness
        self.__hardness: str = hardness
        self.__size : int = size
    def usarPorfolha(self):
        if self.__hardness == "HB": 
            return 1
        if self.__hardness == "2B":
            return 2
        if self.__hardness == "4B":
            return 4
        if self.__hardness == "6B":
            return 6
        
    def set_size(self, size: int):
        self.__size = size
    
    def __str__(self):
        return f"[{self.__thickness}: {self.__hardness}: {self.__size}]"
    
    def get_thickness(self):
        return self.__thickness

    def get_hardness(self):
        return self.__hardness
    
    def get_size(self):
        return self.__size

class Lapiseira:
    def __init__(self, thickness: float = 0, grafite:Grafite | None = None):
        self.__thickess = thickness
        self.__grafite = grafite

    def hasGrafite(self) ->bool:
        return self.__grafite != None

    def insert(self, grafite:Grafite):
        if(self.__thickess != grafite.get_thickness()):
            print("fail: calibre incompativel")
            return
        if(self.hasGrafite()):
            print("fail: ja existe grafite")
            return 
        self.__grafite = grafite

        
    def remove(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return 
        self.__grafite = None

    def write(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return
        if  self.__grafite.get_size() <= 10:
            print("fail: tamanho insuficiente")
            return
        n = self.__grafite.usarPorfolha()

        if self.__grafite.get_size() - n <10:
            print("fail: folha incompleta")
            self.__grafite.set_size(10)
            return 
        self.__grafite.set_size(self.__grafite.get_size() - n)

    def __str__(self):
        return f"calibre: {self.__thickess}, grafite: {"null" if self.__grafite == None else self.__grafite}"
    
def main():
    lapiseira= Lapiseira()
    while True:
        line= input()
        print(f"${line}")
        args= line.split()
        if args[0]=="end":
            break
        elif args[0]=="init":
            lapiseira= Lapiseira(float(args[1]))
        elif args[0] == "show":
            print(lapiseira)
        elif args[0]=="insert":
            grafite = Grafite(float(args[1]), args[2], int(args[3]))
            lapiseira.insert(grafite)
        elif args[0] == "remove":
            lapiseira.remove()
        elif args[0]=="write":
            lapiseira.write()
        else: 
            print("fail: comando invalido")
    
main()






        