from random import shuffle
from algoritmia.datastructures.mergefindsets import MergeFindSet
from algoritmia.datastructures.digraphs import UndirectedGraph
from .labyrinthviewer import LabyrinthViewer


def create_labyrinth(rows, cols, n=0):
    vertices = []
    for i in range(rows):
        for j in range(cols):
            vertices.append((i, j))

    mfs = MergeFindSet()
    for un_vertice in vertices:
        mfs.add(un_vertice)

    edges = []
    for r in range(rows):
        for c in range(cols):
            if r == rows - 1:
                if not c == cols - 1:
                    edges.append(((r, c), (r, c + 1)))
            elif c == cols - 1:
                edges.append(((r, c), (r + 1, c)))
            else:
                edges.append(((r, c), (r, c + 1)))
                edges.append(((r, c), (r + 1, c)))

    # for f,c in vertices:
    #   if c+1<cols:
    #        edges.append(((f,c), (f,c+1)))
    #    if f+1<rows:
    #        edges.append(((f,c),(f+1,c)))

    shuffle(edges)

    corridors = []
    for edge in edges:
        u, v = edge
        if mfs.find(u) != mfs.find(v):
            mfs.merge(u, v)
            corridors.append(edge)
        elif n > 0:
            corridors.append(edge)
            n -= 1

    return UndirectedGraph(E=corridors)


if __name__ == '__main__':
    graph = create_labyrinth(100, 100)
    lv = LabyrinthViewer(graph, canvas_width=600, canvas_height=400, margin=10)
    lv.run()
