#recorre aristas en anchura
from algoritmia.datastructures.digraphs import Digraph
from algoritmia.datastructures.queues import Fifo

from .labyrinthviewer import LabyrinthViewer, Vertex, Edge, List

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
