vector=[14,2,10,15,3,7,0]
k=3

#def buscar_kesimo(v, k):
#    vector.sort()
#    return vector[k-1]

def buscar_kesimo(v, k):
    for i in range(len(vector)):
        cuenta_mayores=0
        for j in range(len(vector)):
            if not cuenta_mayores == k:
                if not i==j:
                    if vector[i] > vector[j]:
                        cuenta_mayores += 1
            else:
                break
        if cuenta_mayores == k-1:
            return vector[i]

print(buscar_kesimo(vector,k))