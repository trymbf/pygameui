import pygame, sys, string
import pygameuiOLD as pgu

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
title = pgu.Text((450, 90), "This is a title",  (244, 162, 97), font_size = 100, font_name = "elephant")
undertitle = pgu.Text((450, 150), "This is an undertitle", (233, 196, 106), font_size = 20, font_name = "elephant")
text_elements.append(title)
undertitle.jump((450, 150), (450, 155), 40)
text_elements.append(undertitle)
you_have_written = pgu.Text((450, 580), "You have written: ", (233, 196, 106), font_size = 20)
text_elements.append(you_have_written)
# Button elements
clickable_elements = []
start_button = pgu.Element((450, 300), rect_width = 300, content = "Start!", rect_color = (233, 196, 106), text_color = (231, 111, 81), font_size= 50)
start_button.flow((450, 305), (450, 315), 60)
clickable_elements.append(start_button)

# Input elements
input_element = pgu.Input((win_width//2, 400), example_content="Username")
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

    if start_button.is_hovered():
        start_button.change(new_text_color=(255, 255, 255), new_rect_color=(231, 111, 81))

    you_have_written.change("Username: " + input_element.getValue())
    input_element.work(events, clickable_elements)
    draw(win)
    clock.tick(60)
