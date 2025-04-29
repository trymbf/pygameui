# DropdownMenu

The `DropdownMenu` provides a dropdown interface for selecting one option from a list of choices. It supports customizable colors, text styles, and the ability to wrap options into multiple columns.

## Basic Usage

```python
# Create a dropdown menu
dropdown = pygameui.DropdownMenu(
    position=(100, 100),
    options=["Option 1", "Option 2", "Option 3"],
    width=200,
    height=50
)

# In the main loop
events = pygame.event.get()
dropdown.update(events)  # Pass events for proper interaction
dropdown.draw(screen)

# Get the selected option
selected_option = dropdown.get_selected_option()
```

## Properties

```python
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
```

- `position`: Tuple of (x, y) coordinates
- `width`: Width of the dropdown menu main button
- `height`: Height of the dropdown menu main button
- `options`: List of strings representing the dropdown options
- `on_change`: Function called when the selected option changes
- `element_width`: Width of each option button in the dropdown
- `element_height`: Height of each option button in the dropdown
- `element_spacing`: Spacing between option buttons
- `max_elements_per_column`: Maximum number of options per column before wrapping
- `wrap_reverse`: If True, wraps options in reverse order
- `color`: Default background color of the option buttons
- `hover_color`: Background color when an option is hovered over
- `click_color`: Background color when an option is clicked
- `font_size`: Size of the text font
- `font_family`: Font family used for text
- `text_color`: Default text color
- `text_hover_color`: Text color when hovered over
- `text_click_color`: Text color when clicked
- `selected_option_color`: Background color of the main button
- `selected_option_hover_color`: Background color of the main button when hovered
- `selected_option_click_color`: Background color of the main button when clicked
- `selected_option_text_color`: Text color of the main button
- `selected_option_text_hover_color`: Text color of the main button when hovered
- `selected_option_text_click_color`: Text color of the main button when clicked
- `border_radius`: Radius for rounded corners
- `centered`: If True, the dropdown is centered on the provided position

## Methods

All methods inherited from the [Element](element.md) class.

### Setters

```python
set_options(options: list[str]) -> None
set_selected_option(option: str) -> None
set_selected_index(index: int) -> None
```

- `set_options`: Set the list of options for the dropdown
- `set_selected_option`: Set the currently selected option by value
- `set_selected_index`: Set the currently selected option by index

### Getters

```python
get_selected_option() -> str
get_selected_index() -> int
get_options() -> list[str]
```

- `get_selected_option`: Get the currently selected option
- `get_selected_index`: Get the index of the currently selected option
- `get_options`: Get the list of options

### Mouse and Click Events

See the [Mouse and Click Events](element.md#mouse-and-click-events) section in the Element documentation.

## Example

Simple example of a dropdown menu with selectable options.

```python
import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create dropdown menu
dropdown = pygameui.DropdownMenu(
    position=(400, 200),
    options=["Option 1", "Option 2", "Option 3"],
    width=250,
    height=50,
    color=(240, 240, 240),
    hover_color=(220, 220, 220),
    text_color=(50, 50, 50),
    centered=True
)

# Main loop
running = True
while running:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Reset screen
    screen.fill((30, 30, 30))  # Dark background

    # Update dropdown
    dropdown.update(events)

    # Check for selection
    if dropdown.get_selected_option():
        print(f"Selected: {dropdown.get_selected_option()}")

    # Draw elements
    dropdown.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
