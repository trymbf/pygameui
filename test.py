import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Create dropdown menu
dropdown = pygameui.Table(
    (250, 250),
    content=[["Option 1", "Option 2", "Option 3"], ["Option 4", "Option 5", "Option 6"]],
    centered=True
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