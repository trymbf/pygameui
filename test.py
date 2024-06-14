import pygame, sys
import pygameui

pygame.init()

win = pygame.display.set_mode((500, 500))

# Create input element
my_input = pygameui.Input((250, 250))

# Create clickable elements list
clickable_elements = [my_input]

clock = pygame.time.Clock()
while True:
    win.fill((0, 0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Make input element works
    my_input.work(events, clickable_elements)

    # Draw input element
    my_input.draw(win)

    pygame.display.flip()
    clock.tick(60)