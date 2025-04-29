# Input

The Input component provides a text input field for user interaction.

## Basic Usage

```python
# Create the input field
input_field = pygameui.Input(
    position=(100, 100),
    width=300,
    height=40,
    hint="Enter your name..."
)

# In the main loop
events = pygame.event.get()
# Important: Input component requires events to handle typing
input_field.update(events)  
input_field.draw(screen)

# Getting the current value
text_value = input_field.get_value()
```

**Important**: The Input component requires event handling to work properly. Always pass the events list to the update method.

## Properties

```python
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
```

- `position`: Tuple of (x, y) coordinates
- `width`: Width of the input field
- `height`: Height of the input field
- `passive_text_color`: Color of the text when the input is not active
- `active_text_color`: Color of the text when the input is active
- `passive_border_color`: Color of the border when the input is not active
- `active_border_color`: Color of the border when the input is active
- `border_radius`: Radius for rounded corners
- `border_width`: Width of the border
- `font_size`: Size of the font
- `font_family`: Font family for the text
- `hint`: Text to display when the input is empty
- `centered`: If True, the input is centered on the provided position

## Methods

All methods inherited from the [Text](text.md) class.

### Setters

```python
set_max_length(max_length: int) -> None
set_filter(filter: str, only_allow_filter: bool = False) -> None
set_hint(hint: str) -> None
set_value(value: str) -> None
```

- `set_max_length`: Set the maximum length of the input text
- `set_filter`: Set a filter for allowed characters. If only_allow_filter is True, only characters in filter are allowed; otherwise, characters in filter are excluded
- `set_hint`: Set the hint text displayed when the input is empty
- `set_value`: Set the current text value

### Getters

```python
get_value() -> str
```

- `get_value`: Get the current text value entered by the user

## Example

A simple form with input fields.

```python
import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create input fields
name_input = pygameui.Input(
    position=(400, 150),
    width=300,
    height=40,
    hint="Enter your name",
    passive_text_color=(180, 180, 180),
    active_text_color=(255, 255, 255),
    passive_border_color=(80, 80, 80),
    active_border_color=(120, 120, 255),
    border_radius=5,
    centered=True
)

# Create a numbers-only input field
age_input = pygameui.Input(
    position=(400, 220),
    width=300,
    height=40,
    hint="Enter your age (numbers only)",
    passive_text_color=(180, 180, 180),
    active_text_color=(255, 255, 255),
    passive_border_color=(80, 80, 80),
    active_border_color=(120, 120, 255),
    border_radius=5,
    centered=True
)
# Set a filter to only allow numbers
age_input.set_filter("0123456789", only_allow_filter=True)
age_input.set_max_length(3)

# Create labels
name_label = pygameui.Text(
    position=(200, 150),
    content="Name:",
    color=(255, 255, 255),
    font_size=20,
    centered=True
)

age_label = pygameui.Text(
    position=(200, 220),
    content="Age:",
    color=(255, 255, 255),
    font_size=20,
    centered=True
)

# Create a submit button
submit_button = pygameui.Button(
    position=(400, 300),
    width=120,
    height=40,
    label="Submit",
    color=(100, 180, 100),
    hover_color=(120, 200, 120),
    text_color=(255, 255, 255),
    border_radius=5,
    centered=True
)

# Result text
result_text = pygameui.Text(
    position=(400, 400),
    content="",
    color=(255, 255, 255),
    font_size=20,
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

    # Update elements
    name_input.update(events)
    age_input.update(events)
    name_label.update()
    age_label.update()
    submit_button.update()
    result_text.update()

    # Check for submit button click
    if submit_button.was_clicked():
        name = name_input.get_value()
        age = age_input.get_value()

        if name and age:
            result_text.set_content(f"Hello {name}, you are {age} years old!")
        else:
            result_text.set_content("Please fill in all fields")

    # Draw elements
    name_input.draw(screen)
    age_input.draw(screen)
    name_label.draw(screen)
    age_label.draw(screen)
    submit_button.draw(screen)
    result_text.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)

```
