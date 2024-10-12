import numpy, pygame
import transformations as t

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
run = True
dt = 0
alpha = 0
beta = 0
gamma = 0

SQUARE_SIDELENGTH = 50

""" def square(c = SQUARE_SIDELENGTH):
    lst = []
    for i in [0, c]:
        for j in [0, c]:
            for k in [0, c]:
                lst.append((i, j, k))
    return lst

square_side_coords = square() """

# El que vull jo és tenir diverses funcions que donin els punts necessaris per dibuixar una certa figura
# (cub, torus, etc), aquestes funcions rebrien el nom de square, torus, ... Llavors, aquestes funcions no
# retornen només una llista de punts, sinó que vull que retorni una matriu on cada element de la primera
# fila està unit mitjançant una recta amb cada element d'aquella mateixa columna. Així doncs en el cas
# del cub, els punts (0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1) estan units mitjançant una recta. D'aquesta
# manera, donada una llista de punts cal trobar una regla per poder crear aquesta matriu (que no té perquè ser quadrada).
# Un cop tenim això, la funció draw ha de dibuixar les rectes entre els punts que estan units mirant dins a matriu. 
# Evidentment cal dibuixar les rectes després de transformar els punts.

def square():
    SIDE_LENGTH = 50
    vertices =[(0, 0, 0), (0, 0, 50), (0, 50, 0), (0, 50, 1), (50, 0, 0), (50, 0, 50), (50, 50, 0), (50, 50, 50)]
    edges = [[(0, 0, 0), (0, 0, 50), (0, 50, 0), (50, 0, 0)],
                [(0, 0, 50), (50, 0, 50), (0, 50, 50)],
                [(0, 50, 0), (0, 50, 50), (50, 50, 0)], 
                [(0, 50, 50), (50, 50, 50)], 
                [(50, 0, 0), (50, 0, 50), (50, 50, 0)], 
                [(50, 0, 50), (50, 50, 50)],
                [(50, 50, 0), (50, 50, 50)]]
        
    return edges

edges = square()

def draw():
    for fila in range(0, len(edges)):
        for element in range(0, len(edges[fila])):
            pivot = t.xy_projection(t.translation(t.rotation(t.translation(edges[fila][0], (-SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2)), alpha, beta, gamma), (screen.get_width()/2, screen.get_height()/2, 0)))
            coords_fin = t.xy_projection(t.translation(t.rotation(t.translation(edges[fila][element], (-SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2)), alpha, beta, gamma), (screen.get_width()/2, screen.get_height()/2, 0)))
            pygame.draw.line(screen, "red", pivot, coords_fin)

""" def draw():
    for i in square_side_coords:
        coords_init = t.xy_projection(t.translation(t.rotation(t.translation(i, (-SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2)), alpha, beta, gamma), (screen.get_width()/2, screen.get_height()/2, 0)))
        for j in square_side_coords:
            coords_fin = t.xy_projection(t.translation(t.rotation(t.translation(j, (-SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2)), alpha, beta, gamma), (screen.get_width()/2, screen.get_height()/2, 0)))
            if numpy.linalg.norm(numpy.array(i)-numpy.array(j)) == SQUARE_SIDELENGTH:
                pygame.draw.line(screen, "red", coords_init, coords_fin) """

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