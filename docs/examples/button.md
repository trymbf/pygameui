# Button Example

This example demonstrates how to create and interact with different styles of buttons in PygameUI.

## Features Demonstrated

- Creating buttons with different styles
- Handling button clicks
- Updating UI elements based on user interaction
- Customizing button colors, text, and borders

## Code Walkthrough

### Setting Up

First, we initialize Pygame and create a screen:

```python
import pygame
import pygameui

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
```

### Creating UI Elements

We create a title and three different button styles:

```python
# Create a title
title = pygameui.Text(
    position=(400, 100),
    content="Button Example",
    color=(255, 255, 255),
    font_size=36,
    centered=True
)

# Create three button styles: primary, secondary, and danger
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
```

### Main Loop

In our main loop, we handle events, update UI elements, and respond to user interactions:

```python
# Main loop
running = True
while running:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Reset screen
    screen.fill((30, 30, 30))
    
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
```

## Button Customization Options

The Button class offers many customization options:

- **Colors**: Background color, hover color, click color
- **Text**: Text content, color, font, size
- **Shape**: Border radius for rounded corners
- **Size**: Width and height
- **Position**: X, Y coordinates (can be centered)

## Full Example Code

See the complete [button_example.py](https://github.com/trymbf/pygameui/blob/main/examples/button_example.py) file in the examples directory.

```python
# See full implementation in examples/button_example.py
```