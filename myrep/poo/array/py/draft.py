import random
#array vazio
n= []
ary= ["py", "tr", "yk", "op"]
print(f"tamanho da lista: {len(ary)}")

#final
ary.append("my")
print(f"adicionar ao final: {ary}")
ary.pop(4)
print(f"remover ao final: {ary}")


#inicio
ary.insert(0, "tvy")
print(f"adicionar ao inicio: {ary}")
ary.pop(0)
print(f"remover o inicio: {ary}")

 
#especifica
ary.insert(3,"lj")
ary.pop(2)
print(f" lista modificada: {ary}")


#join
line= " ".join(ary)
print(f"formatação: {line}")


#0-n
n1= 10
l=[]
for i in range (0, n1+1):
    l.append(i)
print(f"sequencial de numeros: {l}")


print(random.randint(1, 100))

#aleatorio
l=[]
for i in range (0, 5):
    l.append(random.randint(0, 99))
print(f"valores aleatorios: {l}")
print(f"indice 1: {l[1]}")


#for-range
for i in l:
    print(f"{i} -> ", end="")
print("")
#for indexado
for i in range(0, len(l)):
    print(f"{l[i]} -> ", end="")


l = [10,20,30,40,50]
search = 20

for i in l:
    if i == search:
        print("elemento achado")
#laço 
l = [1,2,3,5,4]
i=0
for i in l:
    if i==4:
        print(f"achei {i-1}")
#função nativa
l1= [3,8,5,9,4]
n=8
if n in l1:
    print(f"elemento achado {n}")
else:
    print(f"nao achei nada")

#pares array
n= [4,9,6,23,26,28,54,65]
for i in n:
    if i%2==0:
        print(i, end=" ")
print("")

#x_quadrado
n= [2,3,4,5,6]
l: list[int] = []
for i in n:
    l.append(i**2)
print(l)

#buscar e remover
l=[3,8,5,4,9,5]
valor = 5
if valor in l:
    l.remove(valor)
print(l)

#remover todos x
l=[5,3,8,5,4,5,9,5,5]
valor = 1
contador=0
if valor in l:
    for x in range(len(l)):
        if l[x]==valor:
            contador+=1
    for x in range(contador):
        l.remove(valor)
print(l)
#
