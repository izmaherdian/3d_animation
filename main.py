import pygame
import objects as o

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen_midpos = (screen.get_width()/2, screen.get_height()/2)
clock = pygame.time.Clock()
run = True
dt = 0
alpha = 0
beta = 0
gamma = 0

cub = o.Cube(50)

while run:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    cub.rotate(alpha, beta, gamma)

    cub.draw(screen, screen_midpos, "blue")

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()