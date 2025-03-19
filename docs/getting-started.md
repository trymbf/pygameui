# Getting Started with PygameUI

## Installation
Ensure you have Python and PyGame installed.

Start by downloading the PyGameUI python file from the [releases page](https://github.com/trymbf/pygameui/releases).

Then place the PyGameUI file in the same folder as your project files.

![gif of putting the file in the same folder](https://trymbf.github.io/pygameui/assets//gifs//add_pygameui.gif)

## Basic Structure

Every PygameUI application follows this basic structure:

```python
import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((width, height))

# Create UI elements
ui_element = pygameui.Element(position=(x, y))

# Main loop
running = True
while running:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Update and draw
    screen.fill(background_color)
    ui_element.update()
    ui_element.draw(screen)
    pygame.display.flip()
```
