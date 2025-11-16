class Kid:
    def __init__(self, nome:str, idade:int):
        self.__idade = idade
        self.__nome = nome

    def getAge(self):
        return self.__idade
    def getName(self):
        return self.__nome
    def setAge(self, age:int):
        self.__idade = age
    def setNome(self, nome: str):
        self.__nome = nome
    def __str__(self):
        return f"{self.__nome}:{self.__idade}"

class PulaPula:
    def __init__(self):
        self.__playing : list[Kid | None] = []
        self.__waiting : list[Kid | None] = []
    
    def arrive(self, name:str, age:int):
        kid = Kid(name, age)
        self.__waiting.insert(0,kid)

    def enter(self):
        if not self.__waiting:
           print(f"fila vazia")
        self.__playing.insert(0, self.__waiting[len(self.__waiting)-1])
        self.__waiting.pop(len(self.__waiting)-1)

    def remove(self, name:str):
        for i, kid in enumerate(self.__playing):
            if kid.getName()==name:
                self.__playing.pop(i)
                return
        for i, kid in enumerate(self.__waiting):
            if kid.getName()==name:
                self.__waiting.pop(i)
                return
        print(f"fail: {name} nao esta no pula-pula")
    def leave(self):
        if not self.__playing:
            return 
        self.__waiting.insert(0, self.__playing[len(self.__playing)-1])
        self.__playing.pop(len(self.__playing)-1)

    def __str__(self):
        playing_str= ", ".join(str(k) for k in self.__playing)
        waiting_str= ", ".join(str(k) for k in self.__waiting)
        return f"[{waiting_str}] => [{playing_str}]"


def main():
    trampolin=PulaPula()
    while True:
        line= input()
        print(f"${line}")
        args=line.split()
        if args[0]=="end":
            break
        elif args[0]=="show":
            print(trampolin)
        elif args[0]=="arrive":
            trampolin.arrive(args[1], int(args[2]))
        elif args[0]=="enter":
            trampolin.enter()
        elif args[0]=="leave":
            trampolin.leave()
        elif args[0]=="remove":
            trampolin.remove(args[1])
        else:
            return "comando invalido"
main()