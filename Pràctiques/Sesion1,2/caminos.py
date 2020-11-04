from algoritmia.datastructures.queues import Fifo
import sys
from . import laberinto
from algoritmia.datastructures.digraphs import UndirectedGraph
from .labyrinthviewer import LabyrinthViewer, Vertex, Edge, List


def path(g: UndirectedGraph, source: Vertex, target: Vertex):
    def recorrido_desde(u, v):
        seen.add(v)
        aristas.append((u, v))
        for suc in g.succs(v):
            if suc not in seen:
                recorrido_desde(v, suc)

    aristas = []
    seen = set()
    recorrido_desde(source, source)
    return recover_path(aristas, target)


def recover_path(aristas: List[Edge], traget: Vertex):
    bp = {}
    for u, v in aristas:
        bp[v] = u
    v = traget
    camino = [v]
    while v != bp[v]:
        v = bp[v]
        camino.append(v)
    camino.reverse()
    return camino


def shortest_path(g: UndirectedGraph, source: Vertex, target: Vertex):
    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((source, source))
    seen.add(source)
    while len(queue) > 0:
        u, v = queue.pop()
        aristas.append((u, v))
        for suc in g.succs():
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))
    return recover_path(aristas, target)


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    n=100
    graph = laberinto.create_labyrinth(50, 60, n)
    lv = LabyrinthViewer(graph, canvas_width=600, canvas_height=400, margin=10)
    lv.set_input_point((0, 0))
    lv.set_output_point((45, 38))
    lv.add_path(path(graph, (0, 0), (45, 38)), "blue")
    #lv.add_path(shortest_path(graph, (0,0), (45,38)), "red")
    lv.run()

