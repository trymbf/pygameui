# Text Element

The Text class provides text rendering capabilities with customizable fonts and styles.

## Basic Usage

```python
text = pygameui.Text(
    position=(100, 100),
    content="Hello World",
    color=(255, 255, 255),
    font_size=20,
    font_family="Arial",
    centered=True
)
```

## Properties

```python
position: tuple[int, int],
content: str,
color: tuple[int, int, int] = (255, 255, 255),
font_size: int = 20,
font_family: str = "Arial",
width: int = 0,
height: int = 0,
anti_aliasing: bool = True,
centered: bool = False
```

- `position`: Tuple of (x, y) coordinates
- `content`: The text string to display
- `color`: RGB tuple for text color
- `font_size`: Size of the text
- `font_family`: Font family to use
- `width`: Width of the text box (0 for auto)
- `height`: Height of the text box (0 for auto)
- `anti_aliasing`: If True, the text is anti-aliased meaning smoother edges
- `centered`: If True, the text is centered on the provided position

## Methods

All methods inherited from the [Element](element.md) class.

(Some methods may not be applicable to the Image class, but are included for consistency.)

### Setters

```python
set_content(content: str) -> None
set_color(color: tuple[int, int, int]) -> None
set_font_size(font_size: int) -> None
set_font_family(font_family: str) -> None
```

- `set_content`: Set the text content
- `set_color`: Set the text color
- `set_font_size`: Set the font size
- `set_font_family`: Set the font family

### Getters

```python
get_content() -> str
```

- `get_content`: Get the current text content

## Font Support

Supported font families:

- System fonts
- Custom TTF fonts
- Default pygame fonts

## Example

Demonstrating different text styles and animations.

```python
import pygame
import pygameui
import math

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create different text elements
title = pygameui.Text(
    position=(400, 100),
    content="PyGame UI Text Examples",
    color=(255, 255, 255),
    font_size=32,
    font_family="Arial",
    centered=True
)

normal_text = pygameui.Text(
    position=(400, 200),
    content="Regular Text",
    color=(220, 220, 220),
    font_size=20,
    centered=True
)

colored_text = pygameui.Text(
    position=(400, 250),
    content="Colored Text",
    color=(100, 200, 255),  # Light blue
    font_size=20,
    centered=True
)

animated_text = pygameui.Text(
    position=(400, 350),
    content="Animated Text",
    color=(255, 200, 100),  # Yellow/orange
    font_size=24,
    centered=True
)

# Set up animation for the animated text
animated_text.flow(
    start_position=(300, 350),
    end_position=(500, 350),
    time=2000,  # 2 seconds
    loop=True
)
animated_text.set_animate(True)

# Main loop
running = True
start_time = pygame.time.get_ticks()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate time for color animation
    current_time = pygame.time.get_ticks()
    time_factor = (current_time - start_time) / 1000  # Convert to seconds

    # Create a pulsing color effect
    r = int(127 + 127 * math.sin(time_factor))
    g = int(127 + 127 * math.sin(time_factor + 2))
    b = int(127 + 127 * math.sin(time_factor + 4))

    # Update the color of the colored text
    colored_text.set_color((r, g, b))

    # Reset screen
    screen.fill((30, 30, 30))

    # Update text elements
    title.update()
    normal_text.update()
    colored_text.update()
    animated_text.update()

    # Draw text elements
    title.draw(screen)
    normal_text.draw(screen)
    colored_text.draw(screen)
    animated_text.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
