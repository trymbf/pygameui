# Button

Buttons provide clickable interface elements with hover effects.

## Basic Usage

```python
button = pygameui.Button(
    position=(100, 100),
    content="Click Me",
    width=200,
    height=50,
    color=(255, 255, 255),
    hover_color=(200, 200, 200),
    click_color=(150, 150, 150),
    text_color=(0, 0, 0),
    centered=True
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
