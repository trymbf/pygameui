# Text

The Text component displays text on the screen with customizable appearance.

## Basic Usage

```python
# Create a text element
text = pygameui.Text(
    position=(100, 100),
    content="Hello, World!",
    color=(255, 255, 255),  # White text
    font_size=24
)

# In the main loop
text.update(events)  # events parameter is included for API consistency
text.draw(screen)
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
- `content`: The text to display
- `color`: RGB tuple for text color (r, g, b)
- `font_size`: Size of the font in pixels
- `font_family`: Font family to use (should be available on the system)
- `width`: Width of the text element in pixels, 0 indicates auto-width based on content
- `height`: Height of the text element in pixels, 0 indicates auto-height based on content
- `anti_aliasing`: Whether to use anti-aliasing for smoother text rendering
- `centered`: If True, the text is centered on the provided position; otherwise, the top-left corner is at the position

## Methods

All methods inherited from the [Element](element.md) class.

### Update Method

```python
update(events=None) -> None
```

- `update`: Updates the text element's state including animations. The `events` parameter is included for API consistency with other components but is not used by the Text class.

### Setters

```python
set_content(content: str) -> None
set_color(color: tuple[int, int, int]) -> None
set_font_size(font_size: int) -> None
set_font_family(font_family: str) -> None
```

- `set_content`: Change the displayed text. Non-string content will be converted to string automatically.
- `set_color`: Change the color of the text as RGB tuple (r, g, b)
- `set_font_size`: Change the size of the font in pixels
- `set_font_family`: Change the font family (must be available on the system)

### Getters

```python
get_content() -> str
```

- `get_content`: Get the current text content
