def square():
    SIDE_LENGTH = 50
    vert = [(0, 0, 0), (0, 0, 50), (0, 50, 0), (0, 50, 50), (50, 0, 0), (50, 0, 50), (50, 50, 0), (50, 50, 50)]
    edges = [[(0, 0, 0), (0, 0, 50), (0, 50, 0), (50, 0, 0)],
                [(0, 0, 50), (50, 0, 50), (0, 50, 50)],
                [(0, 50, 0), (0, 50, 50), (50, 50, 0)], 
                [(0, 50, 50), (50, 50, 50)], 
                [(50, 0, 0), (50, 0, 50), (50, 50, 0)], 
                [(50, 0, 50), (50, 50, 50)],
                [(50, 50, 0), (50, 50, 50)]]
    
    """ vertices = numpy.empty((8, 3))
    for col in range(8):
        for fil in range(3):
            vertices[col][fil] = vert[col][fil]

    edges = []
    for vertice in vertices:
        lst = []
        lst.append(vertice)
        vertices.pop(0)
        for vertice in vertices:
            if numpy.linalg.norm(vertice-lst[0]) == SIDE_LENGTH:
                lst.append(vertice)
        edges.append(lst)
        
    print(edges) """
    return edges