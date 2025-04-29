# Animation Demo

This example demonstrates how to use PygameUI's built-in animation capabilities as well as implementing custom animations.

## Features Demonstrated

- Flow animation (smooth movement)
- Jump animation (teleporting)
- Custom animation (circular motion)
- Animation controls (play/pause)

## Animation Types

PygameUI provides two built-in animation methods which are demonstrated in this example:

1. **Flow Animation**: Smooth movement between two positions
2. **Jump Animation**: Instant teleportation between positions with configurable timing

Additionally, the example shows how to create custom animations by directly manipulating element positions.

## Code Walkthrough

### Flow Animation

The flow animation smoothly transitions an element between two points:

```python
# Create flow animation elements
flow_box = pygameui.Element(
    position=(200, 170),
    width=50,
    height=50,
    color=(75, 145, 250),
    border_radius=10,
    centered=True
)

# Set up flow animation
flow_box.flow(
    start_position=(200, 170),
    end_position=(600, 170),
    time=2000,  # 2 seconds
    loop=True
)
flow_box.set_animate(True)
```

### Jump Animation

The jump animation teleports an element between positions:

```python
# Create jump animation elements
jump_box = pygameui.Element(
    position=(200, 300),
    width=50,
    height=50,
    color=(250, 100, 100),
    border_radius=10,
    centered=True
)

# Set up jump animation
jump_box.jump(
    start_position=(200, 300),
    end_position=(600, 300),
    time=2000,  # 2 seconds
    loop=True,
    ratio=0.5  # Equal time at each position
)
jump_box.set_animate(True)
```

### Custom Animation

The custom animation uses trigonometric functions to create a circular motion:

```python
# Custom animation variables
angle = 0

# In the main loop:
if animations_active:
    angle += 0.02
    x = 400 + 150 * math.cos(angle)
    y = 450 + 40 * math.sin(angle)
    custom_box.set_position((x, y))
```

### Animation Controls

The example demonstrates toggling animations on and off with keyboard input:

```python
# Handle events
events = pygame.event.get()
for event in events:
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            # Toggle animations
            animations_active = not animations_active
            flow_box.set_animate(animations_active)
            jump_box.set_animate(animations_active)
```

## Animation Parameters

### Flow Animation Parameters

- `start_position`: The initial position (x, y coordinates)
- `end_position`: The destination position (x, y coordinates)
- `time`: Duration of one animation cycle in milliseconds
- `loop`: Whether the animation should repeat after completion

### Jump Animation Parameters

- `start_position`: The first position (x, y coordinates)
- `end_position`: The second position (x, y coordinates)
- `time`: Duration of one animation cycle in milliseconds
- `loop`: Whether the animation should repeat after completion
- `ratio`: Time spent at start_position vs. end_position (0.5 = equal time at both)

### Animation Controls

For both animation types, you must:
1. Set up the animation with `flow()` or `jump()`
2. Enable animation with `set_animate(True)`
3. Call `update()` each frame to apply animation changes

## Full Example Code

See the complete [animation_demo.py](https://github.com/trymbf/pygameui/blob/main/examples/animation_demo.py) file in the examples directory.

```python
# See full implementation in examples/animation_demo.py
```