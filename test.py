import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Create dropdown menu
dropdown = pygameui.Button(
    (250,250),
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