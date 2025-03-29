# Button

Buttons provide clickable interface elements with hover effects.

## Basic Usage

```python
button = pygameui.Button(
    position=(100, 100),
)
```

## Properties

```python
position: tuple[int, int],
width: int = 200,
height: int = 50,
border_radius: int = 10,
content: str = "Click me.",
color: tuple[int, int, int] = (255, 255, 255),
hover_color: tuple[int, int, int] = (200, 200, 200),
click_color: tuple[int, int, int] = (150, 150, 150),
text_color: tuple[int, int, int] = (100, 100, 100),
text_hover_color: tuple[int, int, int] = (0, 0, 0),
text_click_color: tuple[int, int, int] = (0, 0, 0),
font_size: int = 20,
font_family: str = "Arial",
centered: bool = False
```

- `position`: Tuple of (x, y) coordinates
- `width`: Width of the button
- `height`: Height of the button
- `border_radius`: Radius for rounded corners
- `content`: Text displayed on the button
- `color`: Default button backgroundcolor
- `hover_color`: Backgroundcolor when the button is hovered over
- `click_color`: Backgroundcolor when the button is clicked
- `text_color`: Color of the text when not hovered
- `text_hover_color`: Color of the text when hovered over
- `text_click_color`: Color of the text when clicked
- `font_size`: Size of the text font
- `font_family`: Font family for the text
- `centered`: If True, the button is centered on the provided position

## Methods

All methods inherited from the [Element](element.md) class.

(Some methods may not be applicable to the Image class, but are included for consistency.)

### Setters

```python
set_label(label: str) -> None
set_color(color: tuple[int, int, int]) -> None
set_hover_color(color: tuple[int, int, int]) -> None
set_click_color(color: tuple[int, int, int]) -> None
set_text_color(color: tuple[int, int, int]) -> None
set_text_hover_color(color: tuple[int, int, int]) -> None
set_text_click_color(color: tuple[int, int, int]) -> None
```

- `set_label`: Set the text displayed on the button
- `set_color`: Set the default button background color
- `set_hover_color`: Set the background color when the button is hovered over
- `set_click_color`: Set the background color when the button is clicked
- `set_text_color`: Set the color of the buttonlabel when not hovered
- `set_text_hover_color`: Set the color of the buttonlabel when hovered over
- `set_text_click_color`: Set the color of the buttonlabel when clicked

### Mouse and Click Events

See the [Mouse and Click Events](element.md#mouse-and-click-events) section in the Element documentation.

## Example

Simple example of buttons with different styles and functionality.

```python
import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create buttons
primary_button = pygameui.Button(
    position=(400, 200),
    label="Primary Button",
    width=250,
    height=60,
    color=(75, 145, 250),         # Blue
    hover_color=(95, 165, 255),   # Lighter blue
    click_color=(55, 125, 235),   # Darker blue
    text_color=(255, 255, 255),   # White text
    font_size=24,
    border_radius=15,
    centered=True
)

secondary_button = pygameui.Button(
    position=(400, 300),
    label="Secondary Button",
    width=250,
    height=60,
    color=(240, 240, 240),        # Light gray
    hover_color=(220, 220, 220),  # Medium gray
    click_color=(200, 200, 200),  # Darker gray
    text_color=(50, 50, 50),      # Dark text
    font_size=24,
    border_radius=15,
    centered=True
)

# Track click status
message = "Click a button!"

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

    # Update buttons
    primary_button.update()
    secondary_button.update()

    # Check for button clicks
    if primary_button.was_clicked():
        print("Primary button clicked!")

    if secondary_button.was_clicked():
        print("Secondary button clicked!")

    # Draw elements
    primary_button.draw(screen)
    secondary_button.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
