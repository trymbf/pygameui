# Image

The Image component displays images on the screen with customizable appearance.

## Basic Usage

```python
image = pygameui.Image(
    position=(100, 100),
    src="path/to/image.png"
)
```

## Properties

```python
position: tuple[int, int],
src: str,
width: int = 0,
height: int = 0,
scale: int = 1,
centered: bool = False
```

- `position`: Tuple of (x, y) coordinates
- `src`: Path to the image file
- `width`: Width to resize the image to, 0 indicates using original width (modified by scale)
- `height`: Height to resize the image to, 0 indicates using original height (modified by scale)
- `scale`: Factor to scale the image by compared to the original size, applies when width and height are not set
- `centered`: If True, the image is centered on the provided position

## Methods

All methods inherited from the [Element](element.md) class.

### Setters

```python
set_image(src: str) -> None
scale(scale: int) -> None
```

- `set_image`: Change the displayed image
- `scale`: Change the scale of the image

### Getters

```python
get_image() -> pygame.Surface
get_scale() -> int
```

- `get_image`: Get the current image surface
- `get_scale`: Get the current scale factor

## Example

A simple example demonstrating image display and scaling.

```python
import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Image path - adjust to your image location
image_path = "path/to/your/image.png"

# Create a basic image
logo = pygameui.Image(
    position=(400, 200),
    src=image_path,
    centered=True
)

# Create a scaled image
small_logo = pygameui.Image(
    position=(200, 400),
    src=image_path,
    scale=0.5,
    centered=True
)

# Create a sized image
sized_logo = pygameui.Image(
    position=(600, 400),
    src=image_path,
    width=150,
    height=100,
    centered=True
)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Reset screen
    screen.fill((30, 30, 30))  # Dark background

    # Update images
    logo.update()
    small_logo.update()
    sized_logo.update()

    # Draw images
    logo.draw(screen)
    small_logo.draw(screen)
    sized_logo.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
