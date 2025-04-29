# Troubleshooting

This guide addresses common issues you might encounter when using PygameUI and provides solutions.

## Component Interaction Issues

### Components Not Responding to Clicks

1. **Z-Order Issues**: Components might be overlapping. Ensure your draw order is correct:

   ```python
   # Draw in the correct order (bottom to top)
   background.draw(screen)
   button1.draw(screen)
   button2.draw(screen)  # This will appear on top
   ```
    
2. **Position Check**: Verify that components are positioned within the visible area of the screen.

### Input Fields Not Accepting Text

**Issue**: Input components don't register keystrokes.

**Solutions**:

1. **Active State**: The input field must be activated by clicking on it first.

2. **Events Handling**: Make sure you'  re passing events to the input component:

   ```python
   events = pygame.event.get()
   my_input.update(events)
   ```

3. **Filter Settings**: Check if you've set a filter that might be blocking the characters:

   ```python
   # Remove any restrictive filters
   my_input.set_filter("", only_allow_filter=False)
   ```

## Rendering Issues

### Components Not Displaying Correctly

**Issue**: Components appear with wrong sizes, colors, or don't display at all.

**Solutions**:

1. **Display Setting**: Check if the component's display property is enabled:

   ```python
   my_component.set_display(True)
   ```

2. **Draw Call**: Ensure you're calling the draw method for each component:

   ```python
   my_component.draw(screen)
   ```

3. **Screen Updates**: Make sure you're updating the screen after drawing:

   ```python
   pygame.display.flip()  # or pygame.display.update()
   ```

4. **Color Format**: Ensure colors are valid RGB tuples with values between 0-255:

   ```python
   # Correct: RGB tuple
   my_component.set_color((255, 100, 100))
   
   # Incorrect: values out of range or wrong format
   # my_component.set_color((300, 100, 100))  # Values > 255
   # my_component.set_color("#FF0000")  # Wrong format
   ```

### Text Rendering Problems

**Issue**: Text appears blurry, wrong size, or doesn't show up.

**Solutions**:

1. **Font Availability**: Make sure the specified font family is installed on your system.

2. **Anti-aliasing**: Try toggling anti-aliasing:

   ```python
   my_text = pygameui.Text(
       position=(100, 100),
       content="Hello World",
       anti_aliasing=True  # or False
   )
   ```

3. **Size Issues**: If text is too small or large, adjust the font size:

   ```python
   my_text.set_font_size(24)  # Adjust as needed
   ```

## Animation Problems

### Animations Not Working

**Issue**: Flow or jump animations don't run.

**Solutions**:

1. **Animation State**: Make sure animation is enabled:

   ```python
   my_element.set_animate(True)
   ```

2. **Update Call**: Ensure you're calling update in your game loop:

   ```python
   my_element.update(events)
   ```

3. **Position Override**: Check that you're not setting the position manually after setting up animations:

   ```python
   # This will override your animation:
   # my_element.set_position((100, 100))
   ```

4. **Animation Setup**: Verify that animation parameters are correct:

   ```python
   # For flow animation:
   my_element.flow(
       start_position=(100, 100),
       end_position=(300, 100),
       time=1000,  # milliseconds
       loop=True
   )
   ```

## Performance Issues

### Slow Frame Rate

**Issue**: The application becomes slow when using multiple components.

**Solutions**:

1. **Optimize Updates**: Only update visible or active components:

   ```python
   # Only update visible components
   for component in components:
       if component.get_display():
           component.update(events)
   ```

2. **Reduce Animation**: Limit the number of animated components.

3. **Simplify Rendering**: Use simpler shapes or smaller images where possible.

4. **Text Caching**: For static text, consider creating it once and reusing:

   ```python
   # Create once
   my_text = pygameui.Text(position=(100, 100), content="Static Text")
   
   # In the game loop
   my_text.draw(screen)  # Just draw, no need to update static text
   ```

## Installation Issues

### Module Not Found

**Issue**: `ImportError: No module named 'pygameui'`

**Solutions**:

1. **File Location**: Make sure pygameui.py is in the same directory as your project.

2. **Running path**: Check that you're running your script from the correct directory. If you're using an IDE, ensure the working directory is set to where pygameui.py is located.

3. **Initialization**: Check that you've imported it correctly:

   ```python
   import pygameui  # Not 'from pygameui import ...'
   ```

## Additional Help

If you're still experiencing issues after trying these solutions:

1. **Check Examples**: Look at the [example code](examples/index.md) to see working implementations.

2. **Review Documentation**: Make sure you're using the components as described in the documentation.

3. **GitHub Issues**: Check [existing issues](https://github.com/trymbf/pygameui/issues) or create a new one with a detailed description of your problem.