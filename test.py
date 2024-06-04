import pygame, sys
import pygameui

pygame.init()

win = pygame.display.set_mode((500, 500))

my_element = pygameui.Element((250, 250), content="Im movi'n")

# Button
clickable_elements =[]
button = pygameui.Element((250, 100), content="Hold me to move")
clickable_elements.append(button)

clock = pygame.time.Clock()
while True:
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Button click
    if button.is_clicked(clickable_elements):
        my_element.move_to(250, 400)
    else:
        my_element.move_to(250, 250)

    # Draw element
    my_element.draw(win)
    button.draw(win)

    pygame.display.flip()
    clock.tick(60)