from algoritmia.datastructures.digraphs import UndirectedGraph


def knigth_graph(num_rows: int, num_cols: int) -> UndirectedGraph:
    vertices = []
    for i in range(num_rows):
        for j in range(num_cols):
            vertices.append((i,j))

    aristas = []
    for row, col in vertices:
        #1
        if col-2>=0 and row-1<num_rows:

            aristas.append(((row, col), (row-1, col-2)))
        #2
        if row-2>=0 and col-1>=0:

            aristas.append(((row, col), (row-2, col-1)))
        #3
        if row+2<num_rows and col+1<num_cols:
            aristas.append(((row, col), (row+2, col+1)))
        #4
        if row+1<num_rows and col+2<num_cols:
            aristas.append(((row, col), (row+1, col+2)))

    print(aristas)

knigth_graph(3,3)





