import pygame, sys, PyGameUI

pygame.init()

win = pygame.display.set_mode((500, 500))

example_element = PyGameUI.element((300, 300), content= "Kul knapp")
example_element.flow((300, 300), (300, 310), 10)

Titel = PyGameUI.text((100, 100), "Titel", (255, 255, 255))

clock = pygame.time.Clock()
while True:
    win.fill((0, 0, 0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    example_element.draw(win)
    Titel.draw(win)
    if example_element.is_hovered():
        example_element.update()

    if example_element.was_clicked([example_element]):
        Titel.show = not Titel.show

    

    pygame.display.flip()
    clock.tick(60)