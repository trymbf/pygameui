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

## Methods
All methods inherited from the [Element](element.md) class.

(Some methods may not be applicable to the Image class, but are included for consistency.)

### Basic methods
```python
draw(surface: pygame.Surface) -> None
update(events: list) -> None
```

- `draw`: Draws the input field on the provided surface.
- `update`: Updates the input field and processes events. The `events` parameter should be the list of events from `pygame.event.get()`, se [Basic structure](../getting-started.md#Basic-Structure). This method should be called every frame to ensure animations and events are processed.

### Setters
```python
set_max_length(length: int) -> None
set_filter(filter: str, only_allow_filter: bool = False) -> None
set_hint(hint: str) -> None
set_value(value: str) -> None
```

- `set_max_length`: Set the maximum length of the input field.
- `set_filter`: Set a filter for the input field. The `filter` parameter can be a string of characters. If `only_allow_filter` is set to False, only characters in the filter will be allowed. If set to True, all characters except those in the filter will be allowed.
- `set_hint`: Set the hint text for the input field.
- `set_value`: Set the current value of the input field.

### Getters
```python
get_value() -> str
```

- `get_value`: Get the current value of the input field.