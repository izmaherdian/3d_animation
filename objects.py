import numpy as np

class Object:

    def __init__(self):
        pass

class Cube(Object):

    def __init__(self, side_length, mass = 1):
        super().__init__()
        self.side_length = side_length
        self.vertices = self.vertices()
        self.center_of_mass = self.center_of_mass()
        self.edges = self.edges()
    
    def vertices(self):
        vertices_matrix = np.array([[0, 0, 0], [0, 0, self.side_length], [0, self.side_length, 0], [0, self.side_length, self.side_length], [self.side_length, 0, 0], [self.side_length, 0, self.side_length], [self.side_length, self.side_length, 0], [self.side_length, self.side_length, self.side_length]])
        return vertices_matrix

    def center_of_mass(self):
        # We consider the solid to be a set of points in space, all of them with the same constant mass.
        # This set of points will be the vertices of the Object.
        coords = np.sum(self.vertices, axis=0)/len(self.vertices)
        return coords

    def edges(self):
        edges_matrix = []
        for p in self.vertices:
            lst = []
            lst.append(p)
            for q in self.vertices:
                if np.linalg.norm(p-q) == self.side_length:
                    lst.append(q)
            edges_matrix.append(lst)
        return edges_matrix


cube = Cube(50)
print(cube.edges)

""" def square():
    SIDE_LENGTH = 50
    vert = [(0, 0, 0), (0, 0, 50), (0, 50, 0), (0, 50, 50), (50, 0, 0), (50, 0, 50), (50, 50, 0), (50, 50, 50)]
    edges = [[(0, 0, 0), (0, 0, 50), (0, 50, 0), (50, 0, 0)],
                [(0, 0, 50), (50, 0, 50), (0, 50, 50)],
                [(0, 50, 0), (0, 50, 50), (50, 50, 0)], 
                [(0, 50, 50), (50, 50, 50)], 
                [(50, 0, 0), (50, 0, 50), (50, 50, 0)], 
                [(50, 0, 50), (50, 50, 50)],
                [(50, 50, 0), (50, 50, 50)]]
    
    vertices = numpy.empty((8, 3))
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
        
    print(edges)
    return edges """