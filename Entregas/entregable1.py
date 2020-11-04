import sys
from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
import random

def crear_vertices(rows, cols):
    vertices = []
    for x in range(rows):
        for y in range(cols):
            vertices.append((x, y))

    mfset = MergeFindSet()
    for v in vertices:
        mfset.add(v)

    edges = []
    for n in range(rows):
        for x in range(cols):
            vertice = (n, x)
            if x + 1 < cols:
                vecino1 = (n, x + 1)
                edges.append((vertice, vecino1))
            if n + 1 < rows:
                vecino2 = (n + 1, x)
                edges.append((vertice, vecino2))
    return edges

if __name__ == '__main__':
    lista = sys.argv
    print(lista)
    f = open(lista[1])
    #num_filas num_cols
    l1 = f.readline().split(" ")
    num_filas = l1[0]
    num_cols = l1[1]
    #n_paredes
    n_paredes = f.readline()
    #aristas ((f1,c1),(f2,c2))
    edges = crear_vertices(num_filas, num_cols)
    print(edges)
    aristas = []
    i = 0
    while i <= n_paredes:
        l = f.readline().split(" ")
        vertice1 = (l[0], l[1])
        vertice2 = (l[2], l[3])

    f.close()