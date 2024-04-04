import pygame, sys, time
import pygameui as pgui

pygame.init()

win = pygame.display.set_mode((500, 500))

# Creating an input
element = pgui.Element((250, 250), content="Test")

elements = []
elements.append(element)

clock = pygame.time.Clock()
while True:
    win.fill((0, 0, 0))

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    element.change(newContent="Other", newTextColor=(255,0,0), newFontSize=50, newFontName="elephant")
    for elemente in elements:
        elemente.draw(win)
    # Updating the display
    pygame.display.flip()
    time.sleep(1)
    win.fill((0, 0, 0))
    element.change(newContent="Write something:", newTextColor=(255, 0, 255), newFontSize=30, newFontName="impact")
    element.draw(win)

    # Updating the display
    pygame.display.flip()
    time.sleep(1)