"""
# Oh hey there! You found the source code for the PygameGUI library!
# If you are lost and don't know how to use the library,
# check out the documentation at https://tbf3d.github.io/pygameui/
# Or if you know what you are doing, feel free to look around the code and see how it works!
# Or even contribute to the project!
"""

import pygame
import re

pygame.init()

VERSION = "2.1.0"

class Element:
    """
    Basic element that can be displayed
    """
    def __init__(self,
                 position: tuple[int, int],
                 width: int,
                 height:int,
                 color: tuple[int, int, int] = (255, 255, 255),
                 border_radius: int = 0,
                 centered: bool = False):
        """
        Create a basic element
        :param position: Where the element will be positioned
        :param width: Width of the element rectangle
        :param height: Height of the element rectangle
        :param color: Color of the element
        :param centered: If the element will be centered in the position
        """
        # Basic attributes
        self._rect = pygame.Rect(position, (width, height))
        self._border_radius = border_radius
        self._color = color
        self._display = True
        # Centered attribute, if True, the element will be centered in the position
        self._centered = centered
        if self._centered:
            self._rect.center = position

        # Movement attributes
        self._is_moving = False
        self._loop = False
        self._move_point_index = 0
        # Move points is a list of tuples with the points that the element will move to in order
        self._move_points = []

        # Framerate
        self._framerate = 60

        # Clicked
        self._clicked = False

    """
    Setters
    """

    def set_position(self, position: tuple[int, int]) -> None:
        """
        Set the position of the element
        :param position: tuple[int, int] with the new position
        :return: None
        """
        if self._centered:
            self._rect.center = position
        else:
            self._rect.topleft = position

    def set_framerate(self, framerate: int) -> None:
        """
        Set the framerate of the element
        :param framerate: int with the new framerate
        :return: None
        """
        self._framerate = framerate

    def set_display(self, display: bool) -> None:
        """
        Set if the element will be displayed
        :param display: bool with the new display value
        :return: None
        """
        self._display = display

    def set_color(self, color: tuple[int, int, int]) -> None:
        """
        Set the color of the element
        :param color: tuple[int, int, int] with the new color
        :return: None
        """
        self._color = color

    def set_border_radius(self, border_radius: int) -> None:
        """
        Set the border radius of the element
        :param border_radius: int with the new border radius
        :return: None
        """
        self._border_radius = border_radius

    """
    Getters
    """

    def get_position(self) -> tuple[int, int]:
        """
        Get the position of the element
        :return: tuple[int, int] with the position of the element
        """
        if self._centered:
            return self._rect.center

        return self._rect.topleft

    """
    Toggles
    """

    def toggle_display(self) -> None:
        """
        Toggle the display of the element
        :return: None
        """
        self._display = not self._display

    """
    Movement functions
    """

    def start_move(self) -> None:
        """
        Start the movement of the element
        :return: None
        """
        self._is_moving = True

    def stop_move(self) -> None:
        """
        Stop the movement of the element
        :return: None
        """
        self._is_moving = False

    # TODO - Fix the framerate of the movement so it actually takes the time to move from start to end position
    def flow(self,
             start_position: tuple[int, int],
             end_position: tuple[int, int],
             time: int,
             loop: bool = False) -> None:

        """
        Sets and starts movement of the element
        :param start_position: Where the element will start to move from
        :param end_position: Where the element will move to
        :param time: How much time in ms the element will take to move from start_position to end_position
        :param loop: If the element will loop the movement
        :return: None
        """
        # Calculate the number of frames
        num_frames = time // (1000 // self._framerate)
        # Calculate the distance between the start and end positions
        distance = [end_position[0] - start_position[0], end_position[1] - start_position[1]]
        # Calculate the speed of the element per frame
        speed = [distance[0] / num_frames, distance[1] / num_frames]
        # Create a list of points that the element will move to in order
        self._move_points = [[start_position[0] + speed[0] * i, start_position[1] + speed[1] * i] for i in
                            range(num_frames)]
        self._move_points.append(end_position)

        # If loop is True, the element will move back to the start position after reaching the end position
        if loop:
            self._loop = True
            self._move_point_index = 0
            # Reverse the list of points so the element moves back to the start position
            self._move_points += reversed(self._move_points)

        self.start_move()

    # TODO - Fix the framerate of the jumping so it actually takes the time to jump from start to end position
    def jump(self,
             start_position: tuple[int, int],
             end_position: tuple[int, int],
             time: int,
             loop: bool = False,
             ratio: float = 1) -> None:

        """
        Sets and starts jumping of the element, the element will jump from start_position to end_position
        :param start_position: Where the element will start to jump from
        :param end_position: Where the element will jump to
        :param time: How much time in ms the element will take to jump from start_position to end_position
        :param loop: If the element will continuously jump from start_position to end_position
        :param ratio: Float between 0 and 1. The less the ratio, the less time the element will spend in the start_position
        :return:
        """
        # Calculate the number of frames
        num_frames = time // (1000 // self._framerate)

        # Calculate ratio
        start_pos_share = 0.5*ratio
        ent_pos_share = 1-start_pos_share

        # Create a list of points that the element will move to in order
        self._move_points = [start_position for _ in range(int(num_frames*start_pos_share))]
        self._move_points += [end_position for _ in range(int(num_frames*ent_pos_share))]

        # If loop is True, the element will jump back to the start position after reaching the end position
        if loop:
            self._loop = True
            self._move_point_index = 0
            self._move_points += reversed(self._move_points)

        self.start_move()

    def _update_movement(self) -> None:
        """
        Update the movement of the element
        :return: None
        """
        if not self._is_moving:
            return

        if self._loop:
            point_to_move_to = self._move_points[self._move_point_index]
            self._move_point_index += 1

            if self._move_point_index >= len(self._move_points):
                self._move_point_index = 0

        else:
            point_to_move_to = self._move_points.pop(0)
            if not self._move_points:
                self._is_moving = False

        self.set_position(point_to_move_to)

    """
    Mouse and clicking functions
    """

    def is_hovered(self):
        """
        Returns if the element is hovered.

        Returns:
            bool: True if the element is hovered, False otherwise.
        """
        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self._rect.collidepoint(mouse_pos):
            return True

        return False

    def is_clicked(self, button: int = 1):
        """
        Returns if the element is clicked.
        :param button: The button that will be used to click the element, default is left click
        :return: True if the element is clicked, False otherwise
        """
        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self._rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == button:
                self._clicked = True
                return True

        return False

    def was_clicked(self):
        """
        Returnes true if the element was left clicked and then released
        """
        if self.is_clicked():
            return

        if self._clicked:
            self._clicked = False
            return True

    """
    Basic functions
    """

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the element in the surface
        :param surface: pygame.Surface where the element will be drawn
        :return: None
        """
        if not self._display:
            return

        pygame.draw.rect(surface, self._color, self._rect, border_radius = self._border_radius)

    def update(self, _=None) -> None:
        """
        Update the element
        :return: None
        """
        self._update_movement()

class Text(Element):
    """
    Text element that can be displayed
    """
    def __init__(self,
                 position: tuple[int, int],
                 content: str,
                 color: tuple[int, int, int] = (255, 255, 255),
                 font_size: int = 20,
                 font_family: str = "Arial",
                 width: int = 0,
                 height: int = 0,
                 anti_aliasing: bool = True,
                 centered: bool = False):
        """
        Create a text element
        :param position: Where the text will be positioned
        :param content: The text displayed
        :param color: The text color
        :param font_size: The size of the font
        :param font_family: What font family the text will use
        :param width: Width of the text element, 0 indicates that the width will be the width of the text.
        :param height: Height of the text element, 0 indicates that the height will be the width of the text.
        :param anti_aliasing: If the text will be anti aliased
        :param centered: If the text will be centered in the position
        """
        # Text attributes
        self._content = content
        self._font_size = font_size
        self._font_family = font_family
        self._font = pygame.font.SysFont(self._font_family, self._font_size)
        self._anti_aliasing = anti_aliasing

        # Get the dimensions of the text
        if width and height:
            text_dimensions = (width, height)
        else:
            text_dimensions = self.get_text_rect_dimensions()

        super().__init__(position, width=text_dimensions[0], height=text_dimensions[1], color=color, centered=centered)

        # Render text
        self._text_surface = self._render_text()

    """
    Getters
    """

    def get_text_rect_dimensions(self) -> tuple[int, int]:
        """
        Get the dimensions of the text, width and height
        :return: tuple[int, int] with the width and height of the text
        """
        font = pygame.font.SysFont(self._font_family, self._font_size)
        text_surface = font.render(self._content, True, (255, 255, 255))

        rect = text_surface.get_rect()
        return rect.width, rect.height

    """
    Setters
    """

    def set_content(self, new_content: str) -> None:
        """
        Change the text of the element
        :param new_text: str with the new text
        :return: None
        """
        self._content = new_content
        self._text_surface = self._render_text()

    def set_color(self, new_color: tuple[int, int, int]) -> None:
        """
        Change the color of the text
        :param new_color: tuple[int, int, int] with the new color
        :return: None
        """

        self._color = new_color
        self._text_surface = self._render_text() # Update the text surface with the new color

    def set_font_size(self, new_size: int) -> None:
        """
        Change the size of the font
        :param new_size: int with the new size
        :return: None
        """
        self._font_size = new_size
        self._text_surface = self._render_text()
    
    def set_font_family(self, new_family: str) -> None:
        """
        Change the font family of the text
        :param new_family: str with the new font family
        :return: None
        """
        self._font_family = new_family
        self._text_surface = self._render_text()

    """
    Internal functions
    """

    def _render_text(self) -> pygame.Surface:
        """
        Render the text
        :return: pygame.Surface with the rendered text
'       """

        font = pygame.font.SysFont(self._font_family, self._font_size)
        text_surface = font.render(self._content, self._anti_aliasing, self._color)
        return text_surface
    
    """
    Basic functions
    """
    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the text in the surface
        :param surface: pygame.Surface where the text will be drawn
        :return: None
        """

        if not self._display:
            return

        rect = self._text_surface.get_rect()
        if self._centered:
            rect.center = self._rect.center
        else:
            rect.topleft = self._rect.topleft

        surface.blit(self._text_surface, rect)

class Image(Element):
    """
    Image element that can be displayed
    """
    def __init__(self,
                 position: tuple[int, int],
                 image_path: str,
                 width: int = 0,
                 height: int = 0,
                 scale:int = 1,
                 centered: bool = False):
        """
        Create an image element
        :param position: Where the image will be positioned
        :param image_path: Path to the image file
        :param centered: If the image will be centered in the position
        :param width: Width of the image, 0 indicates that the image will keep its original width
        :param height: Height of the image, 0 indicates that the image will keep its original height
        :param scale: Factor to scale the image by compared to the original size, applies when width and height are not set
        """
        # Image attributes
        self._image = pygame.image.load(image_path)
        self._image_path = image_path
        self._scale = scale
        self._width = width
        self._height = height

        if width and height:
            self._image = pygame.transform.scale(self._image, (width, height)).convert_alpha()
        else:
            self._image = pygame.transform.scale(self._image, (self._image.get_width() * self._scale, self._image.get_height() * self._scale)).convert_alpha()
            self._width = self._image.get_width()
            self._height = self._image.get_height()

        super().__init__(position, self._image.get_width(), self._image.get_height(), centered=centered)



    """
    Setters
    """

    def set_image(self, new_image_path: str) -> None:
        """
        Change the image of the element
        :param new_image_path: str with the new image path
        :return: None
        """
        
        self._image = pygame.image.load(new_image_path)
        self._image = pygame.transform.scale(self._image, (self._width, self._height)).convert_alpha()

    def scale(self, new_scale: int) -> None:
        """
        Change the scale of the image
        :param new_scale: int with the new scale
        :return: None
        """
        self._scale = new_scale
        self._image = pygame.transform.scale(self._load_original_image(), (self._image.get_width() * self._scale, self._image.get_height() * self._scale)).convert_alpha()

    """
    Getters
    """
    
    def get_image(self) -> pygame.Surface:
        """
        Get the image of the element
        :return: pygame.Surface with the image
        """
        return self._image
    
    def get_scale(self) -> int:
        """
        Get the scale of the image
        :return: int with the scale of the image
        """
        return self._scale

    """
    Internal functions
    """

    def _load_original_image(self) -> None:
        """
        Load the original image
        :return: pygame.Surface with the original image
        """
        return pygame.image.load(self._image_path).convert_alpha()

    """
    Basic functions
    """

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the image in the surface
        :param surface: Where the image will be drawn
        :return: None
        """

        if not self._display:
            return

        surface.blit(self._image, self._rect)

class Input(Text):
    """
    Input element that can be displayed
    """
    def __init__(self,
                 position: tuple [int, int],
                 width: int = 200,
                 height: int = 50,
                 passive_text_color: tuple[int, int, int] = (150, 150, 150),
                 active_text_color: tuple[int, int, int] = (255, 255, 255),
                 passive_border_color: tuple[int, int, int] = (100, 100, 100),
                 active_border_color: tuple[int, int, int] = (200, 200, 200),
                 border_radius: int = 0,
                 border_width: int = 2,
                 font_size: int = 20,
                 font_family: str = "Arial",
                 hint: str = "",
                 centered: bool = False):
        """
        Create an input element
        :param position: Where the input will be positioned
        :param width: Width of the input
        :param height: Height of the input
        :param passive_text_color: Color of the text when the input is not active
        :param active_text_color: Color of the text when the input is active
        :param passive_border_color: Color of the border when the input is not active
        :param active_border_color: Color of the border when the input is active
        :param border_radius: Radius of the border
        :param border_width: Width of the border
        :param font_size: Size of the font
        :param font_family: Font family of the text
        :param hint: Hint of the input
        """

        super().__init__(position,
                         content=hint,
                         color=passive_text_color,
                         font_size=font_size,
                         font_family=font_family,
                         width=width,
                         height=height,
                         centered=centered)
        
        # Initialize the pygame scrap module
        # This module is used to copy and paste text from the clipboard
        pygame.scrap.init()
        pygame.scrap.set_mode(pygame.SCRAP_CLIPBOARD)

        # Visual attributes
        self._passive_text_color = passive_text_color
        self._active_text_color = active_text_color
        self._passive_border_color = passive_border_color
        self._active_border_color = active_border_color
        self._border_radius = border_radius
        self._border_width = border_width

        # Text attributes
        self._hint = hint
        self._text = "" # User input text

        # States
        self.active = False

        # Filer
        self._max_length = 0
        self._filter = None
        self._filter_mode_exclude = True

        # Keys that will be ignored from the input
        self._exclude_keys = [pygame.KMOD_SHIFT, pygame.KMOD_CAPS, pygame.K_CAPSLOCK, pygame.K_LSHIFT, pygame.K_RSHIFT]
        # Keys that will exit the input
        self._exit_keys = [pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_TAB, pygame.K_ESCAPE]

        # Cursor
        self._cursor = False
        self._cursor_index = 0

    """
    Getters
    """

    def get_text(self):
        """
        Get the text of the input
        """
        return self._text

    """
    Setters
    """

    def set_max_length(self, max_length: int) -> None:
        """
        Set the maximum length of the input
        :param max_length: int with the maximum length
        """
        self._max_length = max_length

    def set_filter(self, new_filter: str, exclude_mode: bool = True) -> None:
        """
        Set the filter of the input
        :param new_filter: str with the new filter
        :param exclude_mode: If the true, the filter will exclude the characters in the filter, if false, the filter will only allow characters in the filter
        """
        self._filter = new_filter
        self._filter_mode_exclude = exclude_mode

    """
    Internal functions
    """
    def _allow_key(self, key: str):
        """
        Check if the key is allowed by the filter
        :param key: str with the key to be checked
        """
        if self._max_length and len(self._text) >= self._max_length:
            return False

        if not self._filter:
            return True

        if self._filter_mode_exclude:
            if key not in self._filter:
                return True
        else:
            if key in self._filter:
                return True

        return False

    def _handle_keys(self, events: list) -> None:
        """
        Handle the typing of the input
        :param events: list with the events
        """
        for event in events:
            if event.type != pygame.KEYDOWN: # We only want to handle key down events
                continue
            # Handle copy/paste
            if event.key == pygame.K_v and event.mod & pygame.KMOD_CTRL:
                pasted_text = pygame.scrap.get("text/plain;charset=utf-8").decode()
                # Remove all non-printable characters
                pasted_text = re.sub(r'[^\x20-\x7E]+', '', pasted_text)

                for char in pasted_text:
                    if not self._allow_key(char):
                        pasted_text = pasted_text.replace(char, "")
                
                if self._max_length and len(pasted_text) + len(self._text) > self._max_length:
                    pasted_text = pasted_text[:self._max_length - len(self._text)]

                self._text = self._text[:self._cursor_index] + pasted_text + self._text[self._cursor_index:]
                self._cursor_index += len(pasted_text)
                continue
            elif event.key == pygame.K_c and event.mod & pygame.KMOD_CTRL:
                pygame.scrap.put(pygame.SCRAP_TEXT, self._text.encode('utf-8'))
                continue
            elif event.key == pygame.K_x and event.mod & pygame.KMOD_CTRL:
                pygame.scrap.put(pygame.SCRAP_TEXT, self._text.encode('utf-8'))
                self._text = ""
                self._cursor_index = 0
                continue
            elif event.key in self._exit_keys: # Check if the key should exit the input
                self.active = False
            elif event.key in self._exclude_keys: # Check the key should be ignored
                continue
            # Cursor
            elif event.key == pygame.K_RIGHT:
                if self._cursor_index >= len(self._text):
                    continue
                self._cursor_index += 1
            elif event.key == pygame.K_LEFT:
                if self._cursor_index <= 0:
                    continue
                self._cursor_index -= 1
            # Backspace and delete
            elif event.key == pygame.K_BACKSPACE:
                if self._cursor_index == 0:
                    continue

                self._text = self._text[:self._cursor_index-1] + self._text[self._cursor_index:]
                self._cursor_index -= 1
            elif event.key == pygame.K_DELETE:
                if self._cursor_index == len(self._text):
                    continue

                self._text = self._text[:self._cursor_index] + self._text[self._cursor_index+1:]
            # Normal keys
            else:
                if not self._allow_key(event.unicode):
                    continue

                self._text = self._text[:self._cursor_index] + event.unicode + self._text[self._cursor_index:]
                self._cursor_index += 1

        self.set_content(self._text)

    def _draw_cursor(self, surface: pygame.Surface):
        """
        Draw the cursor
        :param surface: pygame.Surface where the cursor will be drawn
        """
        if not self._cursor:
            return

        font = pygame.font.SysFont(self._font_family, self._font_size)
        cursor_surface = font.render("|", True, self._active_text_color)

        text_to_cursor = Text(self.get_position(), self._text[:self._cursor_index], self._active_text_color,
                              self._font_size, self._font_family, self._centered)

        cursor_position = (self._rect.x + text_to_cursor._rect.width, self._rect.y)

        if self._centered:
            print((self._rect.width - self.get_text_rect_dimensions()[0])//2)
            cursor_position = (self._rect.x + (self._rect.width - self.get_text_rect_dimensions()[0]), self._rect.centery - text_to_cursor._rect.height//2)

        surface.blit(cursor_surface, cursor_position)

    """
    Basic functions
    """

    def draw(self, surface: pygame.surface):
        """
        Draw the input and the cursor
        :param surface: pygame.Surface where the input will be drawn
        """
        super().draw(surface)

        if self.active:
            self._draw_cursor(surface)
            pygame.draw.rect(surface, self._active_border_color, self._rect, self._border_width, border_radius=self._border_radius)
        else:
            pygame.draw.rect(surface, self._passive_border_color, self._rect, self._border_width, border_radius=self._border_radius)

    def update(self, events: list) -> None:
        """
        Update the input
        :param events: list with the events
        """
        super().update()

        # Check if the input was clicked
        if self.was_clicked():
            self.active = True
        # Check if the input was clicked outside, if so, deactivate it
        elif self.active:
            self._handle_keys(events)
            if pygame.mouse.get_pressed()[0] == 1 and not self.is_clicked():
                self.active = False
                if self._text != "":
                    self.set_content(self._text)
                else:
                    self.set_content(self._hint)

class Button(Element):
    """
    Button element that can be displayed
    """
    def __init__(self,
                 position: tuple[int, int],
                 width: int = 200,
                 height: int = 50,
                 border_radius: int = 10,
                 content: str = "Click me.",
                 color: tuple[int, int, int] = (255, 255, 255),
                 hover_color: tuple[int, int, int] = (200, 200, 200),
                 click_color: tuple[int, int, int] = (150, 150, 150),
                 text_color: tuple[int, int, int] = (100, 100, 100),
                 text_hover_color: tuple[int, int, int] = (0, 0, 0),
                 text_click_color: tuple[int, int, int] = (0, 0, 0),
                 font_size: int = 20,
                 font_family: str = "Arial",
                 centered: bool = False):
        """
        Create a button element
        :param position: Where the button will be positioned
        :param width: Width of the button
        :param height: Height of the button
        :param content: Text of the button
        :param color: Color of the button
        :param hover_color: Color of the button when hovered
        :param click_color: Color of the button when clicked
        :param font_size: Size of the font
        :param font_family: Font family of the text
        :param centered: If the button will be centered in the position
        """

        super().__init__(position, width, height, color, border_radius, centered)

        self._text_object = Text(position, content, text_color, font_size, font_family, width, height, centered)

        # Button attributes
        self._text = content
        self._color = color
        self._hover_color = hover_color
        self._click_color = click_color
        self._border_radius = border_radius

        # Text attributes
        self._text_color = text_color
        self._text_hover_color = text_hover_color
        self._text_click_color = text_click_color

        # States
        self._hovered = False
        self._clicked = False

    """
    Basic functions
    """
    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the button
        :param surface: pygame.Surface where the button will be drawn
        """
        if not self._display:
            return

        if self._clicked:
            pygame.draw.rect(surface, self._click_color, self._rect, border_radius=self._border_radius)
            self._text_object.set_color(self._text_click_color)
        elif self._hovered:
            pygame.draw.rect(surface, self._hover_color, self._rect, border_radius=self._border_radius)
            self._text_object.set_color(self._text_hover_color)
        else:
            pygame.draw.rect(surface, self._color, self._rect, border_radius=self._border_radius)
            self._text_object.set_color(self._text_color)

        self._text_object.draw(surface)

    def update(self,  _=None) -> None:
        """
        Update the button,
        Collects the events and updates the button
        """
        self._text_object.update()

        # Check if the button is hovered
        self._hovered = self.is_hovered()