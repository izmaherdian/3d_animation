import numpy as np
import transformations as t
import pygame

# El proper pas seria implementar les funcions dins la classe pare

class Object:

    def __init__(self):
        self.alpha = 0
        self.beta = 0
        self.gamma = 0

    def center_of_mass(self):
        # We consider the solid to be a set of points in space, all of them with the same constant mass.
        # This set of points will be the vertices of the Object.
        coords = np.sum(self.vertices, axis=0)/len(self.vertices)
        return coords

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

    def draw(self, display, pos, color):
        for i in range(len(self.edges)):
            p_init = t.xy_projection(t.translation(t.rotation(t.translation(self.edges[i][0], -self.center_of_mass), self.alpha, self.beta, self.gamma), pos))
            for j in range(len(self.edges[i])):
                p_fin = t.xy_projection(t.translation(t.rotation(t.translation(self.edges[i][j], -self.center_of_mass), self.alpha, self.beta, self.gamma), pos))
                pygame.draw.aaline(display, color, p_init, p_fin)


class Cube(Object):

    def __init__(self, side_length, mass = 1):
        super().__init__()
        self.side_length = side_length
        self.vertices = self.vertices()
        self.center_of_mass = self.center_of_mass()
        self.edges = self.edges()
    
    def vertices(self):
        vertices_matrix = np.zeros((8, 3))
        i=0
        for a in [0, self.side_length]:
            for b in [0, self.side_length]:
                for c in [0, self.side_length]:
                    vertices_matrix[i] = [a, b, c]
                    i+=1
        return vertices_matrix

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

class Torus(Object):

    def __init__(self, r, R):
        super().__init__()
        self.r = r
        self.R = R
        self.r_density = 16
        self.R_density = 16
        self.vertices = self.vertices()
        self.center_of_mass = self.center_of_mass()
        self.edges = self.edges()
        
    def vertices(self):
        i = 0
        vertices_matrix = np.zeros((self.r_density*self.R_density, 3))
        for k in range(self.R_density):
            for n in range(self.r_density):
                vertices_matrix[i] = [(self.R + self.r * np.cos(2*np.pi/self.r_density*n)) * np.cos(2*np.pi/self.R_density*k), (self.R + self.r * np.cos(2*np.pi/self.r_density*n)) * np.sin(2*np.pi/self.R_density*k), self.r * np.sin(2*np.pi/self.r_density*n)]
                i += 1
        return vertices_matrix
    
    def edges(self):
        edges_matrix = np.zeros((self.r_density*self.R_density, 5, 3))
        for i in range(len(self.vertices)):
            k = 0
            edges_matrix[i][k] = self.vertices[i]
            for j in range(len(self.vertices)):
                if i%self.r_density == 0:
                    if j == (i+1)%(self.r_density*self.r_density) or (j-i)%(self.r_density*self.r_density) == 15 or j == (i+self.r_density)%(self.r_density*self.r_density) or j == (i-self.r_density)%(self.r_density*self.r_density):
                        k += 1
                        edges_matrix[i][k] = self.vertices[j]    
                elif i%self.r_density == -1%self.r_density:
                    if (j+self.r_density-1) == i or (j+1) == i or j == (i+self.r_density)%(self.r_density*self.r_density) or j == (i-self.r_density)%(self.r_density*self.r_density):
                        k += 1
                        edges_matrix[i][k] = self.vertices[j]
                else:
                    if j == (i+1)%(self.r_density*self.r_density) or j == (i-1)%(self.r_density*self.r_density) or j == (i+self.r_density)%(self.r_density*self.r_density) or j == (i-self.r_density)%(self.r_density*self.r_density):
                        k += 1
                        edges_matrix[i][k] = self.vertices[j]
        return edges_matrix