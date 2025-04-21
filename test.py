
import pygameui as pgUI
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def cool():
    print(menu.get_selected_option())

menu = pgUI.DropdownMenu(
    position=(100, 100),
    options=list(range(1949, 2020)),
    element_width=70,
    element_height=30,
    on_change=cool

)

# Main loop
running = True
while running:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))  # Dark background

    # Update dropdown
    menu.update()

    # Draw elements
    menu.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)
 