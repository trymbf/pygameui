"""
# Oh hey there! You found the source code for the PygameGUI library!
# If you are lost and don't know how to use the library,
# check out the documentation at https://tbf3d.github.io/pygameui/
# Or if you know what you are doing, feel free to look around the code and see how it works!
# Or even contribute to the project!
"""

from time import time
import re
import pygame

pygame.init()

VERSION = 1.25

class Text:
    """
    Text class is used to create text objects that can be drawn on the screen.
    """
    def __init__(self,
                 position: tuple,
                 content:str,
                 color=(255, 255, 255),
                 center_mode = True,
                 font_name = "freesansbold.ttf",
                 font_size = 20
                 ):
        """
        Initializes the Text object.

        Args:
            position (tuple): The position of the text.
            content (str): The text content.
            color (tuple, optional): The color of the text. Defaults to (255, 255, 255).
            center_mode (bool, optional): Whether to center the text. Defaults to True.
            font_name (str, optional): The font name. Defaults to "freesansbold.ttf".
            font_size (int, optional): The font size. Defaults to 20.
        """
        # Basic variables
        # Pos
        self.x, self.y = position
        # Show, if false the text will not be drawn
        self.hide = False
        # Font
        self.font_name = font_name
        self.font_size = font_size
        self.font = pygame.font.SysFont(self.font_name, self.font_size)  # Load font
        # Text
        self.color = color
        self.content = content
        self.text = self.font.render(self.content, True, color) # Create surface object
        self.text_sect = self.text.get_rect() # Get rect of text
        # center_mode
        self.center_mode = center_mode
        # Position textRect based on center_mode
        center = (self.x - (self.text_sect.width // 2), self.y - (self.text_sect.height // 2))
        self.text_sect.topleft = center if self.center_mode else (self.x, self.y)

        # Other moving variables
        # Flowing
        self.flowing = False
        self.current_flow_pos = None
        self.other_flow_pos = None
        self.x_step = 0
        self.y_step = 0
        # Jumping
        self.jumping = False
        self.current_jump_pos = None
        self.other_jump_pos = None
        self.frames = 0
        self.frames_counter = 0

    def hide_toggle(self):
        """
        Toggles the hide variable, if true the text will not be drawn.
        """
        self.hide = not self.hide

    def jump_toggle(self):
        """
        Toggles the jumping variable, if true the text will jump between two points.
        """
        self.jumping = not self.jumping

    def flow_toggle(self):
        """
        Toggles the flowing variable, if true the text will flow between two points.
        """
        self.flowing = not self.flowing

    def get_pos(self):
        """
        Returns the position of the text object.
        """
        if self.center_mode:
            return self.text_sect.center

        return self.text_sect.topleft

    def change(self, new_content = None, new_color = None, new_font_name = None, new_font_size = None):
        """
        Changes the text object to new values.

        Args:
            new_content (str, optional): The new text content. Defaults to None.
            new_color (tuple, optional): The new text color. Defaults to None.
            new_font_name (str, optional): The new font name. Defaults to None.
            new_font_size (int, optional): The new font size. Defaults to None.
        """
        # If no new values are given, the old ones will be used
        if not new_content:
            new_content = self.content
        if not new_color:
            new_color = self.color
        if not new_font_name:
            new_font_name = self.font_name
        if not new_font_size:
            new_font_size = self.font_size

        # Create new surface object
        self.font = pygame.font.SysFont(new_font_name, new_font_size)  # Load font
        self.text = self.font.render(new_content, True, new_color)
        self.text_sect = self.text.get_rect() # Get rect
        # center_mode
        center = (self.x - (self.text_sect.width // 2), self.y - (self.text_sect.height // 2))
        self.text_sect.topleft = center if self.center_mode else (self.x, self.y)

        # Store the new values
        self.content = new_content
        self.color = new_color
        self.font_name = new_font_name
        self.font_size = new_font_size

    def draw(self, win):
        """
        Draws the text object on the screen.

        Args:
            win (pygame.Surface): The surface to draw the text on.
        """
        if not self.hide:
            win.blit(self.text, self.text_sect)

    def update(self):
        """
        Updates and moves the text if needed.
        """
        if self.flowing: # If flowing
            # Check if flow has reached a flow point
            # If center_mode is activated we will use the rects center position, if not the top left
            if self.center_mode:
                if self.x_step == 0 or self.y_step == 0:
                    if ((self.x_step > 0) and (self.text_sect.centerx > self.current_flow_pos[0])) or ((self.x_step < 0) and (self.text_sect.centerx < self.current_flow_pos[0])) or ((self.y_step < 0) and (self.text_sect.centery < self.current_flow_pos[1])) or ((self.y_step > 0) and (self.text_sect.centery > self.current_flow_pos[1])):
                        self.x_step, self.y_step = -self.x_step, -self.y_step # Switch directions, self.y_step = -self.x_step, -self.y_step # Switch direction
                        self.current_flow_pos, self.other_flow_pos = self.other_flow_pos, self.current_flow_pos
                else:
                    if (((self.x_step > 0) and (self.text_sect.centerx > self.current_flow_pos[0])) and ((self.y_step > 0) and (self.text_sect.centery > self.current_flow_pos[1]))) or (((self.x_step > 0) and (self.text_sect.centerx > self.current_flow_pos[0])) and ((self.y_step < 0) and (self.text_sect.centery < self.current_flow_pos[1]))) or (((self.x_step < 0) and (self.text_sect.centerx < self.current_flow_pos[0])) and ((self.y_step > 0) and (self.text_sect.centery > self.current_flow_pos[1])))or (((self.x_step < 0) and (self.text_sect.centerx < self.current_flow_pos[0])) and ((self.y_step < 0) and (self.text_sect.centery < self.current_flow_pos[1]))):
                        self.x_step, self.y_step = -self.x_step, -self.y_step # Switch direction
                        self.current_flow_pos, self.other_flow_pos = self.other_flow_pos, self.current_flow_pos
            else:
                if self.x_step == 0 or self.y_step == 0:
                    if ((self.x_step > 0) and (self.text_sect.x > self.current_flow_pos[0])) or ((self.x_step < 0) and (self.text_sect.x < self.current_flow_pos[0])) or ((self.y_step < 0) and (self.text_sect.y < self.current_flow_pos[1])) or ((self.y_step > 0) and (self.text_sect.y > self.current_flow_pos[1])):
                        self.x_step, self.y_step = -self.x_step, -self.y_step # Switch direction
                        self.current_flow_pos, self.other_flow_pos = self.other_flow_pos, self.current_flow_pos
                else:
                    if (((self.x_step > 0) and (self.text_sect.x > self.current_flow_pos[0])) and ((self.y_step > 0) and (self.text_sect.y > self.current_flow_pos[1]))) or (((self.x_step > 0) and (self.text_sect.x > self.current_flow_pos[0])) and ((self.y_step < 0) and (self.text_sect.y < self.current_flow_pos[1]))) or (((self.x_step < 0) and (self.text_sect.x < self.current_flow_pos[0])) and ((self.y_step > 0) and (self.text_sect.y > self.current_flow_pos[1])))or (((self.x_step < 0) and (self.text_sect.x < self.current_flow_pos[0])) and ((self.y_step < 0) and (self.text_sect.y < self.current_flow_pos[1]))):
                        self.x_step, self.y_step = -self.x_step, -self.y_step # Switch direction
                        self.current_flow_pos, self.other_flow_pos = self.other_flow_pos, self.current_flow_pos

            self.move(self.x_step, self.y_step) # Apply movement

        elif self.jumping: # If jumping
            self.frames_counter += 1 # Increase frame counter
            if self.frames_counter >= self.frames: # If it has gone enough time to switch position
                self.move_to(self.other_jump_pos[0], self.other_jump_pos[1]) # Apply movement
                self.current_jump_pos, self.other_jump_pos = self.other_jump_pos, self.current_jump_pos
                self.frames_counter = 0 # Reset counter

    def move_to(self, x: int, y: int):
        """
        Moves the text to specific coordinates.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
        """
        if self.center_mode:
            self.x = x - (self.text_sect.width // 2)
            self.y = y - (self.text_sect.height // 2)
            self.text_sect.topleft = (self.x, self.y)
        else:
            self.x, self.y = x, y
            self.text_sect.topleft = (self.x, self.y)

    def move(self, x_movement: float, y_movement: float):
        """
        Moves the text in x and y direction.

        Args:
            x_movement (float): The movement in x direction.
            y_movement (float): The movement in y direction.
        """
        # Used to make small movements posible (self.x is a float, self.textRect.x is an int)
        self.x += x_movement
        self.y += y_movement
        self.text_sect.x = self.x
        self.text_sect.y = self.y

    def is_hovered(self):
        """
        Returns if the text is hovered.

        Returns:
            bool: True if the text is hovered, False otherwise.
        """
        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self.text_sect.collidepoint(mouse_pos):
            return True

    def flow(self, position1: tuple, position2: tuple, iterations: int):
        """
        Lets the text flow between two points.

        Args:
            position1 (tuple): The first position.
            position2 (tuple): The second position.
            iterations (int): The number of iterations.
        """
        # Move to flowpoint
        self.move_to(position1[0], position1[1])
        # Set flowpostions
        self.other_flow_pos, self.current_flow_pos = position1, position2
        # Get amount to move per iteration
        x_distance, y_distance = (position2[0] - position1[0]), (position2[1] - position1[1])
        self.x_step = x_distance / iterations
        self.y_step = y_distance / iterations
        # Activate flowing
        self.flowing = True

    def jump(self, position1: tuple, position2: tuple, frames: int):
        """
        Lets the text jump between two points on a user-specified timer.

        Args:
            position1 (tuple): The first position.
            position2 (tuple): The second position.
            frames (int): The number of frames.
        """
        # Move to jumppoint
        self.move_to(position1[0], position1[1])
        # Set jumpPostions
        self.other_jump_pos, self.current_jump_pos = position2, position1
        # Frames
        self.frames = frames
        # Activate jumping
        self.jumping = True

class Element:
    """
    Element class is used to create UI elements that can be drawn on the screen.
    """
    def __init__(self, position: tuple, content=None, text_color=(231, 111, 81), center_text=True, center_mode=True, font_name="freesansbold.ttf", font_size=20, rect_width=200, rect_height=75, rect_color=(233, 196, 106), rect_border_radius=10):
        """
        Initializes the Element object.

        Args:
            position (tuple): The position of the element.
            content (str or pygame.Surface, optional): The content of the element. Defaults to None.
            text_color (tuple, optional): The color of the text. Defaults to (231, 111, 81).
            center_text (bool, optional): Whether to center the text. Defaults to True.
            center_mode (bool, optional): Whether to center the element. Defaults to True.
            font_name (str, optional): The font name. Defaults to "freesansbold.ttf".
            font_size (int, optional): The font size. Defaults to 20.
            rect_width (int, optional): The width of the rectangle. Defaults to 200.
            rect_height (int, optional): The height of the rectangle. Defaults to 75.
            rect_color (tuple, optional): The color of the rectangle. Defaults to (233, 196, 106).
            rect_border_radius (int, optional): The border radius of the rectangle. Defaults to 10.
        """
        # Common variables
        self.center_mode = center_mode
        self.content = content
        # Rect
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.rect_border_radius = rect_border_radius
        # Show
        self.hide = False
        self.size_multiplier= 1
        # Flowing
        self.flowing = False
        self.current_flow_pos = None
        self.other_flow_pos = None
        self.x_step = 0
        self.y_step = 0
        # Jumping
        self.jumping = False
        self.current_jump_pos = None
        self.other_jump_pos = None
        self.frames = 0
        self.frames_counter = 0
        # Clicking
        self.clicked = True

        if isinstance(self.content, str):
            self.type = "text"
            # Pos
            self.x, self.y = (position[0] - (rect_width // 2), position[1] - (rect_height // 2)) if self.center_mode else (position[0], position[1])
            # Rect
            self.rect = pygame.rect.Rect(self.x, self.y, rect_width, rect_height)
            self.rect_color = rect_color
            self.border_radius = rect_border_radius
            # Load font
            self.font_name = font_name
            self.font_size = font_size
            self.font = pygame.font.SysFont(self.font_name, self.font_size)  # Load font
            # Text
            self.center_text = center_text
            self.text_color = text_color
            self.text = self.font.render(content, True, text_color) # Create surface object
            self.text_rect = self.text.get_rect() # Get rect
            # centering the text
            if center_text:
                self.text_rect.center = self.rect.center
            else: self.text_rect.topleft = self.rect.topleft
        # If there is an image
        elif self.content:
            self.type = "image"
            try:
                self.content = pygame.transform.scale(self.content, (self.rect_width, self.rect_height))
                self.rect = self.content.get_rect()
            except:
                raise Exception(f"{self.content} is not a pygame image")

            if self.center_mode:
                # Pos
                self.rect.center = (position[0], position[1])
                # Pos
                self.x, self.y = self.rect.center
            else:
                self.rect.topleft = (position[0], position[1])
                self.x, self.y = self.rect.topleft
        # If there is no content (only a rectangle)
        else:
            self.type = "rectangle"
            # Pos
            self.x, self.y = (position[0] - (self.rect_width // 2), position[1] - (self.rect_height // 2)) if self.center_mode else (position[0], position[1])
            # Rect
            self.rect = pygame.rect.Rect(self.x, self.y, self.rect_width, self.rect_height)
            self.border_radius = rect_border_radius
            self.rect_color = rect_color

    def get_pos(self):
        """
        Returns the position of the element.

        Returns:
            tuple: The position of the element.
        """
        if self.center_mode:
            return self.rect.center

        return self.rect.topleft

    def change(self, new_content = None, new_text_color = None, new_font_name = None, new_font_size = None, new_rect_color = None, new_rect_width = None, new_rect_height = None, new_rect_border_radius = None):
        """
        Changes the element to new values.

        Args:
            new_content (str or pygame.Surface, optional): The new content. Defaults to None.
            new_text_color (tuple, optional): The new text color. Defaults to None.
            new_font_name (str, optional): The new font name. Defaults to None.
            new_font_size (int, optional): The new font size. Defaults to None.
            new_rect_color (tuple, optional): The new rectangle color. Defaults to None.
            new_rect_width (int, optional): The new rectangle width. Defaults to None.
            new_rect_height (int, optional): The new rectangle height. Defaults to None.
            new_rect_border_radius (int, optional): The new rectangle border radius. Defaults to None.
        """
        if self.type == "text":
            # If no new values are given, the old ones will be used
            if not new_content:
                new_content = self.content
            if not new_text_color:
                new_text_color = self.text_color
            if not new_font_name:
                new_font_name = self.font_name
            if not new_font_size:
                new_font_size = self.font_size
            if not new_rect_color:
                new_rect_color = self.rect_color
            if not new_rect_width:
                new_rect_width = self.rect_width
            if not new_rect_height:
                new_rect_height = self.rect_height
            if not new_rect_border_radius:
                new_rect_border_radius = self.border_radius

            # Rect
            self.rect = pygame.rect.Rect(self.x, self.y, new_rect_width, new_rect_height)

            self.rect_color = new_rect_color
            self.border_radius = new_rect_border_radius

            # Create new surface object
            self.font = pygame.font.SysFont(new_font_name, new_font_size)  # Load font
            self.text = self.font.render(new_content, True, new_text_color)
            self.text_rect = self.text.get_rect() # Get rect
            if self.center_text:
                self.text_rect.center = self.rect.center
            else:
                self.text_rect.topleft = self.rect.topleft


            # Store the new values
            self.content = new_content
            self.text_color = new_text_color
            self.font_name = new_font_name
            self.font_size = new_font_size
            self.rect_width = new_rect_width
            self.rect_height = new_rect_height
            self.rect_border_radius = new_rect_border_radius
        elif self.type == "image":
            if not new_content:
                new_content = self.content
            if not new_rect_width:
                new_rect_width = self.rect_width
            if not new_rect_height:
                new_rect_height = self.rect_height

            try:
                self.content = pygame.transform.scale(new_content, (new_rect_width, new_rect_height))
                last_rect = self.rect
                self.rect = self.content.get_rect()
                self.rect.topleft = last_rect.topleft
            except:
                raise Exception(f"{self.content} is not a pygame image")

            # Store the new values
            self.content = new_content
            self.rect_width = new_rect_width
            self.rect_height = new_rect_height
        elif self.type == "rectangle":
            if not new_rect_color:
                new_rect_color = self.rect_color
            if not new_rect_width:
                new_rect_width = self.rect_width
            if not new_rect_height:
                new_rect_height = self.rect_height
            if not new_rect_border_radius:
                new_rect_border_radius = self.border_radius

            self.rect = pygame.rect.Rect(self.rect.x, self.rect.y, new_rect_width, new_rect_height)
            self.rect_color = new_rect_color
            self.border_radius = new_rect_border_radius

            # Store the new values
            self.rect_width = new_rect_width
            self.rect_height = new_rect_height
            self.rect_border_radius = new_rect_border_radius

    def hide_toggle(self):
        """
        Toggles the hide variable, if true the element will not be drawn.
        """
        self.hide = not self.hide

    def jump_toggle(self):
        """
        Toggles the jumping variable, if true the element will jump between two points.
        """
        self.jumping = not self.jumping

    def flow_toggle(self):
        """
        Toggles the flowing variable, if true the element will flow between two points.
        """
        self.flowing = not self.flowing

    def draw(self, win):
        """
        Draws the element on the screen.

        Args:
            win (pygame.Surface): The surface to draw the element on.
        """
        if not self.hide:
            # If the element has text
            if self.type == "text":
                # Draw text
                pygame.draw.rect(win, self.rect_color, self.rect, border_radius = self.border_radius)
                win.blit(self.text, self.text_rect)
            # If the element has an image
            elif self.type == "image":
                # Draw img
                win.blit(self.content, self.rect)
            # If the element is a just rectangle
            elif self.type == "rectangle":
                pygame.draw.rect(win, self.rect_color, self.rect, border_radius = self.border_radius)

    def is_hovered(self):
        """
        Returns if the element is hovered.

        Returns:
            bool: True if the element is hovered, False otherwise.
        """
        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            return True

    def is_clicked(self, clickable_elements: list):
        """
        Returns if the element is clicked.

        Args:
            clickable_elements (list): The list of clickable elements.

        Returns:
            bool: True if the element is clicked, False otherwise.
        """
        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1: # == 1 is left click
                return True
        else:
            for element in clickable_elements: # Checks if user is howering any other buttons
                if element.rect.collidepoint(mouse_pos):
                    break
            else: # If not howering any other buttons: set cursor to arrow
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def was_clicked(self, clickable_elements: list):
        """
        Returns if the element was clicked.

        Args:
            clickable_elements (list): The list of clickable elements.

        Returns:
            bool: True if the element was clicked, False otherwise.
        """
        action = False

        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # == 1 is left click
                self.clicked = True
                action = True
        else:
            for element in clickable_elements:
                if element.rect.collidepoint(mouse_pos):
                    break
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if pygame.mouse.get_pressed()[0] == 0: #  No mousebuttons down
            self.clicked = False

        return action

    def update(self):
        """
        Updates and moves the element if needed.
        """
        if self.flowing: # If flowing
            # Check if flow has reached a flowpoint
            if self.center_mode: # If centermode is activated we will use the rects centerposition, if not the topleft
                if self.x_step == 0 or self.y_step == 0:
                    if ((self.x_step > 0) and (self.rect.centerx > self.current_flow_pos[0])) or ((self.x_step < 0) and (self.rect.centerx < self.current_flow_pos[0])) or ((self.y_step < 0) and (self.rect.centery < self.current_flow_pos[1])) or ((self.y_step > 0) and (self.rect.centery > self.current_flow_pos[1])):
                        self.x_step, self.y_step = -self.x_step, -self.y_step # Switch direction
                        self.current_flow_pos, self.other_flow_pos = self.other_flow_pos, self.current_flow_pos
                else:
                    if (((self.x_step > 0) and (self.rect.centerx > self.current_flow_pos[0])) and ((self.y_step > 0) and (self.rect.centery > self.current_flow_pos[1]))) or (((self.x_step > 0) and (self.rect.centerx > self.current_flow_pos[0])) and ((self.y_step < 0) and (self.rect.centery < self.current_flow_pos[1]))) or (((self.x_step < 0) and (self.rect.centerx < self.current_flow_pos[0])) and ((self.y_step > 0) and (self.rect.centery > self.current_flow_pos[1])))or (((self.x_step < 0) and (self.rect.centerx < self.current_flow_pos[0])) and ((self.y_step < 0) and (self.rect.centery < self.current_flow_pos[1]))):
                        self.x_step, self.y_step = -self.x_step, -self.y_step # Switch direction
                        self.current_flow_pos, self.other_flow_pos = self.other_flow_pos, self.current_flow_pos
            else:
                if self.x_step == 0 or self.y_step == 0:
                    if ((self.x_step > 0) and (self.rect.x > self.current_flow_pos[0])) or ((self.x_step < 0) and (self.rect.x < self.current_flow_pos[0])) or ((self.y_step < 0) and (self.rect.y < self.current_flow_pos[1])) or ((self.y_step > 0) and (self.rect.y > self.current_flow_pos[1])):
                        self.x_step, self.y_step = -self.x_step, -self.y_step # Switch direction
                        self.current_flow_pos, self.other_flow_pos = self.other_flow_pos, self.current_flow_pos
                else:
                    if (((self.x_step > 0) and (self.rect.x > self.current_flow_pos[0])) and ((self.y_step > 0) and (self.rect.y > self.current_flow_pos[1]))) or (((self.x_step > 0) and (self.rect.x > self.current_flow_pos[0])) and ((self.y_step < 0) and (self.rect.y < self.current_flow_pos[1]))) or (((self.x_step < 0) and (self.rect.x < self.current_flow_pos[0])) and ((self.y_step > 0) and (self.rect.y > self.current_flow_pos[1])))or (((self.x_step < 0) and (self.rect.x < self.current_flow_pos[0])) and ((self.y_step < 0) and (self.rect.y < self.current_flow_pos[1]))):
                        self.x_step, self.y_step = -self.x_step, -self.y_step # Switch direction
                        self.current_flow_pos, self.other_flow_pos = self.other_flow_pos, self.current_flow_pos

            self.move(self.x_step, self.y_step) # Apply movement

        elif self.jumping: # If jumping
            self.frames_counter += 1 # Increase frame counter
            if self.frames_counter >= self.frames: # If it has gone enough time to switch position
                self.move_to(self.other_jump_pos[0], self.other_jump_pos[1]) # Apply movement
                self.current_jump_pos, self.other_jump_pos = self.other_jump_pos, self.current_jump_pos
                self.frames_counter = 0 # Reset counter

    def move_to(self, x: int, y: int):
        """
        Moves the element to specific coordinates.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
        """
        if self.center_mode:
            self.rect.center = (x, y)
            self.x, self.y = self.rect.center
            if self.type == "text": # Only affect the textRect if there is text
                if self.center_text:
                    self.text_rect.center = self.rect.center
                else:
                    self.text_rect.topleft = self.rect.topleft
        else:
            self.rect.topleft = (x, y)
            self.x, self.y = self.rect.topleft
            if self.type == "text": # Only affect the textRect if there is text
                if self.center_text:
                    self.text_rect.center = self.rect.center
                else:
                    self.text_rect.topleft = self.rect.topleft

    def move(self, x_movement: float, y_movement: float):
        """
        Moves the element in x and y direction.

        Args:
            x_movement (float): The movement in x direction.
            y_movement (float): The movement in y direction.
        """
        # Used to make small movements posible (self.x is a float, self.textRect.x is an int)
        self.x += x_movement
        self.y += y_movement
        if self.center_mode:
            self.rect.center = (self.x, self.y)
            if self.type == "text": # Only affect the textRect if there is text
                if self.center_text:
                    self.text_rect.center = self.rect.center
                else:
                    self.text_rect.topleft = self.rect.topleft
        else:
            self.rect.topleft = (self.x, self.y)
            if self.type == "text": # Only affect the textRect if there is text
                if self.center_text:
                    self.text_rect.center = self.rect.center
                else:
                    self.text_rect.topleft = self.rect.topleft

    def flow(self, position1: tuple, position2: tuple, iterations: int):
        """
        Lets the element flow between two points.

        Args:
            position1 (tuple): The first position.
            position2 (tuple): The second position.
            iterations (int): The number of iterations.
        """
        # Move to flowpoint
        self.move_to(position1[0], position1[1])
        # Set flowpostions
        self.other_flow_pos, self.current_flow_pos = position1, position2
        # Get amount to move per iteration
        xdistance, ydistance = (position2[0] - position1[0]), (position2[1] - position1[1])
        self.x_step = xdistance / iterations
        self.y_step = ydistance / iterations
        # Activate flowing
        self.flowing = True

    def jump(self, position1: tuple, position2: tuple, iterations: int):
        """
        Lets the element jump between two points on a user-specified timer.

        Args:
            position1 (tuple): The first position.
            position2 (tuple): The second position.
            iterations (int): The number of iterations.
        """
        # Move to jumppoint
        self.move_to(position1[0], position1[1])
        # Set jumpPostions
        self.other_jump_pos, self.current_jump_pos = position2, position1
        # Frames
        self.frames = iterations
        # Activate jumping
        self.jumping = True

class Input:
    """
    Input class is used to create input fields that can be drawn on the screen.
    """
    def __init__(self, position: tuple, font_name ="freesansbold.ttf", font_size = 30, example_content ="Click me to input!", prefilled_content ="", character_limit = 100, normal_text_color = (231, 111, 81), example_text_color = (100, 100, 100), rect_width = 200, rect_height = 50, rect_color_active = (233, 196, 106), rect_color_passive = (200, 200, 200), rect_border_radius = 1, rect_border_width = 5, center_mode = True):
        """
        Initializes the Input object.

        Args:
            position (tuple): The position of the input field.
            font_name (str, optional): The font name. Defaults to "freesansbold.ttf".
            font_size (int, optional): The font size. Defaults to 30.
            example_content (str, optional): The example content. Defaults to "Click me to input!".
            prefilled_content (str, optional): The prefilled content. Defaults to "".
            character_limit (int, optional): The character limit. Defaults to 100.
            normal_text_color (tuple, optional): The normal text color. Defaults to (231, 111, 81).
            example_text_color (tuple, optional): The example text color. Defaults to (100, 100, 100).
            rect_width (int, optional): The width of the rectangle. Defaults to 200.
            rect_height (int, optional): The height of the rectangle. Defaults to 50.
            rect_color_active (tuple, optional): The active rectangle color. Defaults to (233, 196, 106).
            rect_color_passive (tuple, optional): The passive rectangle color. Defaults to (200, 200, 200).
            rect_border_radius (int, optional): The border radius of the rectangle. Defaults to 1.
            rect_border_width (int, optional): The border width of the rectangle. Defaults to 5.
            center_mode (bool, optional): Whether to center the input field. Defaults to True.
        """
        pygame.scrap.init()
        pygame.scrap.set_mode(pygame.SCRAP_CLIPBOARD)

        # Create position variables and font
        self.center_mode = center_mode
        # Pos
        self.x, self.y = (position[0] - (rect_width // 2), position[1] - (rect_height // 2)) if center_mode else (position[0], position[1])
        # Rect
        self.rect = pygame.rect.Rect(self.x, self.y, rect_width, rect_height)
        self.border_radius = rect_border_radius
        self.rect_border_width = rect_border_width
        self.rect_color_passive = rect_color_passive
        self.rectColorActive = rect_color_active
        # Text
        self.normal_text_color = normal_text_color
        self.example_text_color = example_text_color
        self.character_limit = character_limit
        self.font_name = font_name
        self.font_size = font_size
        self.font = pygame.font.SysFont(self.font_name, self.font_size)  # Load font
        self.prefilled_content = prefilled_content
        self.user_text = self.prefilled_content
        self.example_content = example_content
        self.user_text_surface = self.font.render(self.user_text, True, self.normal_text_color) # Create surface object for the user_text
        self.example_text_surface = self.font.render(self.example_content, True, self.example_text_color) # Create surface object the exampleText

        self.user_text_rect = self.user_text_surface.get_rect() # Get rect
        self.example_text_rect = self.example_text_surface.get_rect() # Get rect

        # Filter
        self.filter_mode = "is_allowed" # is_allowed or isDisallowed, if is_allowed the filter_list will only allow the characters in the filter_list, if isDisallowed the filter_list will disallow the characters in the filter_list
        self.filter = None

        # Cursor
        self.cursor_visible_timer = 60
        self.cursor_index = len(self.user_text)

        # centering the text
        self.user_text_rect.center = self.rect.center
        self.example_text_rect.center = self.rect.center
        # Show
        self.hide = False
        # Flowing
        self.flowing = False
        self.currentFlowPos = None
        self.otherFlowPos = None
        self.x_step = 0
        self.y_step = 0
        # Jumping
        self.jumping = False
        self.currentJumpPos = None
        self.otherJumpPos = None
        self.frames = 0
        self.frames_counter = 0
        # Clicking
        self.clicked = False
        self.active = False

        # Key down
        self.key_down_dict = {} #
        self.key_down_time = 0
        self.long_press_active = False
        self.key_down_last_frame = False
        self.min_hold_time = .5 # The minimun time between key reaction

    def hide_toggle(self):
        """
        Toggles the hide variable, if true the input field will not be drawn.
        """
        self.hide = not self.hide

    def get_pos(self):
        """
        Returns the position of the input field.

        Returns:
            tuple: The position of the input field.
        """
        if self.center_mode:
            return self.rect.center
        else:
            return self.rect.topleft

    def jump_toggle(self):
        """
        Toggles the jumping variable, if true the input field will jump between two points.
        """
        self.jumping = not self.jumping

    def flow_toggle(self):
        """
        Toggles the flowing variable, if true the input field will flow between two points.
        """
        self.flowing = not self.flowing

    def set_filter(self, filter_list: list, is_allowed: bool = True):
        """
        Sets the filter for the input field.

        Args:
            filter_list (list): The list of allowed or disallowed characters.
            is_allowed (bool, optional): Whether the filter is allowed or disallowed. Defaults to True.
        """
        self.filter = filter_list
        self.filter_mode = "is_allowed" if is_allowed else "isDisallowed"

    def get_relative_cursor_position(self) -> int:
        """
        Returns the relative cursor position.

        Returns:
            int: The relative cursor position.
        """
        substring = self.user_text[:self.cursor_index]
        return self.font.size(substring)[0]

    def get_letter_position(self, letter_index: int) -> int:
        """
        Returns the position of a letter.

        Args:
            letter_index (str): The index of the letter.

        Returns:
            int: The position of the letter.
        """
        substring = self.user_text[:letter_index]
        return self.font.size(substring)[0] + self.user_text_rect.left

    def draw(self, win):
        """
        Draws the input field on the screen.

        Args:
            win (pygame.Surface): The surface to draw the input field on.
        """
        if not self.hide:
            if self.user_text != "":
                win.blit(self.user_text_surface, self.user_text_rect)
            else:
                if not self.active:
                    win.blit(self.example_text_surface, self.example_text_rect)

            if self.active:
                # Draw rect
                pygame.draw.rect(win, self.rectColorActive, self.rect, self.rect_border_width, border_radius = self.border_radius)

                # Draw cursor and make it blink
                self.cursor_visible_timer -= 1
                if self.cursor_visible_timer > 30:
                    cursor_pos = self.get_relative_cursor_position() + self.user_text_rect.left
                    pygame.draw.line(win, self.normal_text_color, (cursor_pos, self.user_text_rect.top), (cursor_pos, self.user_text_rect.bottom), self.font_size // 15)
                elif self.cursor_visible_timer == 0:
                    self.cursor_visible_timer = 60

            else:
                pygame.draw.rect(win, self.rect_color_passive, self.rect, self.rect_border_width, border_radius = self.border_radius)

    def get_value(self):
        """
        Returns the value of the input field.

        Returns:
            str: The value of the input field.
        """
        return self.user_text

    def backspace(self):
        """
        Deletes the character before the cursor.
        """
        if self.cursor_index == len(self.user_text):
            self.user_text = self.user_text[0: -1]
            if self.cursor_index > 0:
                self.cursor_index -= 1
        elif self.cursor_index != 0:
            self.user_text = self.user_text[0: self.cursor_index - 1] + self.user_text[self.cursor_index:]
            if self.cursor_index > 0:
                self.cursor_index -= 1

    def update_text(self):
        """
        Updates the text of the input field.
        """
        # Update the text
        self.user_text_surface = self.font.render(self.user_text, True, self.normal_text_color) # Create surface object for the user_text
        self.user_text_rect = self.user_text_surface.get_rect() # Get rect
        self.user_text_rect.center = self.rect.center

    def work(self, events: list, clickable_elements: list):
        """
        Handles the input field events.

        Args:
            events (list): The list of events.
            clickable_elements (list): The list of clickable elements.
        """
        # Make activating work
        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # == 1 is left click
                if self.active:
                    # Move cursor to the position of the mouse
                    new_cursor_index = 0
                    for letter_index in range(len(self.user_text)):
                        letter_pos = self.get_letter_position(letter_index)
                        if letter_pos - (self.font.size((self.user_text[letter_index]))[0] // 2) < mouse_pos[0]:
                            new_cursor_index = letter_index

                    # If the mouse is to the right of the text
                    if (self.font.size(self.user_text)[0] + self.user_text_rect.left) < mouse_pos[0]:
                        new_cursor_index = len(self.user_text)

                    self.cursor_index = new_cursor_index
                else:
                    self.active = True
                    # Move cursor to the end of the text
                    self.cursor_index = len(self.user_text)

                self.cursor_visible_timer = 60
                self.clicked = True
        else:
            if pygame.mouse.get_pressed()[0]: # == 1 is left click
                self.active = False
            for element in clickable_elements:
                if element.rect.collidepoint(mouse_pos):
                    break
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if pygame.mouse.get_pressed()[0] == 0: #  No mousebuttons down
            self.clicked = False

        # Make backspace work
        inputs  = pygame.key.get_pressed()

        if self.active:
            if inputs[pygame.K_BACKSPACE]:
                if (not self.long_press_active) and self.key_down_last_frame and (time() - self.key_down_time > .4):
                    self.long_press_active = True
                    self.min_hold_time = .07

                if (time() - self.key_down_time > self.min_hold_time) or not self.key_down_last_frame:
                    self.backspace()
                    self.update_text()
                    self.key_down_time = time()
                    self.key_down_last_frame = True

            else:
                self.key_down_last_frame = False
                self.long_press_active = False
                self.min_hold_time = .5

        # Make writing work
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.active:
                    # Allow the user to paste text from clipboard
                    if event.key == pygame.K_v and event.mod & pygame.KMOD_CTRL:
                        pasted_text = pygame.scrap.get("text/plain;charset=utf-8").decode()
                        # Remove all non-printable characters
                        pasted_text = re.sub(r'[^\x20-\x7E]+', '', pasted_text)

                        # Filter the pasted text
                        for letter in pasted_text:
                            if self.filter_mode == "is_allowed" and letter not in self.filter:
                                pasted_text = pasted_text.replace(letter, "")
                            elif self.filter_mode == "isDisallowed" and letter in self.filter:
                                pasted_text = pasted_text.replace(letter, "")
                        # Check that the pasted text is not exceeding the character limit
                        if len(self.user_text) + len(pasted_text) > self.character_limit:
                            continue

                        self.user_text = self.user_text[0: self.cursor_index] + pasted_text + self.user_text[self.cursor_index:]
                        # Move cursor to the end of the pasted text
                        self.cursor_index += len(pasted_text)
                    elif event.key == pygame.K_BACKSPACE:
                        pass
                    elif event.key == pygame.K_DELETE:
                        if self.cursor_index != len(self.user_text):
                            self.user_text = self.user_text[0: self.cursor_index] + self.user_text[self.cursor_index + 1:]
                    elif event.key == pygame.K_HOME:
                        self.cursor_index = 0
                    elif event.key == pygame.K_END:
                        self.cursor_index = len(self.user_text)
                    elif event.key == pygame.K_TAB:
                        self.user_text = self.user_text[0: self.cursor_index] + "    " + self.user_text[self.cursor_index:]
                        self.cursor_index += 4
                    # Allow the user to move the cursor
                    elif event.key == pygame.K_LEFT:
                        if self.cursor_index > 0:
                            self.cursor_index -= 1
                    elif event.key == pygame.K_RIGHT:
                        if self.cursor_index < len(self.user_text):
                            self.cursor_index += 1
                    # Filter
                    elif self.filter and ((self.filter_mode == "is_allowed" and (event.unicode not in self.filter)) or (self.filter_mode == "isDisallowed" and (event.unicode in self.filter))):
                        continue
                    # Allow the user to write text
                    elif len(self.user_text) <= self.character_limit: # Keep text under character limit and don't enterperate enter as a key
                        if event.unicode and event.key != pygame.K_RETURN:
                            self.user_text = self.user_text[0: self.cursor_index] + event.unicode + self.user_text[self.cursor_index:] # Adds the userinput to the text
                            self.cursor_index += 1

                    # Update the text
                    self.user_text_surface = self.font.render(self.user_text, True, self.normal_text_color) # Create surface object for the user_text
                    self.user_text_rect = self.user_text_surface.get_rect() # Get rect
                    self.user_text_rect.center = self.rect.center

    def update(self):
        """
        Updates and moves the input field if needed.
        """
        if self.flowing: # If flowing
            # Check if flow has reached a flowpoint
            if self.center_mode: # If centermode is activated we will use the rects centerposition, if not the topleft
                if self.x_step == 0 or self.y_step == 0:
                    if ((self.x_step > 0) and (self.rect.centerx > self.currentFlowPos[0])) or ((self.x_step < 0) and (self.rect.centerx < self.currentFlowPos[0])) or ((self.y_step < 0) and (self.rect.centery < self.currentFlowPos[1])) or ((self.y_step > 0) and (self.rect.centery > self.currentFlowPos[1])):
                        self.x_step, self.y_step = -self.x_step, -self.y_step # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos
                else:
                    if (((self.x_step > 0) and (self.rect.centerx > self.currentFlowPos[0])) and ((self.y_step > 0) and (self.rect.centery > self.currentFlowPos[1]))) or (((self.x_step > 0) and (self.rect.centerx > self.currentFlowPos[0])) and ((self.y_step < 0) and (self.rect.centery < self.currentFlowPos[1]))) or (((self.x_step < 0) and (self.rect.centerx < self.currentFlowPos[0])) and ((self.y_step > 0) and (self.rect.centery > self.currentFlowPos[1])))or (((self.x_step < 0) and (self.rect.centerx < self.currentFlowPos[0])) and ((self.y_step < 0) and (self.rect.centery < self.currentFlowPos[1]))):
                        self.x_step, self.y_step = -self.x_step, -self.y_step # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos
            else:
                if self.x_step == 0 or self.y_step == 0:
                    if ((self.x_step > 0) and (self.rect.x > self.currentFlowPos[0])) or ((self.x_step < 0) and (self.rect.x < self.currentFlowPos[0])) or ((self.y_step < 0) and (self.rect.y < self.currentFlowPos[1])) or ((self.y_step > 0) and (self.rect.y > self.currentFlowPos[1])):
                        self.x_step, self.y_step = -self.x_step, -self.y_step # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos
                else:
                    if (((self.x_step > 0) and (self.rect.x > self.currentFlowPos[0])) and ((self.y_step > 0) and (self.rect.y > self.currentFlowPos[1]))) or (((self.x_step > 0) and (self.rect.x > self.currentFlowPos[0])) and ((self.y_step < 0) and (self.rect.y < self.currentFlowPos[1]))) or (((self.x_step < 0) and (self.rect.x < self.currentFlowPos[0])) and ((self.y_step > 0) and (self.rect.y > self.currentFlowPos[1])))or (((self.x_step < 0) and (self.rect.x < self.currentFlowPos[0])) and ((self.y_step < 0) and (self.rect.y < self.currentFlowPos[1]))):
                        self.x_step, self.y_step = -self.x_step, -self.y_step # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos

            self.move(self.x_step, self.y_step) # Apply movement

        elif self.jumping: # If jumping
            self.frames_counter += 1 # Increase frame counter
            if self.frames_counter >= self.frames: # If it has gone enough time to switch position
                self.move_to(self.otherJumpPos[0], self.otherJumpPos[1]) # Apply movement
                self.currentJumpPos, self.otherJumpPos = self.otherJumpPos, self.currentJumpPos
                self.frames_counter = 0 # Reset counter

    def move_to(self, x: int, y: int):
        """
        Moves the input field to specific coordinates.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
        """
        if self.center_mode:
            self.rect.center = (x, y)
            self.x, self.y = self.rect.center
            self.user_text_rect.center = (x, y)
            self.example_text_rect.center = (x, y)
        else:
            self.rect.topleft = (x, y)
            self.x, self.y = self.rect.topleft
            self.user_text_rect.topleft = (self.x, self.y)
            self.example_text_rect.topleft = (self.x, self.y)

    def move(self, x_movement: float, y_movement: float):
        """
        Moves the input field in x and y direction.

        Args:
            x_movement (float): The movement in x direction.
            y_movement (float): The movement in y direction.
        """
        # Used to make small movements possible (self.x is a float, self.textRect.x is an int)
        self.x += x_movement
        self.y += y_movement
        if self.center_mode:
            self.rect.center = (self.x, self.y)
            self.user_text_rect.center = (self.x, self.y)
            self.example_text_rect.center = (self.x, self.y)
        else:
            self.rect.topleft = (self.x, self.y)
            self.user_text_rect.topleft = (self.x, self.y)
            self.example_text_rect.topleft = (self.x, self.y)

    def is_hovered(self):
        """
        Returns if the input field is hovered.

        Returns:
            bool: True if the input field is hovered, False otherwise.
        """
        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            return True

    def flow(self, position1: tuple, position2: tuple, iterations: int):
        """
        Lets the input field flow between two points.

        Args:
            position1 (tuple): The first position.
            position2 (tuple): The second position.
            iterations (int): The number of iterations.
        """
        # Move to flowpoint
        self.move_to(position1[0], position1[1])
        # Set flowpostions
        self.otherFlowPos, self.currentFlowPos = position1, position2
        # Get amount to move per iteration
        x_distance, y_distance = (position2[0] - position1[0]), (position2[1] - position1[1])
        self.x_step = x_distance / iterations
        self.y_step = y_distance / iterations
        # Activate flowing
        self.flowing = True

    def jump(self, position1: tuple, position2: tuple, frames: int):
        """
        Lets the input field jump between two points on a user-specified timer.

        Args:
            position1 (tuple): The first position.
            position2 (tuple): The second position.
            frames (int): The number of frames.
        """
        # Move to jumppoint
        self.move_to(position1[0], position1[1])
        # Set jumpPostions
        self.otherJumpPos, self.currentJumpPos = position2, position1
        # Frames
        self.frames = frames
        # Activate jumping
        self.jumping = True
