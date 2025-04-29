# Checkbox

Checkboxes provide toggleable interface elements with various styles for indicating selection state.

## Basic Usage

```python
checkbox = pygameui.Checkbox(
    position=(100, 100),
    width=50,
    height=50,
    style="checkmark",
    background_color=(220, 220, 220)
)

# In the main loop
checkbox.update(events)  # events parameter for API consistency
checkbox.draw(screen)

# Check the checkbox state
if checkbox.is_checked():
    print("Checkbox is checked!")
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

# Text labels for checkboxes
checkbox_labels = [
    pygameui.Text((200, 250), "Checkmark", (255, 255, 255), centered=True),
    pygameui.Text((300, 250), "Cross", (255, 255, 255), centered=True),
    pygameui.Text((400, 250), "Circle", (255, 255, 255), centered=True),
    pygameui.Text((500, 250), "Square", (255, 255, 255), centered=True)
]

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

    # Update checkboxes with events for proper interaction
    checkboxes = [checkmark_box, cross_box, circle_box, square_box]
    for checkbox in checkboxes:
        checkbox.update(events)
        
        # Display status for each checkbox
        if checkbox.is_checked():
            status_text = f"{checkbox._checked_style} is ON"
        else:
            status_text = f"{checkbox._checked_style} is OFF"
            
        # Draw checkboxes and status
        checkbox.draw(screen)

    # Draw labels
    for label in checkbox_labels:
        label.update()
        label.draw(screen)
        
    # Display instructions
    instructions = pygameui.Text(
        (400, 100), 
        "Click on checkboxes to toggle them", 
        (200, 200, 200),
        font_size=24,
        centered=True
    )
    instructions.update()
    instructions.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
