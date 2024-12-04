import pygame, sys
import pygameui

pygame.init()

win = pygame.display.set_mode((500, 500))

test = pygameui.Element((100, 100), 100, 100, (255, 0, 0))

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