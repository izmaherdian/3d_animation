import numpy as np
import transformations as t
import pygame
import math

# El proper pas seria implementar les funcions dins la classe pare

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
        vertices_matrix = np.zeros((8, 3))
        i=0
        for a in [0, self.side_length]:
            for b in [0, self.side_length]:
                for c in [0, self.side_length]:
                    vertices_matrix[i] = [a, b, c]
                    i+=1
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
    
    def draw(self, display, pos, color):
        for i in range(len(self.edges)):
            p_init = t.xy_projection(t.translation(t.rotation(t.translation(self.edges[i][0], -self.center_of_mass), self.alpha, self.beta, self.gamma), pos))
            for j in range(len(self.edges[i])):
                p_fin = t.xy_projection(t.translation(t.rotation(t.translation(self.edges[i][j], -self.center_of_mass), self.alpha, self.beta, self.gamma), pos))
                pygame.draw.aaline(display, color, p_init, p_fin)

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

class Torus(Object):

    def __init__(self, r, R):
        super().__init__()
        self.r = r
        self.R = R
        self.vertices = self.vertices()
        self.center_of_mass = self.center_of_mass()
        self.alpha = 0
        self.beta = 0
        self.gamma = 0

    def vertices(self):
        # Hi hauria d'haver alguna manera de calcular la densitat en funció de r i R (com de gran és el torus)
        i = 0
        r_density = 16
        R_density = 16
        vertices_matrix = np.zeros((r_density*R_density, 3))
        for k in range(R_density):
            for n in range(r_density):
                vertices_matrix[i] = [(self.R + self.r * math.cos(2*math.pi/r_density*n)) * math.cos(2*math.pi/R_density*k), (self.R + self.r * math.cos(2*math.pi/r_density*n)) * math.sin(2*math.pi/R_density*k), self.r * math.sin(2*math.pi/r_density*n)]
                i+=1
        return vertices_matrix
    
    def center_of_mass(self):
        # We consider the solid to be a set of points in space, all of them with the same constant mass.
        # This set of points will be the vertices of the Object.
        coords = np.sum(self.vertices, axis=0)/len(self.vertices)
        return coords
    
    def edges(self):
        pass
    
    def draw(self, display, pos, color):
        for i in self.vertices:
            p = t.xy_projection(t.translation(t.rotation(t.translation(i, -self.center_of_mass), self.alpha, self.beta, self.gamma), pos))
            pygame.draw.circle(display, color, p, 1)

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