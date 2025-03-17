import pygame, sys
import pygameui

pygame.init()

win = pygame.display.set_mode((500, 500))

test = pygameui.Input((0, 0), hint="Type here")

clock = pygame.time.Clock()
while True:
    win.fill((0, 0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    test.draw(win)
    test.update()

    pygame.display.flip()
    clock.tick(60)