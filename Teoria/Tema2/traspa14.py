#recorre aristas en anchura
from algoritmia.datastructures.digraphs import Digraph, UndirectedGraph
from algoritmia.datastructures.queues import Fifo

from labyrinthviewer import LabyrinthViewer, Vertex, Edge, List, Tuple

Edge = Tuple[Vertex, Vertex]

def recorre_aristas_anchura(grafo: Digraph, v_inical: Vertex) -> List[Edge]:
    aristas = []
    seen = set()
    queue = Fifo()
    queue.push((v_inical, v_inical))
    seen.add(v_inical)
    while len(queue)>0:
        u, v = queue.pop()
        aristas.append((u, v))
        for suc in grafo.succs():
            if suc not in seen:
                seen.add(suc)
                queue.push((u, v))
    return aristas


# e = [((4, 7), (4, 6)), ((4, 7), (4, 8)), ((1, 3), (0, 3)), ((1, 3), (1, 4)), ((4, 8), (4, 9)), ((3, 0), (2, 0)),
#          ((3, 0), (4, 0)), ((2, 8), (2, 7)), ((2, 8), (1, 8)), ((2, 1), (2, 0)), ((2, 1), (2, 2)), ((0, 0), (1, 0)),
#          ((1, 6), (1, 5)), ((1, 6), (2, 6)), ((3, 7), (3, 8)), ((3, 7), (3, 6)), ((2, 5), (1, 5)), ((2, 5), (2, 4)),
#          ((0, 3), (0, 2)), ((4, 0), (4, 1)), ((1, 2), (0, 2)), ((1, 2), (1, 1)), ((4, 9), (3, 9)), ((3, 3), (2, 3)),
#          ((3, 3), (4, 3)), ((2, 9), (3, 9)), ((2, 9), (1, 9)), ((4, 4), (3, 4)), ((4, 4), (4, 3)), ((3, 6), (3, 5)),
#          ((2, 2), (3, 2)), ((4, 1), (4, 2)), ((1, 1), (1, 0)), ((0, 1), (0, 2)), ((3, 2), (3, 1)), ((2, 6), (2, 7)),
#          ((4, 5), (4, 6)), ((0, 4), (0, 5)), ((0, 4), (1, 4)), ((3, 9), (3, 8)), ((0, 5), (0, 6)), ((0, 7), (0, 6)),
#          ((0, 7), (1, 7)), ((4, 2), (4, 3)), ((0, 8), (0, 9)), ((3, 5), (3, 4)), ((1, 8), (1, 7)), ((0, 9), (1, 9)),
#          ((2, 3), (2, 4))]
#
# g = UndirectedGraph(V=e)
# recorre_aristas_anchura(g, (4,7))
