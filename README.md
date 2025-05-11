# PyGameUI

![PygameUI Logo](/docs/assets/imgs/logo.png)

A lightweight Python library that makes creating UI elements in Pygame quick and easy.

[![Version](https://img.shields.io/badge/version-2.2.1-blue.svg)](https://github.com/trymbf/pygameui/releases)
[![License](https://img.shields.io/github/license/trymbf/pygameui.svg)](LICENSE)

## Overview

`PygameUI` is a Python library that simplifies the creation of UI elements like buttons, text, inputs, and more when using Pygame. The library provides many customization options while keeping the implementation straightforward.

### Key Features

- 🎮 **Easy Integration** - Works seamlessly with existing Pygame projects
- 🎨 **Customizable Components** - Extensive styling options for all UI elements
- ✨ **Animation Support** - Built-in animations for UI elements
- 🧩 **Modular Design** - Mix and match components to create complex UI layouts

## Quick Start

```python
import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create a button
button = pygameui.Button(
    position=(400, 300),
    label="Click Me!",
    color=(100, 150, 250),
    hover_color=(120, 170, 255),
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
            
    # Update and draw button
    button.update(events)
    
    if button.was_clicked():
        print("Button clicked!")
        
    # Draw
    screen.fill((30, 30, 30))
    button.draw(screen)
    pygame.display.flip()
```

## Documentation

Full documentation is available at [https://trymbf.github.io/pygameui/](https://trymbf.github.io/pygameui/)

- [Getting Started Guide](https://trymbf.github.io/pygameui/getting-started)
- [Components Reference](https://trymbf.github.io/pygameui/components/element)

## Installation

1. Download the PyGameUI Python file from the [releases page](https://github.com/trymbf/pygameui/releases).
2. Place the file in your project directory.
3. Import it with `import pygameui`.

![Installation Example](https://trymbf.github.io/pygameui/assets/gifs/add_pygameui.gif)

## Available Components

- **Element** - Base class for all UI elements with positioning and animation
- **Text** - Text display with customizable fonts and styling
- **Button** - Interactive buttons with hover and click states
- **Image** - Display and manipulate images
- **Input** - Text input fields with customizable filters
- **Checkbox** - Toggle controls with various styles
- **ProgressBar** - Visual indicators for progress or completion
- **DropdownMenu** - Selectable dropdown menus
- **Table** - Grid-based data display

## Getting Help

- [GitHub Issues](https://github.com/trymbf/pygameui/issues) - Report bugs or request features
- [Documentation](https://trymbf.github.io/pygameui/) - Comprehensive guides and examples

## License

This project is licensed under the terms included in the [LICENSE](LICENSE) file.
