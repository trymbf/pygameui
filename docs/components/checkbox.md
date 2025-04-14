# Checkbox

Checkboxes provide toggleable interface elements with various styles for indicating selection state.

## Basic Usage

```python
checkbox = pygameui.Checkbox(
    position=(100, 100),
    style="checkmark"
)
```

## Properties

```python
position: tuple[int, int],
width: int = 50,
height: int = 50,
style: Literal["checkmark", "cross", "circle", "square", "none"] = "checkmark",
unchecked_style: Literal["checkmark", "cross", "circle", "square", "none"] = "none",
mark_width: int = 5,
color: tuple[int, int, int] = (100, 255, 100),
background_color: tuple[int, int, int] = (200, 200, 200),
border_radius: int = 0,
border_color: tuple[int, int, int] = (0, 0, 0),
border_width: int = 2,
centered: bool = False
```

- `position`: Tuple of (x, y) coordinates
- `width`: Width of the checkbox
- `height`: Height of the checkbox
- `style`: The style of mark when checked ("checkmark", "cross", "circle", "square", or "none")
- `unchecked_style`: The style of mark when unchecked ("checkmark", "cross", "circle", "square", or "none")
- `mark_width`: Width of the mark lines/borders
- `color`: Color of the mark
- `background_color`: Color of the checkbox background
- `border_radius`: Radius for rounded corners
- `border_color`: Color of the checkbox border
- `border_width`: Width of the border
- `centered`: If True, the checkbox is centered on the provided position

## Methods

All methods inherited from the [Element](element.md) class, plus:

### Setters

```python
set_checked(checked: bool) -> None
disable() -> None
enable() -> None
```

- `set_checked`: Set the checked state of the checkbox
- `disable`: Disable the checkbox, preventing user interaction
- `enable`: Enable the checkbox, allowing user interaction

### Getters

```python
is_checked() -> bool
is_enabled() -> bool
```

- `is_checked`: Get the current checked state of the checkbox
- `is_enabled`: Get whether the checkbox is currently enabled

## Example

Simple example demonstrating different checkbox styles and interactions.

```python
import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create checkboxes with different styles
checkmark_box = pygameui.Checkbox(
    position=(200, 200),
    style="checkmark",
    color=(50, 200, 50),  # Green mark
    width=40,
    height=40,
    centered=True
)

cross_box = pygameui.Checkbox(
    position=(300, 200),
    style="cross",
    color=(200, 50, 50),  # Red mark
    width=40,
    height=40,
    centered=True
)

circle_box = pygameui.Checkbox(
    position=(400, 200),
    style="circle",
    color=(50, 50, 200),  # Blue mark
    width=40,
    height=40,
    centered=True
)

square_box = pygameui.Checkbox(
    position=(500, 200),
    style="square",
    color=(200, 200, 50),  # Yellow mark
    width=40,
    height=40,
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

    # Update checkboxes
    for checkbox in [checkmark_box, cross_box, circle_box, square_box]:
        checkbox.update()

    # Draw checkboxes
    for checkbox in [checkmark_box, cross_box, circle_box, square_box]:
        checkbox.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
