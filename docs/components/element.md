# Element Class

The Element class is the foundation of all UI components in PygameUI.

## Basic Usage

```python
element = pygameui.Element(
    position=(100, 100),
    width=200,
    height=100,
    color=(255, 255, 255),
    border_radius=10,
    centered=False
)
```

## Properties
```python
position: tuple[int, int],
width: int,
height:int,
color: tuple[int, int, int] = (255, 255, 255),
border_radius: int = 0,
centered: bool = False
```

- `position`: Tuple of (x, y) coordinates
- `width`: Width of the element
- `height`: Height of the element
- `color`: RGB tuple for element color
- `border_radius`: Radius for rounded corners
- `centered`: If True, the element is centered on the provided position

## Methods

### Basic methods
```python
draw(surface: pygame.Surface) -> None
update() -> None
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
- `set_animate`: If set True, the elements set animations are will be preformed when the element is updated

### Getters
```python
get_position() -> tuple[int, int]
get_display() -> bool
get_animation_state() -> bool
```

- `get_position`: Get the current position of the element, if the element is centered, the returned position is the center of the element
- `get_display`: Get the display state of the element
- `get_animation_state`: Get the animation state of the element, if the element is being animated, the returned value is True, otherwise False


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

- `jump`: Teleports the element from start_position to end_position over a specified time. If loop is True, the animation will repeat.

### Mouse and Click Events
```python
is_hovered() -> bool
is_clicked(button: int = 1) -> bool
was_clicked() -> bool
```

- `is_hovered`: Check if the mouse is hovering over the element. Returns True if hovered, False otherwise.
- `is_clicked`: Check if the element is hovered and the provided mouse button is down. Returns True if clicked, False otherwise. The default button is 1 (left mouse button).
- `was_clicked`: Check if the element was clicked in the last frame. Returns True if clicked, False otherwise.