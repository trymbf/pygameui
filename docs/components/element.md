# Element

The Element class is the foundation of all UI components in PygameUI. It can alse be used as a standalone component for your square or rectangular UI element needs. Backgrounds, panels etc.

## Basic Usage

```python
# Create a basic element
element = pygameui.Element(
    position=(100, 100),
    width=200,
    height=100,
    color=(255, 255, 255)  # White color
)

# In the main loop
# The events parameter is for API consistency, though not used directly by Element
element.update(events)
element.draw(screen)
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
- `width`: Width of the element in pixels
- `height`: Height of the element in pixels
- `color`: RGB tuple for element color (r, g, b)
- `border_radius`: Radius for rounded corners in pixels
- `border_color`: Color of the element border as RGB tuple, if None, the border will not be drawn
- `border_width`: Width of the element border in pixels
- `centered`: If True, the element is centered on the provided position; otherwise, the top-left corner is at the position

## Methods

### Basic methods

```python
draw(surface: pygame.Surface) -> None
update(events=None) -> None
```

- `draw`: Draws the element on the provided surface.
- `update`: Updates the element's state including animations. The `events` parameter is optional and not used by the base Element class, but is included for API consistency with derived classes.

### Movement

```python
move(x: int, y: int) -> None
```

- `move`: Moves the element by the specified amounts in x and y directions relative to its current position. Note that this has no effect when the element is being animated.

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
- `set_framerate`: Set the framerate for the element's animations (affects speed)
- `set_display`: If set to True, the element is drawn when element.draw is called
- `set_color`: Set the color of the element as RGB tuple
- `set_border_radius`: Set the border radius of the element in pixels
- `set_animate`: If set to True, animations set on the element will be performed when update is called

### Getters

```python
get_position() -> tuple[int, int]
get_display() -> bool
get_animation_state() -> bool
```

- `get_position`: Get the current position of the element, if the element is centered, the returned position is the center of the element
- `get_display`: Get the display state of the element (True if visible)
- `get_animation_state`: Get the animation state of the element, returns True if the element is being animated, otherwise False

### Toggles

```python
toggle_display() -> None
```

- `toggle_display`: Toggle the display state of the element (hide if visible, show if hidden)

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

- `flow`: Sets up smooth movement animation of the element between two positions.
  - `start_position`: Where the element will start moving from (x, y coordinates)
  - `end_position`: Where the element will move to (x, y coordinates)
  - `time`: Duration of movement in milliseconds
  - `loop`: If True, the element will continuously move back and forth between positions

- `jump`: Sets up teleporting animation of the element between two positions.
  - `start_position`: Where the element will start jumping from (x, y coordinates)
  - `end_position`: Where the element will jump to (x, y coordinates)
  - `time`: Duration between jumps in milliseconds
  - `loop`: If True, the element will continuously jump back and forth between positions
  - `ratio`: Float between 0 and 1 controlling how much time is spent at each position

Note: You must call `set_animate(True)` to start the animation and call `update()` each frame to apply animation changes.

### Mouse and Click Events

```python
is_hovered() -> bool
is_clicked(button: int = 0) -> bool
was_clicked(button: int = 0) -> bool
```

- `is_hovered`: Check if the mouse is hovering over the element. Returns True if hovered, False otherwise.
- `is_clicked`: Check if the element is hovered and the provided mouse button is down. Returns True if clicked, False otherwise.
- `was_clicked`: Check if the element was clicked and then released. Returns True if this happened, False otherwise.

For mouse button parameters:
- `button` = 0: Left mouse button (default)
- `button` = 1: Middle mouse button
- `button` = 2: Right mouse button
