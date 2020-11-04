from typing import *
from random import random, seed

def mientras_quepa(W: List[int], C: int) -> List[int]:
    res = []
    suma = 0
    cont = 0
    for i in range (len(W)):
        suma += W[i]
        if suma > C:
            cont += 1
            suma = W[i]
        res.append(cont)
    return res


def primero_que_quepa(W: List[int], C: int) -> List[int]:
    res = [0] * len(W)
    pesos = [0] * len(W)
    for i, w in enumerate(W):
        for contenedor, actual in enumerate(pesos):
            peso_contenedor = actual + w
            if peso_contenedor <= C:
                pesos[contenedor] = peso_contenedor
                res[i] = contenedor
                break
    return res


def primero_que_quepa_ordenado(W: List[int], C: int) -> List[int]:
    indices_ordenados=sorted(range(len(W)), key = lambda  i: -W[i])

    res = [0] * len(W)
    pesos = [0] * len(W)
    for i in indices_ordenados:
        for contenedor, actual in enumerate(pesos):
            peso_contenedor = actual + W[i]
            if peso_contenedor <= C:
                pesos[contenedor] = peso_contenedor
                res[i] = contenedor
                break
    return res


def prueba_binpacking():
    W, C = [1, 2, 8, 7, 8, 3], 10
    #seed(42)
    #W, C = [int(random()*1000)+1 for i in range(1000)], 1000

    for solve in [mientras_quepa, primero_que_quepa, primero_que_quepa_ordenado]:
        print("-" * 40)
        print("Método:", solve.__name__)
        try:
            sol = solve(W, C)
            print("Usados {} contenedores: {}".format(1 + max(sol), sol))
        except NotImplementedError:
            print("No implementado")


if __name__ == "__main__":
    prueba_binpacking()
