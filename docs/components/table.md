# Table

Tables allow for displaying data in a grid format with rows and columns.

## Basic Usage

```python
table = pygameui.Table(
    position=(100, 100),
    content=[
        ["Header 1", "Header 2", "Header 3"],
        ["Row 1 Col 1", "Row 1 Col 2", "Row 1 Col 3"],
        ["Row 2 Col 1", "Row 2 Col 2", "Row 2 Col 3"]
    ],
)
```

## Properties

```python
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
```

- `position`: Tuple of (x, y) coordinates
- `content`: 2D list of strings representing the table data
- `width`: Width of the entire table
- `height`: Height of the entire table
- `color`: Background color of the cells
- `hover_color`: Background color of the cells when hovered
- `text_color`: Color of the text in cells
- `border_color`: Color of the cell borders
- `border_width`: Width of the cell borders
- `border_radius`: Radius for rounded corners of cells
- `centered`: If True, the table is centered on the provided position

## Methods

All methods inherited from the [Element](element.md) class.

### Setters

```python
set_content(content: list[list[str]]) -> None
```

- `set_content`: Updates the table with new content

## Example

A simple example demonstrating a table with different types of data.

```python
import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create table data
table_data = [
    ["Name", "Age", "Role"],
    ["John", "32", "Developer"],
    ["Sarah", "28", "Designer"],
    ["Mike", "45", "Manager"]
]

# Create a table
data_table = pygameui.Table(
    position=(400, 300),
    content=table_data,
    width=400,
    height=200,
    color=(240, 240, 240),
    hover_color=(220, 220, 220),
    text_color=(30, 30, 30),
    border_color=(180, 180, 180),
    border_width=1,
    border_radius=2,
    centered=True
)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Reset screen
    screen.fill((30, 30, 30))  # Dark background

    # Update table
    data_table.update()

    # Draw table
    data_table.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
