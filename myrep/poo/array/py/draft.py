k=[]
k1=[1,2,3,4,5]
print(f"Tamanho do array k1: {len(k1)}")

#inicio
k1.insert(0, 10)
k1.pop(0)

#fim
k1.append(10)
k1.pop(len(k1)-1)


#
k1.insert(2, 8)
print(f"array k1: {k1}")