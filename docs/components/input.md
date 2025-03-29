# Input Field

Text input fields for user data entry.

## Basic Usage

```python
input_field = pygameui.Input(
    position=(100, 100),
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

## Example

Simple form with two input fields and validation.

```python
import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create input fields
username_input = pygameui.Input(
    position=(400, 200),
    width=300,
    height=40,
    hint="Username",
    font_size=18,
    centered=True,
    border_radius=5,
    active_border_color=(75, 145, 250)  # Blue highlight when active
)

password_input = pygameui.Input(
    position=(400, 280),
    width=300,
    height=40,
    hint="Password",
    font_size=18,
    centered=True,
    border_radius=5,
    active_border_color=(75, 145, 250)  # Blue highlight when active
)

# Set a maximum length for the username
username_input.set_max_length(20)

# Create a submit button
submit_button = pygameui.Button(
    position=(400, 360),
    width=150,
    height=50,
    label="Submit",
    color=(75, 145, 250),  # Blue
    hover_color=(95, 165, 255),
    text_color=(255, 255, 255),
    border_radius=5,
    centered=True
)

# Title
title = pygameui.Text(
    position=(400, 100),
    content="Login Form",
    color=(255, 255, 255),
    font_size=32,
    centered=True
)

# Status message
status = pygameui.Text(
    position=(400, 440),
    content="Enter your login details",
    color=(200, 200, 200),
    font_size=16,
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
    screen.fill((30, 30, 30))

    # Update UI elements
    username_input.update(events)
    password_input.update(events)
    submit_button.update()
    title.update()
    status.update()

    # Check for submit button click
    if submit_button.was_clicked():
        username = username_input.get_value()
        password = password_input.get_value()

        if not username or not password:
            status.set_content("Please fill in all fields")
            status.set_color((255, 100, 100))  # Red for error
        else:
            status.set_content(f"Logged in as: {username}")
            status.set_color((100, 255, 100))  # Green for success

    # Draw UI elements
    username_input.draw(screen)
    password_input.draw(screen)
    submit_button.draw(screen)
    title.draw(screen)
    status.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
