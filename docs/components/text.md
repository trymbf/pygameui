# Text Element

The Text class provides text rendering capabilities with customizable fonts and styles.

## Basic Usage

```python
text = pygameui.Text(
    position=(100, 100),
    content="Hello World",
    color=(255, 255, 255),
    font_size=20,
    font_family="Arial",
    centered=True
)
```

## Properties
```python
position: tuple[int, int],
content: str,
color: tuple[int, int, int] = (255, 255, 255),
font_size: int = 20,
font_family: str = "Arial",
width: int = 0,
height: int = 0,
anti_aliasing: bool = True,
centered: bool = False
```
- `position`: Tuple of (x, y) coordinates
- `content`: The text string to display
- `color`: RGB tuple for text color
- `font_size`: Size of the text
- `font_family`: Font family to use
- `width`: Width of the text box (0 for auto)
- `height`: Height of the text box (0 for auto)
- `anti_aliasing`: If True, the text is anti-aliased meaning smoother edges
- `centered`: If True, the text is centered on the provided position

## Methods
All methods inherited from the [Element](element.md) class.

(Some methods may not be applicable to the Image class, but are included for consistency.)

### Setters
```python
set_content(content: str) -> None
set_color(color: tuple[int, int, int]) -> None
set_font_size(font_size: int) -> None
set_font_family(font_family: str) -> None
```

- `set_content`: Set the text content
- `set_color`: Set the text color
- `set_font_size`: Set the font size
- `set_font_family`: Set the font family

### Getters
```python
get_content() -> str
```

- `get_content`: Get the current text content

## Font Support

Supported font families:
- System fonts
- Custom TTF fonts
- Default pygame fonts