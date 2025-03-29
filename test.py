import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create dropdown menu
dropdown = pygameui.DropdownMenu(
    position=(400, 200),
    options=["Option 1", "Option 2", "Option 3"],
    width=250,
    height=50,
    color=(240, 240, 240),
    hover_color=(220, 220, 220),
    text_color=(50, 50, 50),
    centered=True,
    border_radius=5,
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

    # Check for selection
    if dropdown.get_selected_option():
        print(f"Selected: {dropdown.get_selected_option()}")

    # Draw elements
    dropdown.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)