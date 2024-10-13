import pygame
import transformations as t
import objects as o

pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
run = True
dt = 0
alpha = 0
beta = 0
gamma = 0

SQUARE_SIDELENGTH = 50

def draw():
    for fila in range(0, len(edges)):
        for element in range(0, len(edges[fila])):
            pivot = t.xy_projection(t.translation(t.rotation(t.translation(edges[fila][0], (-SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2)), alpha, beta, gamma), (screen.get_width()/2, screen.get_height()/2, 0)))
            coords_fin = t.xy_projection(t.translation(t.rotation(t.translation(edges[fila][element], (-SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2, -SQUARE_SIDELENGTH/2)), alpha, beta, gamma), (screen.get_width()/2, screen.get_height()/2, 0)))
            pygame.draw.line(screen, "red", pivot, coords_fin)

while run:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    edges = o.square()

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