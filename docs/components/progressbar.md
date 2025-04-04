# ProgressBar

The ProgressBar component displays a visual representation of progress or completion.

## Basic Usage

```python
progress_bar = pygameui.ProgressBar(
    position=(100, 100),
    width=300,
    height=30
)
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
- `max_progress`: Maximum progress value
- `min_progress`: Minimum progress value
- `color`: Color of the progress indicator
- `background_color`: Color of the background
- `border_radius`: Radius for rounded corners
- `border_color`: Color of the border
- `border_width`: Width of the border
- `centered`: If True, the progress bar is centered on the provided position

## Methods

All methods inherited from the [Element](element.md) class.

### Setters

```python
set_progress(progress: int) -> None
set_max_progress(max_progress: int) -> None
set_min_progress(min_progress: int) -> None
change_progress(amount: int) -> None
```

- `set_progress`: Set the current progress value
- `set_max_progress`: Set the maximum progress value
- `set_min_progress`: Set the minimum progress value
- `change_progress`: Change the progress value by the specified amount

### Getters

```python
get_progress() -> int
```

- `get_progress`: Get the current progress value

## Example

A simple example demonstrating a loading bar with automatic progress.

```python
import pygame
import pygameui
import time

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create a progress bar
loading_bar = pygameui.ProgressBar(
    position=(400, 250),
    width=400,
    height=30,
    progress=0,
    color=(100, 200, 100),  # Green progress
    background_color=(50, 50, 50),
    border_color=(150, 150, 150),
    border_width=2,
    border_radius=5,
    centered=True
)

# Create a label
progress_label = pygameui.Text(
    position=(400, 220),
    content="Loading...",
    color=(255, 255, 255),
    font_size=24,
    centered=True
)

percentage_label = pygameui.Text(
    position=(400, 300),
    content="0%",
    color=(255, 255, 255),
    font_size=18,
    centered=True
)

# Main loop
running = True
start_time = time.time()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate progress based on time
    elapsed = time.time() - start_time
    progress = int(min(100, elapsed * 10))  # Complete in 10 seconds
    
    # Update progress bar and labels
    loading_bar.set_progress(progress)
    percentage_label.set_content(f"{progress}%")
    
    if progress >= 100:
        progress_label.set_content("Loading Complete!")

    # Reset screen
    screen.fill((30, 30, 30))  # Dark background

    # Update components
    loading_bar.update()
    progress_label.update()
    percentage_label.update()

    # Draw components
    loading_bar.draw(screen)
    progress_label.draw(screen)
    percentage_label.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
