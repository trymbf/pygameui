# Element Class

The Element class is the foundation of all UI components in PygameUI.

## Basic Usage

```python
element = pygameui.Element(
    position=(100, 100),
    width=200,
    height=100,
    color=(255, 255, 255),
    border_radius=10,
    centered=False
)
```

## Properties
```python
position: tuple[int, int],
width: int,
height:int,
color: tuple[int, int, int] = (255, 255, 255),
border_radius: int = 0,
centered: bool = False
```

- `position`: Tuple of (x, y) coordinates
- `width`: Width of the element
- `height`: Height of the element
- `color`: RGB tuple for element color
- `border_radius`: Radius for rounded corners
- `centered`: If True, the element is centered on the provided position

## Methods

### Position Control
```python
# Set new position
element.set_position((200, 200))

# Get current position
pos = element.get_position()

# Center the element
element.centered = True
```

### Display Control
```python
# Hide element
element.set_display(False)

# Show element
element.set_display(True)

# Toggle visibility
element.toggle_display()
```

### Mouse Interaction
```python
# Check if mouse is over element
if element.is_hovered():
    print("Mouse over!")

# Check if element is clicked
if element.is_clicked():
    print("Clicked!")
```