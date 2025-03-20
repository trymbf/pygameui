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
screen = pygame.display.set_mode((800, 600)) # Set your own width and height

# Create UI elements
ui_element = pygameui.Element(position=(250, 250), width=200, height=50)

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
  
    # Update element, moves, checks actions etc
    ui_element.update()

    # Draw element on screen
    ui_element.draw(screen)

    # Update pygame display
    pygame.display.flip()
```

To add more UI elements, simply create more instances of the `Element` class or its subclasses (like `Button`, `Text`, etc.) and follow the same pattern.

## Example create text

First create a text object:

```python
my_text = pygameui.Text(
    text="Hello World", 
    position=(100, 100), 
    font_size=30, 
    color=(255, 255, 255)
    )
```

And then in the main loop, you would call:

```python
my_text.update()
my_text.draw(screen)
```

And that's it! You now have a text object on your screen. You can customize the text by changing its properties like `font_size`, `color`, and `position`. [See the Text class documentation for more details.](components/text.md)
