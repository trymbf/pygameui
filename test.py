import pygame, sys, time, string
import pygameui as pgui

pygame.init()

win = pygame.display.set_mode((500, 500))

# Creating an input
input = pgui.Input((100, 100))

clock = pygame.time.Clock()
while True:
    win.fill((0, 0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    input.work(events, [input])
    input.draw(win)

    # Updating the display
    pygame.display.flip()
    clock.tick(60)