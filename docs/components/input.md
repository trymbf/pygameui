# Input Field

Text input fields for user data entry.

## Basic Usage
```python
input_field = pygameui.Input(
    position=(100, 100),
    width=200,
    height=50,
    hint="Enter text...",
    font_size=20
)
```

## Properties
```python
position: tuple [int, int],
width: int = 200,
height: int = 50,
passive_text_color: tuple[int, int, int] = (150, 150, 150),
active_text_color: tuple[int, int, int] = (255, 255, 255),
passive_border_color: tuple[int, int, int] = (100, 100, 100),
active_border_color: tuple[int, int, int] = (200, 200, 200),
border_radius: int = 0,
border_width: int = 2,
font_size: int = 20,
font_family: str = "Arial",
hint: str = "",
centered: bool = False
```

- `position`: Tuple of (x, y) coordinates
- `width`: Width of the input field
- `height`: Height of the input field
- `passive_text_color`: Color of the text when not focused
- `active_text_color`: Color of the text when focused
- `passive_border_color`: Color of the border when not focused
- `active_border_color`: Color of the border when focused
- `border_radius`: Radius for rounded corners
- `border_width`: Width of the border
- `font_size`: Size of the text font
- `font_family`: Font family for the text
- `hint`: Placeholder text when the field is empty
- `centered`: If True, the element is centered on the provided position

### Input Features
- Text filtering
- Custom borders
- Active/inactive states
- Cursor navigation
- Text selection

### Input Filtering
```python
# Only allow numbers
input_field.set_filter("0123456789", exclude_mode=False)

# Exclude special characters
input_field.set_filter("@#$%^&*()", exclude_mode=True)
```