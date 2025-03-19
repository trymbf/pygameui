# Basic Tutorial

In this tutorial, we'll create a simple login form using PygameUI.

**Next:** [NaN](NaN) | **Previous:** [NaN](NaN)

## Step 1: Setup

```python
import pygame
import pygameui

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Login Form")
```

## Step 2: Create Elements

```python
username_input = pygameui.Input(
    position=(200, 100),
    width=200,
    height=30,
    hint="Username",
    centered=True
)

password_input = pygameui.Input(
    position=(200, 150),
    width=200,
    height=30,
    hint="Password",
    centered=True
)

login_button = pygameui.Button(
    position=(200, 200),
    content="Login",
    width=100,
    height=40,
    centered=True
)
```

## Step 3: Main Loop

```python
run = True
while run:
    events = pygame.event.get()
    # Allow user to close the window
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    # Update elements
    username_input.update(events)
    password_input.update(events)
    login_button.update()

    # Draw everything
    screen.fill((50, 50, 50))
    username_input.draw(screen)
    password_input.draw(screen)
    login_button.draw(screen)

    # Update screen
    pygame.display.flip()
```

**Next Steps:** NaN
