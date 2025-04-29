# Table

Tables allow for displaying data in a grid format with rows and columns.

## Basic Usage

```python
# Create a table with data
table = pygameui.Table(
    position=(100, 100),
    content=[
        ["Header 1", "Header 2", "Header 3"],
        ["Row 1 Col 1", "Row 1 Col 2", "Row 1 Col 3"],
        ["Row 2 Col 1", "Row 2 Col 2", "Row 2 Col 3"]
    ],
    width=400,
    height=200
)

# In the main loop
table.update(events)  # events parameter for API consistency
table.draw(screen)
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
- `position`: Tuple of (x, y) coordinates where the table will be positioned
- `content`: 2D list of strings representing the table data (rows and columns)
- `width`: Width of the entire table in pixels
- `height`: Height of the entire table in pixels
- `color`: Background color of the cells as RGB tuple (r, g, b)
- `hover_color`: Background color of the cells when hovered as RGB tuple
- `text_color`: Color of the text in cells as RGB tuple
- `border_color`: Color of the cell borders as RGB tuple
- `border_width`: Width of the cell borders in pixels
- `border_radius`: Radius for rounded corners of cells in pixels
- `centered`: If True, the table is centered on the provided position; otherwise, the top-left corner is at the position

## Methods

All methods inherited from the [Element](element.md) class.

### Update Method

```python
update(events=None) -> None
```

- `update`: Updates the table and its elements. The `events` parameter is included for API consistency with other components but is not used directly by the Table class itself.

### Setters

```python
set_content(content: list[list[str]]) -> None
```

- `set_content`: Updates the table with new content. The content should be a 2D list of strings where each inner list represents a row of data.

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
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Reset screen
    screen.fill((30, 30, 30))  # Dark background

    # Update table with events for API consistency
    data_table.update(events)

    # Draw table
    data_table.draw(screen)

    # Display instructions
    title = pygameui.Text(
        position=(400, 100),
        content="Data Table Example",
        color=(255, 255, 255),
        font_size=30,
        centered=True
    )
    title.update()
    title.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
```
