import pygame, sys, PyGameUI

pygame.init()

win = pygame.display.set_mode((500, 500))

example_element = PyGameUI.element((300, 300))

clock = pygame.time.Clock()
while True:
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    example_element.draw(win)

    pygame.display.flip()
    clock.tick(60)