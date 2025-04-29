# Components Overview

This guide demonstrates how PygameUI components work together to create cohesive user interfaces.

## Component Interactions

PygameUI is designed to make component interactions intuitive. Each component handles its own drawing, updating, and event processing, allowing you to focus on building your application logic.

### Basic Component Pattern

All PygameUI components follow the same basic pattern:

```python
# 1. Create component instances
my_component = pygameui.Component(
    position=(x, y),
    # Component-specific parameters
)

# 2. In the main loop:
# - Update components with events
my_component.update(events)
# - Draw components to the screen
my_component.draw(screen)
```

### Component Z-Order

Components are drawn in the order you call their `draw()` methods. To control which components appear on top of others, simply order your draw calls accordingly:

```python
# Background elements first
background.draw(screen)
# UI container elements
panel.draw(screen)
# Interactive elements
button.draw(screen)
# Foreground elements last
tooltip.draw(screen)
```

### Layout Management

PygameUI doesn't have an automatic layout system, but you can create organized layouts by:

1. **Grid Placement**: Position elements using calculated coordinates
2. **Relative Positioning**: Position elements relative to other elements
3. **Centered Alignment**: Use the `centered=True` parameter for alignment

Example of grid placement:

```python
# Create a 3x3 grid of buttons
buttons = []
for row in range(3):
    for col in range(3):
        button = pygameui.Button(
            position=(200 + col * 150, 150 + row * 100),
            width=100,
            height=50,
            label=f"Button {row*3 + col + 1}"
        )
        buttons.append(button)
```

## Best Practices

### Keeping a clean main loop
To keep your main loop clean and organized, consider sorting your components into lists based on their UI page or functionality. For example:

```python
# Organizing components by functionality
menu_components = [button1, button2, button3]
game_components = [player_stats_ui, enemy_ui, score_display]
settings_components = [volume_slider, resolution_dropdown]
```

This way, you can easily iterate through each list to update and draw components specific to that part of your application.
    
```python
# Main loop
running = True
while running:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Update and draw menu components
    for component in menu_components:
        component.update(events)
        component.draw(screen)

    # Update and draw game components
    for component in game_components:
        component.update(events)
        component.draw(screen)

    # Update and draw settings components
    for component in settings_components:
        component.update(events)
        component.draw(screen)

    pygame.display.flip()
```

### Event Handling

Always pass pygame events to all components:

```python
events = pygame.event.get()
for component in all_components:
    component.update(events)
```

### State Management

Track UI state separately from components:

```python
# Define UI states
UI_STATE_MAIN_MENU = 0
UI_STATE_GAME = 1
UI_STATE_SETTINGS = 2

# Current state
current_state = UI_STATE_MAIN_MENU

# Update and draw components based on state
if current_state == UI_STATE_MAIN_MENU:
    # Update and draw menu components
    for component in menu_components:
        component.update(events)
        component.draw(screen)
elif current_state == UI_STATE_GAME:
    # Update and draw game UI components
    for component in game_components:
        component.update(events)
        component.draw(screen)
# ... and so on
```

### Performance Optimization

For better performance:
- Only update visible components
- Use simple shapes and smaller images where possible
- Limit the number of animated components

### Organizing Component Groups

Group related components for easier management:

```python
player_stats_ui = {
    "container": pygameui.Element(position=(100, 100), width=200, height=150),
    "name": pygameui.Text(position=(100, 110), content="Player Name"),
    "health_bar": pygameui.ProgressBar(position=(100, 140), progress=100),
    "score": pygameui.Text(position=(100, 170), content="Score: 0")
}

# Update and draw all components in a group
for component in player_stats_ui.values():
    component.update(events)
    component.draw(screen)
```