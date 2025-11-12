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
if i in l1:
    print(f"elemento achado {i}")
else:
    print(f"nao achei nada")

#pares array
n= [4,9,6,23,26,28,54,65]
for i in n:
    if i%2==0:
        print(i)

#x_quadrado
#n= [2,3,4,5,6]
#for i in n:
 #   if i**2:
#        print(i)



