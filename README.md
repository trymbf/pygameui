# PyGameUI

Python library that makes making pygame-based-UIs easy!

## Short overview

`PygameUI` is a small Python library written in Python that makes it easier to create UI elements like buttons, texts, inputs, and more when using the Python library PyGame. The library also supplies the user with many optional features for customizing the UI elements.

PyGameUI is not that efficient, so I would not use it on larger games (not that most people would make large games in Python).

Still, if you are looking for a library that makes small projects and games a lot less of a headache, I would definitely recommend you give PyGameUI a try!

## Documentation

>Documentation in web form is available at https://trymbf.github.io/pygameui/

## Installation
Start by downloading the PyGameUI python file from the [releases page](https://github.com/trymbf/pygameui/releases).

Then place the PyGameUI file in the same folder as your project files.

![gif of putting the file in the same folder](https://trymbf.github.io/pygameui/assets//gifs//add_pygameui.gif)

## Available Elements
### Element
The base class for all UI elements. It provides basic functionality such as setting position, drawing, and updating.
### Text
A class for displaying text. It extends the `Element` class and adds text-specific attributes and methods.
### Image
A class for displaying images. It extends the `Element` class and adds image-specific attributes and methods.
### Input
A class for creating input fields. It extends the `Text` class and adds input-specific attributes and methods.
### Button
A class for creating buttons. It extends the `Element` class and adds button-specific attributes and methods.

## Learn more in the docs!
- [Getting Started](docs/getting-started.md)
- [Components Guide](docs/components/index.md)
- [Basic Tutorial](docs/tutorials/basic.md)
- [Animation Guide](docs/features/animation.md)


## Quick Links
- [Examples](docs/examples/index.md)
- [Gallery](docs/examples/gallery.md)

## Getting Help
- [GitHub Issues](https://github.com/trymbf/pygameui/issues)
