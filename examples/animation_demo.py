import pygame
import pygameui
import math

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create UI elements
title = pygameui.Text(
    position=(400, 50),
    content="Animation Demo",
    color=(255, 255, 255),
    font_size=36,
    centered=True
)

# Create flow animation elements
flow_title = pygameui.Text(
    position=(400, 120),
    content="Flow Animation",
    color=(180, 180, 255),
    font_size=24,
    centered=True
)

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

# Create jump animation elements
jump_title = pygameui.Text(
    position=(400, 250),
    content="Jump Animation",
    color=(255, 180, 180),
    font_size=24,
    centered=True
)

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

# Create custom animation elements
custom_title = pygameui.Text(
    position=(400, 380),
    content="Custom Animation",
    color=(180, 255, 180),
    font_size=24,
    centered=True
)

custom_box = pygameui.Element(
    position=(400, 450),
    width=50,
    height=50,
    color=(100, 250, 100),
    border_radius=10,
    centered=True
)

# Animation controls
animation_controls = pygameui.Text(
    position=(400, 550),
    content="Press SPACE to toggle animations",
    color=(200, 200, 200),
    font_size=18,
    centered=True
)

# Animation state
animations_active = True

# Custom animation variables
angle = 0

# Main loop
running = True
while running:
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

    # Reset screen
    screen.fill((30, 30, 30))  # Dark background
    
    # Update UI elements
    title.update(events)
    flow_title.update(events)
    jump_title.update(events)
    custom_title.update(events)
    animation_controls.update(events)
    
    # Update animated elements
    flow_box.update(events)
    jump_box.update(events)
    
    # Custom animation (circular motion)
    if animations_active:
        angle += 0.02
        x = 400 + 150 * math.cos(angle)
        y = 450 + 40 * math.sin(angle)
        custom_box.set_position((x, y))
    custom_box.update(events)
    
    # Update animation controls text based on state
    if animations_active:
        animation_controls.set_content("Press SPACE to pause animations")
    else:
        animation_controls.set_content("Press SPACE to resume animations")
    
    # Draw UI elements
    title.draw(screen)
    flow_title.draw(screen)
    jump_title.draw(screen)
    custom_title.draw(screen)
    animation_controls.draw(screen)
    
    # Draw animated elements
    flow_box.draw(screen)
    jump_box.draw(screen)
    custom_box.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit pygame
pygame.quit()