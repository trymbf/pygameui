# Image Element

The Image class allows you to display images in your UI.

## Basic Usage

```python
image = pygameui.Image(
    position=(100, 100),
    image_path="path/to/image.png",
)
```

## Properties

```python
position: tuple[int, int],
image_path: str,
width: int = 0,
height: int = 0,
scale:int = 1,
centered: bool = False
```

- `position`: Tuple of (x, y) coordinates
- `image_path`: Path to the image file
- `width`: Width of the image (optional, 0 for auto, overrides scale)
- `height`: Height of the image (optional, 0 for auto, overrides scale)
- `scale`: Scale factor for the image (optional, default is 1)
- `centered`: If True, the image is centered on the provided position

## Supported Formats

- PNG (recommended)
- JPEG
- GIF (first frame only)
- BMP

## Image Scaling

Three ways to control image size:

1. Original size (no parameters)
2. Scale factor (`scale` parameter)
3. Exact dimensions (`width` and `height` parameters)

## Methods

All methods inherited from the [Element](element.md) class.

(Some methods may not be applicable to the Image class, but are included for consistency.)

### Setters

```python
set_image(image_path: str) -> None
scale(scale: int) -> None
```

- `set_image`: Set a new image for the element
- `scale`: Set a new scale for the image

### Getters

```python
get_image() -> pygame.Surface
get_scale() -> int
```

- `get_image`: Get the current image of the element
- `get_scale`: Get the current scale of the image

## Example

Simple example of loading and displaying an image with hover effects.

```python
import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create an image
image = pygameui.Image(
    position=(400, 300),
    image_path=r"path/to/img.png",  # Replace with your image path
    width=200,
    height=200,
    centered=True
)

# Set up a hover animation using scale
original_pos = image.get_position()
hover_text = pygameui.Text(
    position=(400, 500),
    content="Hover over the image!",
    color=(255, 255, 255),
    font_size=20,
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
    screen.fill((30, 30, 30))

    # Update elements
    image.update()
    hover_text.update()

    # Check for hover
    if image.is_hovered():
        # When hovered, make the image slightly larger
        image.scale(1.1)
        hover_text.set_content("Image is hovered!")
    else:
        # Return to original size
        image.scale(1)
        hover_text.set_content("Hover over the image!")

    # Draw elements
    image.draw(screen)
    hover_text.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
