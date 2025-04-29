# Button

Buttons provide clickable interface elements with hover effects.

## Basic Usage

```python
button = pygameui.Button(
    position=(100, 100),
    label="Click me.",
    width=200,
    height=50
)

# In the main loop
button.update(events)  # Pass events list for proper interaction handling
button.draw(screen)

# Check for clicks
if button.was_clicked():
    print("Button was clicked!")
```

## Properties

```python
position: tuple[int, int],
width: int = 200,
height: int = 50,
border_radius: int = 10,
border_color: tuple[int, int, int] = None,
border_width: int = 2,
label: str = "Click me.",
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
- `border_color`: Color of the button border, if None, the border will not be drawn
- `border_width`: Width of the button border
- `label`: Text displayed on the button
- `color`: Default button background color
- `hover_color`: Background color when the button is hovered over
- `click_color`: Background color when the button is clicked
- `text_color`: Color of the text when not hovered
- `text_hover_color`: Color of the text when hovered over
- `text_click_color`: Color of the text when clicked
- `font_size`: Size of the text font
- `font_family`: Font family for the text
- `centered`: If True, the button is centered on the provided position

## Methods

All methods inherited from the [Element](element.md) class.

### Update Method

```python
update(events=None) -> None
```

- `update`: Updates the button state based on mouse interaction and animations.
  The `events` parameter should be a list of pygame events, though it's not used directly by the Button class.
  Calling this method is essential for proper button interaction and animation handling.

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
- `set_text_color`: Set the color of the button label when not hovered
- `set_text_hover_color`: Set the color of the button label when hovered over
- `set_text_click_color`: Set the color of the button label when clicked

### Mouse Interaction Methods

```python
is_hovered() -> bool
is_clicked(button: int = 0) -> bool
was_clicked(button: int = 0) -> bool
```

- `is_hovered`: Check if the mouse is currently hovering over the button
- `is_clicked`: Check if the button is currently being pressed (mouse button held down)
- `was_clicked`: Check if the button was clicked (mouse pressed and released on the button)
  For all mouse methods, the `button` parameter specifies which mouse button to check (0=left, 1=middle, 2=right)
