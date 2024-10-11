import numpy, math, pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
run = True
dt = 0
alpha = 0
beta = 0
gamma = 0

SQUARE_SIDELENGTH = 50

def translation(p, v = (screen.get_width()/2, screen.get_height()/2, 0)):
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

def square(c = SQUARE_SIDELENGTH):
    lst = []
    for i in [0, c]:
        for j in [0, c]:
            for k in [0, c]:
                lst.append((i, j, k))
    return lst

square_side_coords = square()

def draw():
    for i in square_side_coords:
        coords_init = xy_projection(translation(rotation(translation(i, (-SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2)), alpha, beta, gamma)))
        for j in square_side_coords:
            coords_fin = xy_projection(translation(rotation(translation(j, (-SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2)), alpha, beta, gamma)))
            if numpy.linalg.norm(numpy.array(i)-numpy.array(j)) == SQUARE_SIDELENGTH:
                pygame.draw.line(screen, "red", coords_init, coords_fin)

while run:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    draw()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        alpha -= 1 * dt
    if keys[pygame.K_s]:
        alpha += 1 * dt
    if keys[pygame.K_a]:
        beta -= 1 * dt
    if keys[pygame.K_d]:
        beta += 1 * dt
    if keys[pygame.K_e]:
        gamma -= 1 * dt
    if keys[pygame.K_q]:
        gamma += 1 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()