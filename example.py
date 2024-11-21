import pygame
import numpy as np

def homothety(center, point, ratio):
    return ratio*np.array(point) + (1-ratio)*np.array(center)

#print(homothety([1, -2], [1, 1], 2))

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

#general setup
pygame.init()
DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
DISPLAY_SURF_MID = (DISPLAY_SURF.get_width()/2,DISPLAY_SURF.get_height()/2)
pygame.display.set_caption('homothety')
clock = pygame.time.Clock()
FPS = 120

cube_sidelength = 50

cube = [[DISPLAY_SURF.get_width()/2, DISPLAY_SURF.get_height()/2],
        [DISPLAY_SURF.get_width()/2 + cube_sidelength, DISPLAY_SURF.get_height()/2],
        [DISPLAY_SURF.get_width()/2, DISPLAY_SURF.get_height()/2 + cube_sidelength],
        [DISPLAY_SURF.get_width()/2 + cube_sidelength, DISPLAY_SURF.get_height()/2 + cube_sidelength]]

run = True
while run:
    # delta-time to achieve constant pixel/second speed of objects on display regardless of hardware specs
    dt = clock.tick(FPS) / 1000

    mouse_pos = pygame.mouse.get_pos()

    # event loop
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                for vertice in range(4):
                    cube[vertice] = homothety(mouse_pos, vertice, 2)
            if event.button == 5:
                for vertice in range(4):
                    cube[vertice] = homothety(mouse_pos, vertice, -2)
            for vertice in cube:
                print(vertice)

    for vertice in cube:
        pygame.draw.circle(DISPLAY_SURF, "blue", vertice, 2)

    pygame.display.update()

pygame.quit()