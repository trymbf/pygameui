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
centered: bool = False
```
- `position`: Tuple of (x, y) coordinates
- `content`: The text string to display
- `color`: RGB tuple for text color
- `font_size`: Size of the text
- `font_family`: Font family to use
- `width`: Width of the text box (0 for auto)
- `height`: Height of the text box (0 for auto)
- `centered`: If True, the text is centered on the provided position

## Methods

### Text Manipulation
```python
# Change text content
text.change_text("New text")

# Change text color
text.change_text_color((255, 0, 0))
```

## Font Support

Supported font families:
- System fonts
- Custom TTF fonts
- Default pygame fonts