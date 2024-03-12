import pygame, sys
import pygameui

pygame.init()

win = pygame.display.set_mode((500, 500))

# Adding one parameter
example_text = pygameui.Text((200, 200), "My cool text", (255, 255, 200), fontName = "elephant")
# Adding multiple parameters
example_text_2 = pygameui.Text((200, 200), "My cool not centermoded text", (255, 255, 100), fontSize = 50, centerMode = False)
clock = pygame.time.Clock()
while True:
    win.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    example_text.draw(win)
    example_text_2.draw(win)
    pygame.display.flip()
    clock.tick(60)