# Components

PygameUI provides a variety of UI components to build interactive interfaces for your Pygame applications. All components share a common update-draw pattern and inherit from the base Element class.

## Component Hierarchy

```
Element
├── Text
│   └── Input
├── Button
├── Image
├── Checkbox
├── ProgressBar
├── DropdownMenu
└── Table
```

## Component Categories

### Basic Components

- [Element](element.md) - The foundation for all UI components with positioning, drawing, and animation capabilities
- [Text](text.md) - Display text with customizable fonts, colors, and sizes
- [Image](image.md) - Display and manipulate images with scaling and positioning options

### Interactive Components

- [Button](button.md) - Clickable buttons with hover and pressed states
- [Input](input.md) - Text input fields with filtering and validation
- [Checkbox](checkbox.md) - Toggle controls with various visual styles
- [DropdownMenu](dropdown-menu.md) - Selectable dropdown lists with customizable options

### Data Display Components

- [ProgressBar](progress-bar.md) - Visual indicators for progress or completion status
- [Table](table.md) - Grid-based data display for structured information

## Common Features

All components share these common features:

- **Positioning**: Set position with optional centering
- **Styling**: Customize colors, borders, and other visual aspects
- **Events**: Handle mouse interactions and clicks
- **Animation**: Apply built-in animations or create custom ones
- **Visibility**: Toggle display on/off

## Getting Started with Components

For a comprehensive overview of how components work together, see the [Components Overview](overview.md) guide.

For practical examples using these components, check out the [Examples](../examples/index.md) section.