# Progress Bar

Progress bars provide visual representation of progress or completion status.

## Basic Usage

```python
# Create a progress bar
progress_bar = pygameui.ProgressBar(
    position=(100, 100),
    width=200,
    height=30,
    progress=50,  # Initial progress value
    max_progress=100,
    color=(150, 255, 150),  # Green progress fill
    background_color=(100, 100, 100),
    centered=True
)

# In the main loop
progress_bar.update(events)  # events parameter for API consistency
progress_bar.draw(screen)

# Change progress values
progress_bar.change_progress(5)  # Increase by 5
# or
progress_bar.set_progress(75)    # Set to specific value
```

## Properties

```python
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
```

- `position`: Tuple of (x, y) coordinates
- `width`: Width of the progress bar
- `height`: Height of the progress bar
- `progress`: Initial progress value
- `max_progress`: Maximum value for the progress bar
- `min_progress`: Minimum value for the progress bar
- `color`: Color of the progress bar fill
- `background_color`: Color of the unfilled portion, set to None for no background
- `border_radius`: Radius for rounded corners
- `border_color`: Color of the border around the progress bar, set to None for no border
- `border_width`: Width of the border
- `centered`: If True, the progress bar is centered on the provided position

## Methods
All methods inherited from the [Element](element.md) class.

### Progress Control
```python
set_progress(progress: int) -> None
set_max_progress(max_progress: int) -> None
set_min_progress(min_progress: int) -> None
change_progress(amount: int) -> None
```

- `set_progress`: Sets the current progress value (clamped between min and max)
- `set_max_progress`: Sets the maximum progress value
- `set_min_progress`: Sets the minimum progress value
- `change_progress`: Increases or decreases the current progress by the specified amount

### Getters
```python
get_progress() -> int
```

- `get_progress`: Returns the current progress value

### Mouse and Click Events
See the [Mouse and Click Events](element.md#mouse-and-click-events) section in the Element documentation.

## Example
Simple example of a styled progress bar that can be controlled with the arrow keys.
```python
import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600)) # Set your own width and height

# Create UI elements
progressbar = pygameui.ProgressBar(
    (400, 300),  # Centered in the screen
    width=400,
    height=30,
    color=(75, 145, 250),  # Blue progress fill
    background_color=(40, 40, 40),  # Dark gray background
    border_color=(150, 150, 150),  # Light gray border
    border_radius=10,  # Rounded corners
    border_width=2,
    centered=True
)

instruction_text = pygameui.Text(
    (400, 200),  # Centered in the screen
    content="Press left/right arrow keys to change progress",
    color=(255, 255, 255),  # White text
    font_size=24,
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

    keys_down = pygame.key.get_pressed()
    # Move progressbar with arrow keys
    if keys_down[pygame.K_RIGHT]:
        progressbar.change_progress(.1)
    if keys_down[pygame.K_LEFT]:
        progressbar.change_progress(-.1)

    # Reset screen
    screen.fill((30, 30, 30))  # Darker background for contrast
    # Update element, moves, checks actions etc
    instruction_text.update()
    progressbar.update()

    # Draw element on screen
    progressbar.draw(screen)
    instruction_text.draw(screen)

    # Update pygame display
    pygame.display.flip()
```
