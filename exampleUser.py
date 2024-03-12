import pygame, sys
import pygameui as pgu

pygame.init()

win_width = 900
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("This is a catption")

def draw(win):
    win.fill((38, 70, 83))

    for element in text_elements:
        element.draw(win)
        element.update()
    for element in clickable_elements:
        element.draw(win)
        element.update()

    pygame.display.flip()

#  Text elements
text_elements = []
title = pgu.Text((450, 90), "This is a title",  (244, 162, 97), fontSize = 100, fontName = "elephant")
undertitle = pgu.Text((450, 150), "This is an undertitle", (233, 196, 106), fontSize = 20, fontName = "elephant")
text_elements.append(title)
undertitle.jump((450, 150), (450, 155), 40)
text_elements.append(undertitle)
# Button elements
clickable_elements = []
start_button = pgu.Element((450, 300), rectWidth = 300, content = "Start!", rectColor = (233, 196, 106), textColor = (231, 111, 81), fontSize= 50)
start_button.flow((450, 305), (450, 315), 60)
clickable_elements.append(start_button)

input_element = pgu.Input((500, 500))
input_element.flow((500, 500), (300, 300), 50)
clickable_elements.append(input_element)

clock = pygame.time.Clock()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        

    if start_button.was_clicked(clickable_elements):
        undertitle.hide_toggle()
    
    input_element.work(events, clickable_elements)
    draw(win)
    clock.tick(60)
