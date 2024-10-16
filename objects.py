import numpy as np
import transformations as t
import pygame

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
        self.alpha = 0
        self.beta = 0
        self.gamma = 0
    
    def vertices(self):
        vertices_matrix = np.array([[0, 0, 0], [0, 0, self.side_length], [0, self.side_length, 0], [0, self.side_length, self.side_length], [self.side_length, 0, 0], [self.side_length, 0, self.side_length], [self.side_length, self.side_length, 0], [self.side_length, self.side_length, self.side_length]])
        return vertices_matrix

    def center_of_mass(self):
        # We consider the solid to be a set of points in space, all of them with the same constant mass.
        # This set of points will be the vertices of the Object.
        coords = np.sum(self.vertices, axis=0)/len(self.vertices)
        return coords

    def edges(self):
        edges_matrix = np.zeros((8, 4, 3))
        for i in range(len(self.vertices)):
            edges_matrix[i][0] = self.vertices[i]
            k=1
            for j in range(len(self.vertices)):
                if np.linalg.norm(self.vertices[j]-edges_matrix[i][0]) == self.side_length:
                    edges_matrix[i][k] = self.vertices[j]
                    k+=1
        return edges_matrix
    
    def draw(self, display, pos):
        for i in range(len(self.edges)):
            p_init = t.xy_projection(t.translation(t.rotation(t.translation(self.edges[i][0], -self.center_of_mass), self.alpha, self.beta, self.gamma), pos))
            for j in range(len(self.edges[i])):
                p_fin = t.xy_projection(t.translation(t.rotation(t.translation(self.edges[i][j], -self.center_of_mass), self.alpha, self.beta, self.gamma), pos))
                pygame.draw.line(display, "red", p_init, p_fin)

    def rotate(self, alpha, beta, gamma):
        self.yaw(alpha)
        self.pitch(beta)
        self.roll(gamma)

    def yaw(self, deg):
        self.alpha = deg
    
    def pitch(self, deg):
        self.beta = deg

    def roll(self, deg):
        self.gamma = deg