# Components Guide

**Next:** [Animation Guide](../animation.md) | **Previous:** [Basic Tutorial](../tutorials/basic.md)

## Available Components

1. [Element](element.md) - Base component
   - Foundation for all UI elements
   - Positioning and display control
   - Mouse interaction handling

2. [Text](text.md) - Text display
   - Custom fonts and sizes
   - Color control
   - Dynamic content updates

3. [Button](button.md) - Interactive buttons
   - Click handling
   - Hover effects
   - Custom styling

4. [Input](input.md) - Text input fields
   - Text filtering
   - Cursor control
   - Custom borders

5. [Image](image.md) - Image display
   - Multiple formats
   - Scaling options
   - Performance optimization

## Usage Examples

Each component page includes:
- Basic implementation
- Available properties
- Common use cases
- Performance tips

## Quick Reference

```python
# Basic element creation pattern
element = pygameui.ComponentName(
    position=(x, y),
    # ... other properties
)

# Update and draw pattern
element.update()  # or element.update(events)
element.draw(screen)
```

**Next:** Learn about [Animation](../animation.md)
