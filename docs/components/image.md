# Image

The Image component displays images on the screen with customizable appearance.

## Basic Usage

```python
# Create an image element
image = pygameui.Image(
    position=(100, 100),
    src="path/to/image.png",
    centered=True  # Center the image at the position
)

# In the main loop
image.update(events)  # events parameter for API consistency
image.draw(screen)
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

- `position`: Tuple of (x, y) coordinates for placing the image
- `src`: Path to the image file (relative or absolute)
- `width`: Width to resize the image to in pixels, 0 indicates using original width (modified by scale)
- `height`: Height to resize the image to in pixels, 0 indicates using original height (modified by scale)
- `scale`: Factor to scale the image by compared to the original size (1 = original size, 2 = double size), only applies when width and height are not set
- `centered`: If True, the image is centered on the provided position; otherwise, the top-left corner is at the position

## Methods

All methods inherited from the [Element](element.md) class.

### Update Method

```python
update(events=None) -> None
```

- `update`: Updates the image element's state including animations. The `events` parameter is included for API consistency with other components but is not used by the Image class.

### Setters

```python
set_image(src: str) -> None
scale(scale: int) -> None
```

- `set_image`: Change the displayed image to a new image file
- `scale`: Change the scale factor of the image relative to its original size

### Getters

```python
get_image() -> pygame.Surface
get_scale() -> int
```

- `get_image`: Get the current pygame Surface containing the image
- `get_scale`: Get the current scale factor applied to the image
