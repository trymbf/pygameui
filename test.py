import pygame
import pygameui

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Login Form")

username = pygameui.Text((250, 250), "trymbf", (250, 0,0))

run = True
while run:
    events = pygame.event.get()
    # Allow user to close the window
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    # Update elements
    username.update()

    # Draw everything
    screen.fill((50, 50, 50))
    username.draw(screen)

    # Update screen
    pygame.display.flip()