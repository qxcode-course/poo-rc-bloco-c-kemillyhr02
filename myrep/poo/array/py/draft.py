import random

ary=[]
ary= [1,2,3,4,5]
print(ary)
#tamanhoary
t= len(ary)
print(f"tamanho: {t}\n")

#add_remover_f
print("adicionar e remover final")
l1=[2,4,6,3,9]
print(l1)
l2= l1
l2.append(8) 
print(l2)
l3= l1
l3.pop(4)
print(l3)
print("\n")

#add_remover.i
print("adicionar e remover inicio")
l1= [4,9,6,7,5]
print(l1)
l2=l1
l2.append(3)
print(l2)
l3=l1
l3.remove(4)
print(l3)
print("\n")
print("add e remover posição especifica")
#add_e_remover_espec
l1=[1,2,3,5,6,7]
print(l1)
l2=l1
l2.insert(4,8)
l3=l1
l3.remove(2)
print(l2,l3)
print("\n")



#join
print("join")
n = 10
l1 = " - ".join(str(i) for i in range(0, n+1))
print(l1)
print("\n")
#cria_x_zero-n
print("zero a n")
l= list(range(0,n-1))
print(l)
print("\n")
#random
print("random")
l = []
for i in range(0, 5):
    l.append(random.randint(1,10))
print(f"aleatorio: {l}")

#indicejoin python
print(f"indice 2: {l[2]}")


#for-range
l1 = [1,2,3,4,5]
n = len(l1)
for i in range(0,n):
    print(f"-> {i} ", end="")
print("\n")


#procurar X usando laço
l = [10, 20, 30 ,40 , 50]
i = 0
f = len(l)
x = 40
while i<f:
    if  x == l[i]:
        print(f"achei!!! o valor {x}\n")
    i+=1
#array_pares
l=[i for i in range(1,15) if i%2==0]
print(f"os elementos pares sao {l}")

#indexado
l = [i**2  for i in range(1, 11)]
print(f"ao quadrado {l}")

#função nativa
print("?????")
print("buscar e remover x")
#buscar e remover
l=[6,5,4,3,2,1]
x=4
l1=l
l1= l.remove(x)
print(f"lista apos remover {x}: {l}")
print("\n")
#remover todos em l
print("remover x na l1")
l1= [2, 1, 2, 3, 2, 4, 2]
valor= 2
while valor in l1:
    l1.remove(valor)
print(l1)
print(f"valor removido: {valor}")


