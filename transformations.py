import numpy as np

def translation(point, vector):
    if len(vector) == 2:
        vector = np.array([vector[0], vector[1], 0])
    return point + vector

def rotation(point, alpha, beta, gamma):
    "Aquesta rotació actua sobre les coordenades absolutes, és a dir, yaw és una rotació de alpha graus sobre el pla XY"
    "deixant invariant l'eix Z. El pitch, deixa invariant tot vector de la forma (0, 1, 0) i per tant, l'eix Y és invariant."
    "Al roll li passa el mateix però en X."
    yaw_matrix = np.array([[np.cos(alpha), -np.sin(alpha), 0],
                           [np.sin(alpha),  np.cos(alpha), 0],
                           [0            ,              0, 1]])
    pitch_matrix = np.array([[ np.cos(beta), 0, np.sin(beta)],
                             [0            , 1,            0], 
                             [-np.sin(beta), 0, np.cos(beta)]])
    roll_matrix = np.array([[1,             0,              0], 
                            [0, np.cos(gamma), -np.sin(gamma)], 
                            [0, np.sin(gamma),  np.cos(gamma)]])
    rotation_matrix = yaw_matrix @ pitch_matrix @ roll_matrix
    coords = rotation_matrix @ point
    return coords

def xy_projection(point):
    xy_projection_matrix = np.array([[1, 0, 0], 
                                     [0, 1, 0], 
                                     [0, 0, 0]])
    coords = xy_projection_matrix @ point
    coords = coords[:-1]
    return coords

def change_of_basis():
    pass

def homothety():
    pass