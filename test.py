import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# Create dropdown menu
dropdown = pygameui.DropdownMenu(
    (200, 200),
    ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6", "Option 7", "Option 8"],
    element_width=60,
    element_height=30,
    font_size=15,
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
    dropdown.update(events)

    # Draw elements
    dropdown.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)