import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create UI elements
title = pygameui.Text(
    position=(400, 100),
    content="Button Example",
    color=(255, 255, 255),
    font_size=36,
    centered=True
)

# Create different styles of buttons
primary_button = pygameui.Button(
    position=(400, 250),
    label="Primary Button",
    width=200,
    height=50,
    color=(75, 145, 250),  # Blue
    hover_color=(95, 165, 255),
    click_color=(55, 125, 235),
    text_color=(255, 255, 255),
    border_radius=8,
    centered=True
)

secondary_button = pygameui.Button(
    position=(400, 325),
    label="Secondary Button",
    width=200,
    height=50,
    color=(240, 240, 240),  # Light gray
    hover_color=(220, 220, 220),
    click_color=(200, 200, 200),
    text_color=(50, 50, 50),
    border_radius=8,
    centered=True
)

danger_button = pygameui.Button(
    position=(400, 400),
    label="Danger Button",
    width=200,
    height=50,
    color=(250, 75, 75),  # Red
    hover_color=(255, 95, 95),
    click_color=(235, 55, 55),
    text_color=(255, 255, 255),
    border_radius=8,
    centered=True
)

status_text = pygameui.Text(
    position=(400, 500),
    content="Click a button to see its action",
    color=(200, 200, 200),
    font_size=18,
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
    
    # Update UI elements
    title.update(events)
    primary_button.update(events)
    secondary_button.update(events)
    danger_button.update(events)
    status_text.update(events)

    # Handle button clicks
    if primary_button.was_clicked():
        status_text.set_content("Primary button was clicked!")
    elif secondary_button.was_clicked():
        status_text.set_content("Secondary button was clicked!")
    elif danger_button.was_clicked():
        status_text.set_content("Danger button was clicked!")
    
    # Draw UI elements
    title.draw(screen)
    primary_button.draw(screen)
    secondary_button.draw(screen)
    danger_button.draw(screen)
    status_text.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit pygame
pygame.quit()