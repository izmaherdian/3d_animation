import numpy as np

def translation(point, vector):
    if len(vector) == 2:
        vector = np.array([vector[0], vector[1], 0])
    return point + vector

def rotation(point, alpha, beta, gamma):
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