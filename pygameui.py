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

VERSION = "2.2.1"

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
                 border_color: tuple[int, int, int] = None,
                 border_width: int = 2,
                 centered: bool = False):
        """
        Create a basic element
        :param position: Where the element will be positioned
        :param width: Width of the element rectangle
        :param height: Height of the element rectangle
        :param color: Color of the element
        :param border_radius: Radius of the element corners
        :param border_color: Color of the element border, if None, the border will not be drawn
        :param border_width: Width of the element border
        :param centered: If the element will be centered in the position
        """
        # Basic attributes
        self._rect = pygame.Rect(position, (width, height))
        self._border_radius = border_radius
        self._border_color = border_color # If None, the border will not be drawn
        self._border_width = border_width # Width of the border
        self._color = color
        self._display = True
        # Centered attribute, if True, the element will be centered in the position
        self._centered = centered
        if self._centered:
            self._rect.center = position

        # Movement attributes
        self._is_being_animated = False
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

    def set_border_radius(self, radius: int) -> None:
        """
        Set the border radius of the element
        :param border_radius: int with the new border radius
        :return: None
        """
        self._border_radius = radius

    def set_animate(self, state: bool) -> None:
        """
        Set if the element will move, be animated or not
        :param move: bool with the new move value
        :return: None
        """
        self._is_being_animated = state

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

    def get_display(self) -> bool:
        """
        Get if the element will be displayed
        :return: bool with the display value
        """
        return self._display

    def get_animation_state(self) -> bool:
        """
        Get if the element is being animated
        :return: bool with the animation state
        """
        return self._is_being_animated

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
    Movement methods
    """
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

        self.set_animate(True)

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

        self.set_animate(True)

    """
    Internal methods
    """

    def _update_movement(self) -> None:
        """
        Update the movement of the element
        :return: None
        """
        if not self._is_being_animated:
            return

        if self._loop:
            point_to_move_to = self._move_points[self._move_point_index]
            self._move_point_index += 1

            if self._move_point_index >= len(self._move_points):
                self._move_point_index = 0

        else:
            point_to_move_to = self._move_points.pop(0)
            if not self._move_points:
                self._is_being_animated = False

        self.set_position(point_to_move_to)

    """
    Mouse and clicking methods
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
    Basic methods
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

        if self._border_color:
            pygame.draw.rect(surface, self._border_color, self._rect, width=self._border_width, border_radius=self._border_radius)

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
            text_dimensions = self._get_text_rect_dimensions()

        super().__init__(position, width=text_dimensions[0], height=text_dimensions[1], color=color, centered=centered)

        # Render text
        self._text_surface = self._render_text()

    """
    Setters
    """

    def set_content(self, content: str) -> None:
        """
        Change the text of the element
        :param content: str with the new text
        :return: None
        """
        self._content = content
        self._text_surface = self._render_text()

    def set_color(self, color: tuple[int, int, int]) -> None:
        """
        Change the color of the text
        :param color: tuple[int, int, int] with the new color
        :return: None
        """

        self._color = color
        self._text_surface = self._render_text() # Update the text surface with the new color

    def set_font_size(self, font_size: int) -> None:
        """
        Change the size of the font
        :param font_size: int with the new size
        :return: None
        """
        self._font_size = font_size
        self._text_surface = self._render_text()
    
    def set_font_family(self, font_family: str) -> None:
        """
        Change the font family of the text
        :param font_family: str with the new font family
        :return: None
        """
        self._font_family = font_family
        self._text_surface = self._render_text()

        """
    Getters
    """

    """
    Getters
    """

    def get_content(self) -> str:
        """
        Get the content of the text
        :return: str with the content of the text
        """
        return self._content

    """
    Internal methods
    """

    def _get_text_rect_dimensions(self) -> tuple[int, int]:
        """
        Get the dimensions of the text, width and height
        :return: tuple[int, int] with the width and height of the text
        """
        font = pygame.font.SysFont(self._font_family, self._font_size)
        text_surface = font.render(self._content, True, (255, 255, 255))

        rect = text_surface.get_rect()
        return rect.width, rect.height

    def _render_text(self) -> pygame.Surface:
        """
        Render the text
        :return: pygame.Surface with the rendered text
'       """

        font = pygame.font.SysFont(self._font_family, self._font_size)
        text_surface = font.render(self._content, self._anti_aliasing, self._color)
        return text_surface
    
    """
    Basic methods
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

    def set_image(self, image_path: str) -> None:
        """
        Change the image of the element
        :param image_path: str with the new image path
        :return: None
        """
        
        self._image = pygame.image.load(image_path)
        self._image = pygame.transform.scale(self._image, (self._width, self._height)).convert_alpha()

    def scale(self, scale: int) -> None:
        """
        Change the scale of the image
        :param scale: int with the new scale
        :return: None
        """
        self._scale = scale
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
    Internal methods
    """

    def _load_original_image(self) -> None:
        """
        Load the original image
        :return: pygame.Surface with the original image
        """
        return pygame.image.load(self._image_path).convert_alpha()

    """
    Basic methods
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
    Setters
    """

    def set_max_length(self, max_length: int) -> None:
        """
        Set the maximum length of the input
        :param max_length: int with the maximum length
        """
        self._max_length = max_length

    def set_filter(self, filter: str, only_allow_filter: bool = False) -> None:
        """
        Set the filter of the input
        :param filter: str with the new filter
        :param only_allow_filter: If true, the filter will exclude the characters in the filter, if false, the filter will only allow characters in the filter
        """
        self._filter = filter
        self._filter_mode_exclude = only_allow_filter

    def set_hint(self, hint: str) -> None:
        """
        Set the hint of the input
        :param hint: str with the new hint
        """
        self._hint = hint
    
    def set_value(self, value: str) -> None:
        """
        Set the text of the input
        :param value: str with the new text
        """
        self._text = value
        self.set_content(self._text)

        

    """
    Getters
    """

    def get_value(self):
        """
        Get the text of the input
        """
        return self._text

    """
    Internal methods
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
            cursor_position = (self._rect.x + (self._rect.width - self._get_text_rect_dimensions()[0]), self._rect.centery - text_to_cursor._rect.height//2)

        surface.blit(cursor_surface, cursor_position)

    """
    Basic methods
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
                 border_color: tuple[int, int, int] = None,
                 border_width: int = 2,
                 label: str = "Click me.",
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
        :param label: Text of the button
        :param color: Color of the button
        :param hover_color: Color of the button when hovered
        :param click_color: Color of the button when clicked
        :param font_size: Size of the font
        :param font_family: Font family of the text
        :param centered: If the button will be centered in the position
        """

        super().__init__(position, width, height, color, border_radius, border_color, border_width, centered)

        self._text_object = Text(
            position=self._rect.center,
            content=label,
            color=text_color,
            font_size=font_size,
            font_family=font_family,
            width=width,
            height=height,
            centered=True # Center the text in the button
        )

        # Button attributes
        self._label = label
        self._color = color
        self._hover_color = hover_color
        self._click_color = click_color

        # Border attributes
        self._border_color = border_color # Color of the border, set to None to disable the border
        self._border_width = border_width
        self._border_radius = border_radius

        # Text attributes
        self._text_color = text_color
        self._text_hover_color = text_hover_color
        self._text_click_color = text_click_color

        # States
        self._hovered = False
        self._clicked = False

    """
    Setters
    """
    def set_label(self, label: str) -> None:
        """
        Set the text of the button
        :param label: str with the new text
        """
        self._label = label
        self._text_object.set_content(label)

    def set_color(self, color: tuple[int, int, int]) -> None:
        """
        Set the background color of the button
        :param color: tuple[int, int, int] with the new color
        """
        self._color = color

    def set_hover_color(self, color: tuple[int, int, int]) -> None:
        """
        Set the hover color of the button
        :param color: tuple[int, int, int]
        """
        self._hover_color = color
    
    def set_click_color(self, color: tuple[int, int, int]) -> None:
        """
        Set the click color of the button
        :param color: tuple[int, int, int]
        """
        self._click_color = color
    
    def set_text_color(self, color: tuple[int, int, int]) -> None:
        """
        Set the text color of the button
        :param color: tuple[int, int, int]
        """
        self._text_color = color
        self._text_object.set_color(color)
    
    def set_text_hover_color(self, color: tuple[int, int, int]) -> None:
        """
        Set the hover color of the text
        :param color: tuple[int, int, int]
        """
        self._text_hover_color = color

    def set_text_click_color(self, color: tuple[int, int, int]) -> None:
        """
        Set the click color of the text
        :param color: tuple[int, int, int]
        """
        self._text_click_color = color

    """
    Basic methods
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

        if self._border_color:
            pygame.draw.rect(surface, self._border_color, self._rect, width=self._border_width, border_radius=self._border_radius)

    def update(self,  _=None) -> None:
        """
        Update the button,
        Collects the events and updates the button
        """
        self._text_object.update()

        # Check if the button is hovered
        self._hovered = self.is_hovered()

class ProgressBar(Element):
    """
    Progress element that can be displayed
    """
    def __init__(self,
                 position: tuple[int, int],
                 width: int = 200,
                 height: int = 50,
                 progrss: int = 0,
                 max_progress: int = 100,
                 min_progress: int = 0,
                 color: tuple[int, int, int] = (150, 255, 150),
                 background_color: tuple[int, int, int] = (100, 100, 100),
                 border_radius: int = 0,
                 border_color: tuple[int, int, int] = (200, 200, 200),
                 border_width: int = 2,
                 centered: bool = False):
        """
        Create a progress element
        :param position: Where the progress will be positioned
        :param width: Width of the progress
        :param height: Height of the progress
        :param progress: Current progress amount
        :param max_progress: Maximum progress amount
        :param min_progress: Minimum progress amount
        :param color: Color of the progress
        :param border_radius: Radius of the border
        :param background_color: Color of the background, set to None to disable the background
        :param border_color: Color of the border, set to None to disable the border
        :param border_width: Width of the border
        :param centered: If the progress will be centered in the position
        """
        super().__init__(position, width, height, color, border_radius, centered)

        # Progress attributes
        self._progress = progrss
        self._max_progress = max_progress
        self._min_progress = min_progress

        # Progress bar attributes
        self._progress_bar = pygame.Rect(self._rect.x, self._rect.y, 0, self._rect.height)
        self._progress_bar_color = color
        self._progress_bar_width = width
        self._progress_bar_height = height
        self._progress_bar_centered = centered

        # Border attributes
        self._border_color = border_color
        self._border_radius = border_radius
        self._border_width = border_width

        # Background attributes
        self._background_color = background_color

    """
    Setters 
    """

    def set_progress(self, progress: int) -> None:
        """
        Set the progress amount
        :param progress: int with the new progress amount
        """
        self._progress = progress

        if self._progress > self._max_progress:
            self._progress = self._max_progress
        elif self._progress < self._min_progress:
            self._progress = self._min_progress
        
        self._update_progress_bar()
    
    def set_max_progress(self, max_progress: int) -> None:
        """
        Set the maximum progress amount
        :param max_progress: int with the new maximum progress amount
        """
        self._max_progress = max_progress
        
        self._update_progress_bar()

    def set_min_progress(self, min_progress: int) -> None:
        """
        Set the minimum progress amount
        :param min_progress: int with the new minimum progress amount
        """
        self._min_progress = min_progress
        # Update the progress bar width
        if self._progress < self._min_progress:
            self._progress = self._min_progress
        
        self._update_progress_bar()

    def change_progress(self, amount: int) -> None:
        """
        Change the progress amount
        :param amount: int with the amount to change the progress by
        :return: None
        """
        self._progress += amount

        self.set_progress(self._progress)

    """
    Getters
    """
    def get_progress(self) -> int:
        """
        Get the progress amount
        :return: int with the progress amount
        """
        return self._progress

    """
    Internal methods
    """
    
    def _update_progress_bar(self) -> None:
        """
        Update the progress bar width
        :return: None
        """
        self._progress_bar.width = int(self._rect.width * (self._progress / self._max_progress))


    """
    Basic methods
    """

    def draw(self, surface: pygame.Surface) -> None:
        """"
        Draw the progress bar
        :param surface: pygame.Surface where the progress bar will be drawn
        :return: None
        """
        if not self._display:
            return

        # Draw the background
        if self._background_color:
            pygame.draw.rect(surface, self._background_color, self._rect, border_radius=self._border_radius)
        # Draw the progress bar
        pygame.draw.rect(surface, self._progress_bar_color, self._progress_bar, border_radius=self._border_radius)
        # Draw the border
        if self._border_color:
            pygame.draw.rect(surface, self._border_color, self._rect, self._border_width, border_radius=self._border_radius)
    
    def update(self, _=None) -> None:
        """
        Update the progress bar
        :return: None
        """
        super().update()
        self._update_progress_bar()
        
class DropdownMenu(Element):
    def __init__(self, 
                 position: tuple[int, int],
                 options: list[str], 
                 width: int = 200, 
                 height: int = 50,
                 max_elements_per_column: int = 5,
                 wrap_reverse: bool = False,
                 color = (255, 255, 255),
                 hover_color = (200, 200, 200),
                 click_color = (150, 150, 150),
                 text_color = (0, 0, 0),
                 text_hover_color = (0, 0, 0),
                 text_click_color = (0, 0, 0),
                 selected_option_color = (200, 200, 200),
                 selected_option_hover_color = (150, 150, 150),
                 selected_option_click_color = (100, 100, 100),
                 selected_option_text_color = (0, 0, 0),
                 selected_option_text_hover_color = (0, 0, 0),
                 selected_option_text_click_color = (0, 0, 0),
                 border_radius = 0, 
                 centered = False):
        
        super().__init__(position, width, height, color, border_radius, centered)

        # Visuals
        self._color = color
        self._hover_color = hover_color
        self._click_color = click_color
        self._text_color = text_color
        self._text_color_hover = text_hover_color
        self._text_color_click = text_click_color

        self._selected_option_color = selected_option_color
        self._selected_option_text_color = selected_option_text_color
        self._selected_option_hover_color = selected_option_hover_color
        self._selected_option_click_color = selected_option_click_color
        self._selected_option_text_hover_color = selected_option_text_hover_color
        self._selected_option_text_click_color = selected_option_text_click_color

        self._border_radius = border_radius

        # Drop down menu attributes
        self._options = options
        self._selected_option_index = 0
        self._wrap_direction = -1 if wrap_reverse else 1
        self._max_elements_per_column = max_elements_per_column
        self._options_buttons = self._generate_options_buttons()
        self._selected_button = self._generate_selected_button()
        self._is_open = False

    """
    Setters
    """

    def set_options(self, options: list[str]) -> None:
        """
        Set the options of the drop down menu
        :param options: list[str] with the new options
        :return: None
        """
        self._options = options
        self._options_buttons = self._generate_options_buttons()
        self._selected_button = self._generate_selected_button()
        self._selected_option_index = 0

    def set_selected_option(self, option: str) -> None:
        """
        Set the selected option of the drop down menu
        :param selected_option: str with the new selected option
        :return: None
        """
        if option not in self._options:
            raise ValueError("Selected option is not in the options list")
        
        self._selected_option_index = self._options.index(option)
        self._selected_button = self._generate_selected_button()
    
    def set_selected_index(self, index: int) -> None:
        """
        Set the selected option of the drop down menu
        :param selected_option_index: int with the new selected option index
        :return: None
        """
        if index < 0 or index >= len(self._options):
            raise ValueError("Selected option index is out of range")
        
        self._selected_option_index = index
        self._selected_button = self._generate_selected_button()

    """
    Getters
    """
    def get_selected_option(self) -> str:
        """
        Get the selected option
        :return: str with the selected option
        """
        return self._options[self._selected_option_index]

    def get_selected_index(self) -> int:
        """
        Get the selected option index
        :return: int with the selected option index
        """
        return self._selected_option_index
    
    def get_options(self) -> list[str]:
        """
        Get the options of the drop down menu
        :return: list[str] with the options
        """
        return self._options

    """
    Internal methods
    """

    def _generate_selected_button(self) -> Button:
        """
        Return a button with the selected option
        :return: Button with the selected option
        """
        selected_button = Button((self._rect.x, self._rect.y), 
                                 self._rect.width, self._rect.height, 
                                 label=self._options[self._selected_option_index], 
                                 color=self._selected_option_color, 
                                 hover_color=self._selected_option_hover_color, 
                                 click_color=self._selected_option_click_color, 
                                 text_color=self._selected_option_text_color,
                                 text_click_color=self._selected_option_text_click_color,
                                 text_hover_color=self._selected_option_text_hover_color,
                                 border_radius=self._border_radius)

        return selected_button
    
    def _generate_options_buttons(self) -> list[Button]:
        """
        Generate the buttons for the options
        :return: list of buttons with the options
        """
        options_buttons = []

        for index, lable in enumerate(self._options):
            offset_x = self._rect.width * (index // self._max_elements_per_column) * self._wrap_direction
            offset_y = self._rect.height * ((index - index // self._max_elements_per_column * self._max_elements_per_column) + 1)
            x_cordinate = self._rect.x + offset_x
            y_cordinate = self._rect.y + offset_y
                
            button = Button((x_cordinate, y_cordinate), 
                            self._rect.width, self._rect.height, 
                            label=lable,
                            color=self._color,
                            hover_color=self._hover_color,
                            click_color=self._click_color,
                            text_color=self._text_color,
                            text_click_color=self._text_color_click,
                            text_hover_color=self._text_color_hover,
                            border_radius=self._border_radius)

            options_buttons.append(button)

        return options_buttons
    
    """
    Basic methods
    """
    
    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the drop down menu
        :param surface: pygame.Surface where the drop down menu will be drawn
        :return: None
        """

        if not self._display:
            return

        self._selected_button.draw(surface)

        if self._is_open:
            for button in self._options_buttons:
                button.draw(surface)

    def update(self, _=None) -> None:
        """
        Update the drop down menu
        :return: None
        """
        super().update()

        # If the menu is being animated, update the buttons so they are in the right position
        if self._is_being_animated:
            self._options_buttons = self._generate_options_buttons()
            self._selected_button = self._generate_selected_button()

        # Update the buttons
        self._selected_button.update()
        for button in self._options_buttons:
            button.update()

        if self._is_open:
            # Check if any of the buttons were clicked, if so, set the selected option to the clicked button
            for button in self._options_buttons:
                if button.was_clicked():
                    self._selected_option_index = self._options_buttons.index(button)
                    self._selected_button = self._generate_selected_button()
                    # Close the menu after selecting an option
                    self._is_open = False
                    return
            
            if self._selected_button.was_clicked():
                self._is_open = False
                return

            # Check if the menu was clicked outside, if so, close it
            if pygame.mouse.get_pressed()[0] == 1 and not self.is_clicked():
                # Check that we haven't clicked any other button from the menu
                for button in self._options_buttons:
                    if button.is_hovered():
                        return
                    
                self._is_open = False
                return

        # Check if the menu was clicked, if so, open it
        if self._selected_button.was_clicked():
            self._is_open = True

class Table(Element):
    def __init__(self, 
                 position,
                 content: list[list[str]], 
                 width = 200, 
                 height = 50, 
                 color = (255, 255, 255),
                 hover_color = (200, 200, 200),
                 text_color = (0, 0, 0),
                 border_color = (200, 200, 200),
                 border_width = 2,
                 border_radius = 0, 
                 centered = False):
        super().__init__(position, width, height, color, border_radius, centered)

        # Table attributes
        self._content = content
        self._columns = len(content[0])
        self._rows = len(content)
        self._cell_width = width // self._columns
        self._cell_height = height // self._rows
        self._cell_color = color
        self._cell_color_hover = hover_color

        self._text_color = text_color

        self._border_color = border_color
        self._border_width = border_width

        # Drawing
        self._items = self._generate_table()

    """
    Setters
    """
    def set_content(self, content: list[list[str]]) -> None:
        """
        Set the content of the table
        :param content: list[list[str]] with the new content
        :return: None
        """
        self._content = content
        self._items = self._generate_table()
        self._columns = len(content[0])
        self._rows = len(content)

    """
    Internal methods
    """

    def _generate_table(self) -> None:
        """
        Generate the table
        :return: None
        """
        items_to_draw = []

        self._cell_width = self._rect.width // self._columns
        self._cell_height = self._rect.height // self._rows

        for row in range(self._rows):
            for column in range(self._columns):
                x = self._rect.x + column * self._cell_width
                y = self._rect.y + row * self._cell_height

                # Draw the text in the cell
                cell = Button((x, y), label=self._content[row][column], width=self._cell_width, height=self._cell_height, color=self._cell_color, border_radius=self._border_radius, border_color=self._border_color, border_width=self._border_width, text_color=self._text_color, hover_color=self._cell_color_hover)
                items_to_draw.append(cell)

        return items_to_draw

    """
    Basic methods
    """

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the table
        :param surface: pygame.Surface where the table will be drawn
        :return: None
        """
        if not self._display:
            return

        for item in self._items:
            item.draw(surface)
            item.update()
    