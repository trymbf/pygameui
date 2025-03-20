import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600)) # Set your own width and height

# Create UI elements
ui_element = pygameui.Button(position=(250, 250), width=200, height=50, centered=True)

# Main loop
running = True
while running:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ui_element.set_label("Right")

            if event.key == pygame.K_LEFT:
                ui_element.set_label("Left")

    # Reset screen
    screen.fill((0,0,0))
  
    # Update element, moves, checks actions etc
    ui_element.update()

    # Draw element on screen
    ui_element.draw(screen)

    # Update pygame display
    pygame.display.flip()
