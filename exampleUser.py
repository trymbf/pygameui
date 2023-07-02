import pygame, sys
import pygameUI as PGU

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
    for element in button_elements:
        element.draw(win)
        element.update()

    pygame.display.flip()

#  Text elements
text_elements = []
title = PGU.text((450, 90), "This is a title",  (244, 162, 97), fontSize = 100, font = "elephant")
undertitle = PGU.text((450, 150), "This is an undertitle", (233, 196, 106), fontSize = 20, font = "elephant")
text_elements.append(title)
undertitle.jump((450, 150), (450, 155), 40)
text_elements.append(undertitle)
# Button elements
button_elements = []
start_button = PGU.element((450, 300), rectWidth = 300, content = "Start!", rectColor = (233, 196, 106), textColor = (231, 111, 81))
start_button.flow((450, 305), (450, 315), 60)
button_elements.append(start_button)
sunset = pygame.transform.scale(pygame.image.load("sunset.png"), (100, 100)).convert()
sunset_button = PGU.element((10, 490), content = sunset, centerMode = False)
sunset_button.flow((10, 490), (30, 470), 60)
button_elements.append(sunset_button)

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if start_button.was_clicked(button_elements):
        undertitle.show = not undertitle.show
    if sunset_button.was_clicked(button_elements):
        sunset_button.flowing = not sunset_button.flowing

    draw(win)
    clock.tick(60)
