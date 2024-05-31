import pygame, sys
import pygameui

pygame.init()

win = pygame.display.set_mode((500, 500))

# List of clickable elements
clickable_elements = []

# Create a button
button = pygameui.Element((250, 250), content="Click me!")
clickable_elements.append(button)

clock = pygame.time.Clock()
while True:
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check if the button was clicked
    if button.was_clicked(clickable_elements):
        print("Button was clicked!")

    # Draw the button
    button.draw(win)

    pygame.display.flip()
    clock.tick(60)