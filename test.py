import pygame, sys
import pygameui

pygame.init()

win = pygame.display.set_mode((500, 500))

# Creating an input
example_input = pygameui.Input((200, 200))

# Creating a list of all clickable elements
clickable_elements = [example_input]

clock = pygame.time.Clock()
while True:
    win.fill((0, 0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Give the input funcionality
    example_input.work(events, clickable_elements)

    # Obtaining the input value
    input_text = example_input.getText()
    print("You have written: " + input_text)

    # Drawing the input
    example_input.draw(win)

    # Updating the display
    pygame.display.flip()
    clock.tick(60)