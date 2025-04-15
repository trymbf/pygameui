import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((500, 500)) # Set your own width and height

# Create UI elements
ui_element = pygameui.Input(position=(250, 250), centered=False, cursor=False)
test_element = pygameui.Element((10,10), 50,200)

# Control framersaate
clock = pygame.time.Clock()
# Main loop
running = True
while running:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Reset screen
    screen.fill((0,0,0))

    test_element.update()
    test_element.draw(screen)
  
    # Update element, moves, checks actions etc
    ui_element.update(events)

    # Draw element on screen
    ui_element.draw(screen)

    # Update pygame display
    pygame.display.flip()

    # Run at 60 frames pr second
    clock.tick(60)
