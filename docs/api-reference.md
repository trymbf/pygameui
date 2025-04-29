# API Reference

This page provides a comprehensive reference for all classes and methods in the PygameUI library.

## Element

The base class for all UI components.

### Constructor

```python
Element(
    position: tuple[int, int],
    width: int,
    height: int,
    color: tuple[int, int, int] = (255, 255, 255),
    border_radius: int = 0,
    border_color: tuple[int, int, int] = None,
    border_width: int = 2,
    centered: bool = False
)
```

### Methods

| Method | Description |
|--------|-------------|
| `draw(surface: pygame.Surface) -> None` | Draws the element on the provided surface |
| `update(events=None) -> None` | Updates the element's state including animations |
| `move(x: int, y: int) -> None` | Moves the element by the specified amounts in x and y directions |
| `set_position(position: tuple[int,int]) -> None` | Sets the position of the element |
| `set_framerate(framerate: int) -> None` | Sets the framerate for animations |
| `set_display(display: bool) -> None` | Sets display status (visible/hidden) |
| `set_color(color: tuple[int, int, int]) -> None` | Sets the element's color |
| `set_border_radius(radius: int) -> None` | Sets the border radius |
| `set_animate(state: bool) -> None` | Enables/disables animation |
| `get_position() -> tuple[int, int]` | Gets the current position |
| `get_display() -> bool` | Gets display status |
| `get_animation_state() -> bool` | Gets animation status |
| `toggle_display() -> None` | Toggles display status |
| `flow(start_position, end_position, time, loop=False) -> None` | Sets up smooth animation |
| `jump(start_position, end_position, time, loop=False, ratio=1) -> None` | Sets up teleporting animation |
| `is_hovered() -> bool` | Checks if mouse is hovering over the element |
| `is_clicked(button: int = 0) -> bool` | Checks if element is being clicked |
| `was_clicked(button: int = 0) -> bool` | Checks if element was clicked and released |

## Text

Text display component.

### Constructor

```python
Text(
    position: tuple[int, int],
    content: str,
    color: tuple[int, int, int] = (255, 255, 255),
    font_size: int = 20,
    font_family: str = "Arial",
    width: int = 0,
    height: int = 0,
    anti_aliasing: bool = True,
    centered: bool = False
)
```

### Methods

Inherits all methods from Element, plus:

| Method | Description |
|--------|-------------|
| `set_content(content: str) -> None` | Sets the displayed text |
| `set_color(color: tuple[int, int, int]) -> None` | Sets the text color |
| `set_font_size(font_size: int) -> None` | Sets the font size |
| `set_font_family(font_family: str) -> None` | Sets the font family |
| `get_content() -> str` | Gets the current text |

## Button

Interactive button component.

### Constructor

```python
Button(
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
)
```

### Methods

Inherits all methods from Element, plus:

| Method | Description |
|--------|-------------|
| `set_label(label: str) -> None` | Sets the button text |
| `set_color(color: tuple[int, int, int]) -> None` | Sets the default color |
| `set_hover_color(color: tuple[int, int, int]) -> None` | Sets the hover color |
| `set_click_color(color: tuple[int, int, int]) -> None` | Sets the click color |
| `set_text_color(color: tuple[int, int, int]) -> None` | Sets the text color |
| `set_text_hover_color(color: tuple[int, int, int]) -> None` | Sets the text hover color |
| `set_text_click_color(color: tuple[int, int, int]) -> None` | Sets the text click color |

## Image

Image display component.

### Constructor

```python
Image(
    position: tuple[int, int],
    src: str,
    width: int = 0,
    height: int = 0,
    scale: int = 1,
    centered: bool = False
)
```

### Methods

Inherits all methods from Element, plus:

| Method | Description |
|--------|-------------|
| `set_image(src: str) -> None` | Changes the image source |
| `scale(scale: int) -> None` | Changes the image scale |
| `get_image() -> pygame.Surface` | Gets the image surface |
| `get_scale() -> int` | Gets the current scale |

## Input

Text input field component.

### Constructor

```python
Input(
    position: tuple[int, int],
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
)
```

### Methods

Inherits all methods from Text, plus:

| Method | Description |
|--------|-------------|
| `set_max_length(max_length: int) -> None` | Sets maximum text length |
| `set_filter(filter: str, only_allow_filter: bool = False) -> None` | Sets character filter |
| `set_hint(hint: str) -> None` | Sets hint text |
| `set_value(value: str) -> None` | Sets the current text value |
| `get_value() -> str` | Gets the current text value |

## Checkbox

Toggle component with various styles.

### Constructor

```python
Checkbox(
    position: tuple[int, int],
    width: int = 50,
    height: int = 50,
    style: Literal["checkmark", "cross", "circle", "square", "none"] = "checkmark",
    unchecked_style: Literal["checkmark", "cross", "circle", "square", "none"] = "none",
    mark_width: int = 5,
    color: tuple[int, int, int] = (100, 255, 100),
    background_color: tuple[int, int, int] = (200, 200, 200),
    border_radius: int = 0,
    border_color: tuple[int, int, int] = (0, 0, 0),
    border_width: int = 2,
    centered: bool = False
)
```

### Methods

Inherits all methods from Element, plus:

| Method | Description |
|--------|-------------|
| `set_checked(checked: bool) -> None` | Sets the checked state |
| `disable() -> None` | Disables the checkbox |
| `enable() -> None` | Enables the checkbox |
| `is_checked() -> bool` | Gets the current checked state |
| `is_enabled() -> bool` | Gets the enabled state |

## ProgressBar

Progress indicator component.

### Constructor

```python
ProgressBar(
    position: tuple[int, int],
    width: int = 200,
    height: int = 50,
    progress: int = 0,
    max_progress: int = 100,
    min_progress: int = 0,
    color: tuple[int, int, int] = (150, 255, 150),
    background_color: tuple[int, int, int] = (100, 100, 100),
    border_radius: int = 0,
    border_color: tuple[int, int, int] = (200, 200, 200),
    border_width: int = 2,
    centered: bool = False
)
```

### Methods

Inherits all methods from Element, plus:

| Method | Description |
|--------|-------------|
| `set_progress(progress: int) -> None` | Sets the progress value |
| `set_max_progress(max_progress: int) -> None` | Sets the maximum progress |
| `set_min_progress(min_progress: int) -> None` | Sets the minimum progress |
| `change_progress(amount: int) -> None` | Changes progress by amount |
| `get_progress() -> int` | Gets the current progress |

## DropdownMenu

Menu with selectable options.

### Constructor

```python
DropdownMenu(
    position: tuple[int, int],
    width: int = 200,
    height: int = 50,
    options: list[str],
    on_change: callable = None,
    element_width: int = 200,
    element_height: int = 50,  
    element_spacing: int = 2,
    max_elements_per_column: int = 5,
    wrap_reverse: bool = False,
    color: tuple[int, int, int] = (255, 255, 255),
    hover_color: tuple[int, int, int] = (200, 200, 200),
    click_color: tuple[int, int, int] = (150, 150, 150),
    font_size: int = 20,
    font_family: str = "Arial",
    text_color: tuple[int, int, int] = (0, 0, 0),
    text_hover_color: tuple[int, int, int] = (0, 0, 0),
    text_click_color: tuple[int, int, int] = (0, 0, 0),
    selected_option_color: tuple[int, int, int] = (200, 200, 200),
    selected_option_hover_color: tuple[int, int, int] = (150, 150, 150),
    selected_option_click_color: tuple[int, int, int] = (100, 100, 100),
    selected_option_text_color: tuple[int, int, int] = (0, 0, 0),
    selected_option_text_hover_color: tuple[int, int, int] = (0, 0, 0),
    selected_option_text_click_color: tuple[int, int, int] = (0, 0, 0),
    border_radius: int = 0,
    centered: bool = False
)
```

### Methods

Inherits all methods from Element, plus:

| Method | Description |
|--------|-------------|
| `set_options(options: list[str]) -> None` | Sets the dropdown options |
| `set_selected_option(option: str) -> None` | Sets selected option by value |
| `set_selected_index(index: int) -> None` | Sets selected option by index |
| `get_selected_option() -> str` | Gets selected option value |
| `get_selected_index() -> int` | Gets selected option index |
| `get_options() -> list[str]` | Gets all options |

## Table

Grid-based data display component.

### Constructor

```python
Table(
    position: tuple[int, int],
    content: list[list[str]], 
    width: int = 200, 
    height: int = 50, 
    color: tuple[int, int, int] = (255, 255, 255),
    hover_color: tuple[int, int, int] = (200, 200, 200),
    text_color: tuple[int, int, int] = (0, 0, 0),
    border_color: tuple[int, int, int] = (200, 200, 200),
    border_width: int = 2,
    border_radius: int = 0, 
    centered: bool = False
)
```

### Methods

Inherits all methods from Element, plus:

| Method | Description |
|--------|-------------|
| `set_content(content: list[list[str]]) -> None` | Updates table content |