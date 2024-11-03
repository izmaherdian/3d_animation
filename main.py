import pygame
import objects as o

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen_midpos = (screen.get_width()/2, screen.get_height()/2)
clock = pygame.time.Clock()
run = True
dt = 0

cube = o.Cube(100)
torus = o.Torus(20, 50)

while run:
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # fill the screen with a color to wipe away anything from last frame
    
    screen.fill("black")

    cube.update(dt)
    
    print(cube.vertices)
    
    cube.draw(screen, screen_midpos)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()