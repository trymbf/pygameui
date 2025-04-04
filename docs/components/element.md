# Element

The Element class is the foundation of all UI components in PygameUI.

## Basic Usage

```python
element = pygameui.Element(
    position=(100, 100),
    width=200,
    height=100,
)
```

## Properties

```python
position: tuple[int, int],
width: int,
height: int,
color: tuple[int, int, int] = (255, 255, 255),
border_radius: int = 0,
border_color: tuple[int, int, int] = None,
border_width: int = 2,
centered: bool = False
```

- `position`: Tuple of (x, y) coordinates
- `width`: Width of the element
- `height`: Height of the element
- `color`: RGB tuple for element color
- `border_radius`: Radius for rounded corners
- `border_color`: Color of the element border, if None, the border will not be drawn
- `border_width`: Width of the element border
- `centered`: If True, the element is centered on the provided position

## Methods

### Basic methods

```python
draw(surface: pygame.Surface) -> None
update(_=None) -> None
```

- `draw`: Draws the element on the provided surface.
- `update`: Updates the element's state. This method should be called every frame to ensure animations and events are processed.

### Setters

```python
set_position(position: tuple[int,int]) -> None
set_framerate(framerate: int) -> None
set_display(display: bool) -> None
set_color(color: tuple[int, int, int]) -> None
set_border_radius(radius: int) -> None
set_animate(state: bool) -> None
```

- `set_position`: Set the position of the element
- `set_framerate`: Set the framerate for the elements animations
- `set_display`: If set True, the element is drawn when element.draw is called
- `set_color`: Set the color of the element
- `set_border_radius`: Set the border radius of the element
- `set_animate`: If set True, the elements set animations are will be performed when the element is updated

### Getters

```python
get_position() -> tuple[int, int]
get_display() -> bool
get_animation_state() -> bool
```

- `get_position`: Get the current position of the element, if the element is centered, the returned position is the center of the element
- `get_display`: Get the display state of the element
- `get_animation_state`: Get the animation state of the element, if the element is being animated, the returned value is True, otherwise False

### Toggles

```python
toggle_display() -> None
```

- `toggle_display`: Toggle the display state of the element

### Animations

```python
flow(
    start_position: tuple[int, int],
    end_position: tuple[int, int],
    time: int,
    loop: bool = False
    ) -> None

jump(
    start_position: tuple[int, int],
    end_position: tuple[int, int],
    time: int,
    loop: bool = False,
    ratio: float = 1
    ) -> None
```

- `flow`: Moves the element from start_position to end_position over a specified time. If loop is True, the animation will repeat.
- `jump`: Teleports the element from start_position to end_position over a specified time. If loop is True, the animation will repeat. The ratio parameter controls how much time is spent at each position.

### Mouse and Click Events

```python
is_hovered() -> bool
is_clicked(button: int = 1) -> bool
was_clicked() -> bool
```

- `is_hovered`: Check if the mouse is hovering over the element. Returns True if hovered, False otherwise.
- `is_clicked`: Check if the element is hovered and the provided mouse button is down. Returns True if clicked, False otherwise. The default button is 1 (left mouse button).
- `was_clicked`: Check if the element was clicked and then released. Returns True if this happened, False otherwise.

## Example

A simple example demonstrating basic element creation and animation.

```python
import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create a basic element with animation
box = pygameui.Element(
    position=(100, 300),
    width=50,
    height=50,
    color=(255, 120, 80),  # Coral-like color
    border_radius=10
)

# Create an animated element
animated_box = pygameui.Element(
    position=(700, 300),
    width=50,
    height=50,
    color=(80, 200, 255),  # Light blue
    border_radius=10
)
# Set up a back-and-forth animation
animated_box.flow(
    start_position=(700, 300),
    end_position=(600, 300),
    time=1000,  # 1 second
    loop=True
)
animated_box.set_animate(True)

print("Click on the coral box to change its color")

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # When the static box is clicked, change its color
    if box.was_clicked():
        # Change to a random color
        r = pygame.time.get_ticks() % 255
        g = (pygame.time.get_ticks() // 2) % 255
        b = (pygame.time.get_ticks() // 4) % 255
        box.set_color((r, g, b))

    # Reset screen
    screen.fill((30, 30, 30))

    # Update elements
    box.update()
    animated_box.update()

    # Draw elements
    box.draw(screen)
    animated_box.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
