entero=int(input("Introduce enteros. Un número negativo para acabar: "))
lista=[]
while entero>=0:
    lista.append(entero)
    entero = int(input("Introduce enteros. Un número negativo para acabar: "))
lista.sort()
for elem in lista:
    print(elem)