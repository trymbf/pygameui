import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create dropdown menu
dropdown = pygameui.Table(
    (300, 300),
    width=300,
    height=100,
    content=[["Option 1", "Option 2", "Option 3"], ["Option 4", "Option 5", "Option 6"]],
    color=(255,0,0),
    border_color=(0, 255, 0),
    border_width=1,
)

# Main loop
running = True
while running:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Reset screen
    screen.fill((30, 30, 30))  # Dark background

    # Update dropdown
    dropdown.update()

    # Draw elements
    dropdown.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)