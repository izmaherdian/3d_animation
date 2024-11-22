import pygame
import numpy as np

def translation(point, vector):
    return np.array(point) + np.array(vector)

def homothety(center, point, ratio = 1.01):
    return ratio*np.array(point) + (1-ratio)*np.array(center)

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

#general setup
pygame.init()
DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
DISPLAY_SURF_MID = [DISPLAY_SURF.get_width()/2, DISPLAY_SURF.get_height()/2]
pygame.display.set_caption('homothety')
clock = pygame.time.Clock()
FPS = 120

cube_sidelength = 50

cube = [[0, 0],
        [cube_sidelength, 0],
        [0, cube_sidelength],
        [cube_sidelength, cube_sidelength]]

for i in range(len(cube)):
    cube[i] = translation(cube[i], DISPLAY_SURF_MID)

run = True
while run:
    # delta-time to achieve constant pixel/second speed of objects on display regardless of hardware specs
    dt = clock.tick(FPS) / 1000

    DISPLAY_SURF.fill("black")

    mouse_pos = pygame.mouse.get_pos()

    # event loop
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                for i in range(len(cube)):
                    cube[i] = homothety(mouse_pos, cube[i])
            if event.button == 5:
                for i in range(len(cube)):
                    cube[i] = homothety(mouse_pos, cube[i], -1.01)

    for vertice in cube:
        pygame.draw.circle(DISPLAY_SURF, "blue", vertice, 2)

    pygame.display.update()

pygame.quit()