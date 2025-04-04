import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create a basic element with animation
box = pygameui.Element(
    position=(100, 300),
    width=50,
    height=50,
    color=(255, 120, 80),  # Coral-like color
    border_radius=10
)

# Create an animated element
animated_box = pygameui.Element(
    position=(700, 300),
    width=50,
    height=50,
    color=(80, 200, 255),  # Light blue
    border_radius=10
)
# Set up a back-and-forth animation
animated_box.flow(
    start_position=(700, 300),
    end_position=(600, 300),
    time=1000,  # 1 second
    loop=True
)
animated_box.set_animate(True)

print("Click on the coral box to change its color")

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # When the static box is clicked, change its color
    if box.was_clicked():
        # Change to a random color
        r = pygame.time.get_ticks() % 255
        g = (pygame.time.get_ticks() // 2) % 255
        b = (pygame.time.get_ticks() // 4) % 255
        box.set_color((r, g, b))

    # Reset screen
    screen.fill((30, 30, 30))

    # Update elements
    box.update()
    animated_box.update()

    # Draw elements
    box.draw(screen)
    animated_box.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)