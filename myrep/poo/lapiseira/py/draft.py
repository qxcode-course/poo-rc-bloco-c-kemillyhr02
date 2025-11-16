class Grafite:
    def __init__(self, thickness:float, hardness:str, size:int):
        self.__thickness: float = thickness
        self.__hardness: str = hardness
        self.__size : int = size
       
    def sagePerSheet(self):
        if self.__hardness == "HB": 
            return 1
        if self.__hardness == "2B":
            return 2
        if self.__hardness == "4B":
            return 4
        else:
            return 6

        
    def set_size(self, size: int):
        self.__size = size
    
    def __str__(self):
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"
    
    def get_thickness(self):
        return self.__thickness

    def get_hardness(self):
        return self.__hardness
    
    def get_size(self):
        return self.__size

class Lapiseira:
    def __init__(self, thickness: float = 0, lead:Grafite | None = None):
        self.__thickess = thickness
        self.__lead= lead
        self.__barrel =[]

    def hasGrafite(self)-> bool:
        return self.__lead != None

    def insert(self, grafite:Grafite):
        if(self.__thickess != grafite.get_thickness()):
            print("fail: calibre incompatível")
            return
        if(self.hasGrafite()):
            print("fail: ja existe grafite")
            return 
        
        self.__barrel.append(grafite)
    
    def pull(self):
        if self.__lead is not None: 
            print ("fail: ja existe grafite no bico")
            return
        if len(self.__barrel) == 0:
            print("fail: não existe grafite no tambor")
            return
        self.__lead=self.__barrel[0]
        self.__barrel.pop(0)
        
     
    def remove(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return 
        self.__lead = None

    def write(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite no bico")
            return
        if  self.__lead.get_size() <= 10:
            print("fail: tamanho insuficiente")
            return
        
        k = self.__lead.sagePerSheet()

        if self.__lead.get_size() -k <10:
            print("fail: folha incompleta")
            self.__lead.set_size(10)
            return 
        self.__lead.set_size(self.__lead.get_size()- k)

    def __str__(self):
        lead = "[]" if self.__lead is None else str(self.__lead)
        ans = f"calibre: {self.__thickess}, bico: {lead}, tambor: <"
        for i, p in enumerate(self.__barrel):
            if p is not None:
                ans+= str(p)
        ans +=">"
        return ans
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
        elif args[0]=="pull":
            lapiseira.pull()
        else: 
            print("fail: comando invalido")
    
main()






        