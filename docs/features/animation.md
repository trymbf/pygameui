# Animation Guide

PygameUI provides built-in animation capabilities for UI elements.

## Flow Animation

The `flow()` method creates smooth movement between positions:

```python
element.flow(
    start_position=(0, 0),
    end_position=(100, 100),
    time=1000,  # milliseconds
    loop=False
)
```

### Parameters
- `start_position`: Starting coordinates (x, y)
- `end_position`: Ending coordinates (x, y)
- `time`: Duration in milliseconds
- `loop`: Whether to loop the animation

## Jump Animation

The `jump()` method creates instant position changes:

```python
element.jump(
    start_position=(0, 0),
    end_position=(100, 0),
    time=1000,
    loop=True,
    ratio=0.5
)
```

### Parameters
- `start_position`: Starting coordinates (x, y)
- `end_position`: Ending coordinates (x, y)
- `time`: Duration in milliseconds
- `loop`: Whether to loop the animation
- `ratio`: Time distribution between positions (0-1)

## Animation Control

Control methods available for all animations:
- `start_move()`: Begin animation
- `stop_move()`: Stop animation
- `set_framerate(fps)`: Set animation speed
