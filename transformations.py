import numpy, math

def translation(p, v):
    coords = numpy.array([p[0] + v[0], p[1] + v[1], p[2] + v[2]])
    return coords

def rotation(p, alpha, beta, gamma):
    yaw_matrix = numpy.array([[math.cos(alpha), -math.sin(alpha), 0], [math.sin(alpha), math.cos(alpha), 0], [0, 0, 1]])
    pitch_matrix = numpy.array([[math.cos(beta), 0, math.sin(beta)], [0, 1, 0], [-math.sin(beta), 0, math.cos(beta)]])
    roll_matrix = numpy.array([[1, 0, 0], [0, math.cos(gamma), -math.sin(gamma)], [0, math.sin(gamma), math.cos(gamma)]])
    rotation_matrix = yaw_matrix @ pitch_matrix @ roll_matrix
    coords = rotation_matrix @ numpy.array([p[0], p[1], p[2]])
    return coords

def xy_projection(p):
    xy_projection_matrix = numpy.array([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
    coords = xy_projection_matrix @ numpy.array([p[0], p[1], p[2]])
    coords = coords[:-1]
    return coords