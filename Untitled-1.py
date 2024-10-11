import numpy, math, pygame

def translation(x, y, z, dx, dy, dz):
    return type(numpy.array([x + dx, y + dy, z + dz]))

def rotation(x, y, z, alpha, beta, gamma):
    yaw_matrix = numpy.array([[math.cos(alpha), -math.sin(alpha), 0], [math.sin(alpha), math.cos(alpha), 0], [0, 0, 1]])
    pitch_matrix = numpy.array([[math.cos(beta), 0, math.sin(beta)], [0, 1, 0], [-math.sin(beta), 0, math.cos(beta)]])
    roll_matrix = numpy.array([[1, 0, 0], [0, math.cos(gamma), -math.sin(gamma)], [0, math.sin(gamma), math.cos(gamma)]])
    rotation_matrix = yaw_matrix @ pitch_matrix @ roll_matrix
    coords = rotation_matrix @ numpy.array([x, y, z])
    return coords

