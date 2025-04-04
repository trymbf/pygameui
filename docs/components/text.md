# Text

The Text component displays text on the screen with customizable appearance.

## Basic Usage

```python
text = pygameui.Text(
    position=(100, 100),
    content="Hello, World!"
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
- `content`: The text to display
- `color`: RGB tuple for text color
- `font_size`: Size of the font
- `font_family`: Font family to use
- `width`: Width of the text element, 0 indicates that the width will be the width of the text
- `height`: Height of the text element, 0 indicates that the height will be the height of the text
- `anti_aliasing`: Whether to use anti-aliasing for the text
- `centered`: If True, the text is centered on the provided position

## Methods

All methods inherited from the [Element](element.md) class.

### Setters

```python
set_content(content: str) -> None
set_color(color: tuple[int, int, int]) -> None
set_font_size(font_size: int) -> None
set_font_family(font_family: str) -> None
```

- `set_content`: Change the displayed text
- `set_color`: Change the color of the text
- `set_font_size`: Change the size of the font
- `set_font_family`: Change the font family

### Getters

```python
get_content() -> str
```

- `get_content`: Get the current text content

## Example

A simple example demonstrating text with different styles.

```python
import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create different text elements
title = pygameui.Text(
    position=(400, 100),
    content="PygameUI Text Demo",
    color=(255, 255, 255),
    font_size=40,
    font_family="Arial",
    centered=True
)

subtitle = pygameui.Text(
    position=(400, 180),
    content="Easy text rendering with PygameUI",
    color=(180, 180, 180),
    font_size=24,
    font_family="Arial",
    centered=True
)

body_text = pygameui.Text(
    position=(400, 280),
    content="This component allows you to easily display and\nupdate text in your Pygame applications.",
    color=(220, 220, 220),
    font_size=18,
    font_family="Arial",
    centered=True
)

# Create a text that will change color
animated_text = pygameui.Text(
    position=(400, 400),
    content="Text color can be changed dynamically!",
    color=(255, 255, 0),
    font_size=20,
    font_family="Arial",
    centered=True
)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Animate text color
    t = pygame.time.get_ticks()
    r = int(127 * (1 + (pygame.math.Vector2(1, 0).rotate(t / 10)).x))
    g = int(127 * (1 + (pygame.math.Vector2(1, 0).rotate(t / 10 + 120)).x))
    b = int(127 * (1 + (pygame.math.Vector2(1, 0).rotate(t / 10 + 240)).x))
    animated_text.set_color((r, g, b))

    # Reset screen
    screen.fill((30, 30, 30))  # Dark background

    # Update text elements
    title.update()
    subtitle.update()
    body_text.update()
    animated_text.update()

    # Draw text elements
    title.draw(screen)
    subtitle.draw(screen)
    body_text.draw(screen)
    animated_text.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
