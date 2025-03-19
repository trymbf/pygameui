# Image Element

The Image class allows you to display images in your UI.

## Basic Usage

```python
image = pygameui.Image(
    position=(100, 100),
    image_path="path/to/image.png",
    width=200,  # Optional
    height=150, # Optional
    scale=1,    # Optional
    centered=True
)
```

## Properties
```python
position: tuple[int, int],
image_path: str,
width: int = 0,
height: int = 0,
scale:int = 1,
centered: bool = False
```

- `position`: Tuple of (x, y) coordinates
- `image_path`: Path to the image file
- `width`: Width of the image (optional, 0 for auto, overrides scale)
- `height`: Height of the image (optional, 0 for auto, overrides scale)
- `scale`: Scale factor for the image (optional, default is 1)
- `centered`: If True, the image is centered on the provided position

## Supported Formats

- PNG (recommended)
- JPEG
- GIF (first frame only)
- BMP

## Image Scaling

Three ways to control image size:
1. Original size (no parameters)
2. Scale factor (`scale` parameter)
3. Exact dimensions (`width` and `height` parameters)

## Performance Tips

```python
# Efficient loading for multiple instances
shared_image = pygame.image.load("sprite.png")
for pos in positions:
    image = pygameui.Image(
        position=pos,
        image=shared_image
    )
```

## Best Practices

- Use appropriate image sizes
- Convert images to PNG for transparency
- Cache frequently used images
- Consider memory usage with large images
