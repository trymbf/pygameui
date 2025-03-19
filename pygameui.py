"""
# Oh hey there! You found the source code for the PygameGUI library!
# If you are lost and don't know how to use the library,
# check out the documentation at https://tbf3d.github.io/pygameui/
# Or if you know what you are doing, feel free to look around the code and see how it works!
# Or even contribute to the project!
"""

import pygame

pygame.init()

VERSION = 2.00

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
        self.rect = pygame.Rect(position, (width, height))
        self.border_radius = border_radius
        self.color = color
        self.display = True
        # Centered attribute, if True, the element will be centered in the position
        self.centered = centered
        if self.centered:
            self.rect.center = position

        # Movement attributes
        self.is_moving = False
        self.loop = False
        self.move_point_index = 0
        # Move points is a list of tuples with the points that the element will move to in order
        self.move_points = []

        # Framerate
        self.framerate = 60

        # Clicked
        self.clicked = False


    """
    Setters
    """

    def set_position(self, position: tuple[int, int]) -> None:
        """
        Set the position of the element
        :param position: tuple[int, int] with the new position
        :return: None
        """
        if self.centered:
            self.rect.center = position
        else:
            self.rect.topleft = position

    def set_framerate(self, framerate: int) -> None:
        """
        Set the framerate of the element
        :param framerate: int with the new framerate
        :return: None
        """
        self.framerate = framerate

    def set_display(self, display: bool) -> None:
        """
        Set if the element will be displayed
        :param display: bool with the new display value
        :return: None
        """
        self.display = display

    """
    Getters
    """

    def get_position(self) -> tuple[int, int]:
        """
        Get the position of the element
        :return: tuple[int, int] with the position of the element
        """
        if self.centered:
            return self.rect.center

        return self.rect.topleft

    """
    Toggles
    """

    def toggle_display(self) -> None:
        """
        Toggle the display of the element
        :return: None
        """
        self.display = not self.display

    """
    Movement functions
    """

    def start_move(self) -> None:
        """
        Start the movement of the element
        :return: None
        """
        self.is_moving = True

    def stop_move(self) -> None:
        """
        Stop the movement of the element
        :return: None
        """
        self.is_moving = False

    # TODO - Fix the framerate of the movement so it actually takes the time to move from start to end position
    def flow(self,
             start_position: [int, int],
             end_position: [int, int],
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
        num_frames = time // (1000 // self.framerate)
        # Calculate the distance between the start and end positions
        distance = [end_position[0] - start_position[0], end_position[1] - start_position[1]]
        # Calculate the speed of the element per frame
        speed = [distance[0] / num_frames, distance[1] / num_frames]
        # Create a list of points that the element will move to in order
        self.move_points = [[start_position[0] + speed[0] * i, start_position[1] + speed[1] * i] for i in
                            range(num_frames)]
        self.move_points.append(end_position)

        # If loop is True, the element will move back to the start position after reaching the end position
        if loop:
            self.loop = True
            self.move_point_index = 0
            # Reverse the list of points so the element moves back to the start position
            self.move_points += reversed(self.move_points)

        self.start_move()

    # TODO - Fix the framerate of the jumping so it actually takes the time to jump from start to end position
    def jump(self,
             start_position: [int, int],
             end_position: [int, int],
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
        num_frames = time // (1000 // self.framerate)

        # Calculate ratio
        start_pos_share = 0.5*ratio
        ent_pos_share = 1-start_pos_share

        # Create a list of points that the element will move to in order
        self.move_points = [start_position for _ in range(int(num_frames*start_pos_share))]
        self.move_points += [end_position for _ in range(int(num_frames*ent_pos_share))]

        # If loop is True, the element will jump back to the start position after reaching the end position
        if loop:
            self.loop = True
            self.move_point_index = 0
            self.move_points += reversed(self.move_points)

        self.start_move()

    def update_movement(self) -> None:
        """
        Update the movement of the element
        :return: None
        """
        if not self.is_moving:
            return

        if self.loop:
            point_to_move_to = self.move_points[self.move_point_index]
            self.move_point_index += 1

            if self.move_point_index >= len(self.move_points):
                self.move_point_index = 0

        else:
            point_to_move_to = self.move_points.pop(0)
            if not self.move_points:
                self.is_moving = False

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
        if self.rect.collidepoint(mouse_pos):
            return True

        return False

    def is_clicked(self):
        """
        Returns if the element is clicked.
        """
        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:  # == 1 is left click
                self.clicked = True
                return True

        return False

    def was_clicked(self):
        """
        Returnes true if the element was clicked and then released
        """
        if self.is_clicked():
            return

        if self.clicked:
            self.clicked = False
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
        if not self.display:
            return

        pygame.draw.rect(surface, self.color, self.rect, border_radius = self.border_radius)

    def update(self) -> None:
        """
        Update the element
        :return: None
        """
        self.update_movement()

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
                 centered: bool = False):
        """
        Create a text element
        :param position: Where the text will be positioned
        :param content: The text displayed
        :param color: The text color
        :param centered: If the text will be centered in the position
        :param font_size: The size of the font
        :param font_family: What font family the text will use
        :param width: Width of the text element, 0 indicates that the width will be the width of the text.
        :param height: Height of the text element, 0 indicates that the height will be the width of the text.
        """
        # Text attributes
        self.content = content
        self.font_size = font_size
        self.font_family = font_family
        self.font = pygame.font.SysFont(self.font_family, self.font_size)

        # Get the dimensions of the text
        if width != 0 and height != 0:
            text_dimensions = (width, height)
        else:
            text_dimensions = self.get_text_rect_dimensions()

        super().__init__(position, width=text_dimensions[0], height=text_dimensions[1], color=color, centered=centered)

        # Render text
        self.text_surface = self.render_text()

    def get_text_rect_dimensions(self) -> tuple[int, int]:
        """
        Get the dimensions of the text, width and height
        :return: tuple[int, int] with the width and height of the text
        """
        font = pygame.font.SysFont(self.font_family, self.font_size)
        text_surface = font.render(self.content, True, (255, 255, 255))

        rect = text_surface.get_rect()
        return rect.width, rect.height

    def render_text(self) -> pygame.Surface:
        """
        Render the text
        :return: pygame.Surface with the rendered text
'       """

        font = pygame.font.SysFont(self.font_family, self.font_size)
        text_surface = font.render(self.content, True, self.color)
        return text_surface

    def change_text(self, new_text: str) -> None:
        """
        Change the text of the element
        :param new_text: str with the new text
        :return: None
        """
        self.content = new_text
        self.text_surface = self.render_text()

    def change_text_color(self, new_color: tuple[int, int, int]) -> None:
        """
        Change the color of the text
        :param new_color: tuple[int, int, int] with the new color
        :return: None
        """
        self.color = new_color
        self.text_surface = self.render_text()

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the text in the surface
        :param surface: pygame.Surface where the text will be drawn
        :return: None
        """

        if not self.display:
            return

        rect = self.text_surface.get_rect()
        if self.centered:
            rect.center = self.rect.center
        else:
            rect.topleft = self.rect.topleft

        surface.blit(self.text_surface, rect)

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
        self.image = pygame.image.load(image_path)
        self.scale = scale

        if width and height:
            self.image = pygame.transform.scale(self.image, (width, height)).convert_alpha()
        else:
            self.image = pygame.transform.scale(self.image, (self.image.get_width() * self.scale, self.image.get_height() * self.scale)).convert_alpha()

        super().__init__(position, self.image.get_width(), self.image.get_height(), centered=centered)

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the image in the surface
        :param surface: Where the image will be drawn
        :return: None
        """

        if not self.display:
            return

        surface.blit(self.image, self.rect)

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

        # Visual attributes
        self.passive_text_color = passive_text_color
        self.active_text_color = active_text_color
        self.passive_border_color = passive_border_color
        self.active_border_color = active_border_color
        self.border_radius = border_radius
        self.border_width = border_width

        # Text attributes
        self.hint = hint
        self.text = ""

        # States
        self.active = False

        # Filer
        self.filter = None
        self.filter_mode_exclude = True

        # Keys
        self.exclude_keys = [pygame.KMOD_SHIFT, pygame.KMOD_CAPS, pygame.K_CAPSLOCK, pygame.K_LSHIFT, pygame.K_RSHIFT]
        self.exit_keys = [pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_TAB, pygame.K_ESCAPE]

        # Cursor
        self.cursor = False
        self.cursor_index = 0

    """
    Getters
    """

    def get_text(self):
        """
        Get the text of the input
        """
        return self.text

    """
    Filter
    """

    def set_filter(self, new_filter: str, exclude_mode: bool = True) -> None:
        """
        Set the filter of the input
        :param new_filter: str with the new filter
        :param exclude_mode: If the true, the filter will exclude the characters in the filter, if false, the filter will only allow characters in the filter
        """
        self.filter = new_filter
        self.filter_mode_exclude = exclude_mode

    def allow_key(self, key: str):
        """
        Check if the key is allowed by the filter
        :param key: str with the key to be checked
        """
        if not self.filter:
            return True

        if self.filter_mode_exclude:
            if key not in self.filter:
                return True
        else:
            if key in self.filter:
                return True

        return False

    """
    Typing
    """
    def handle_keys(self, events: list) -> None:
        """
        Handle the typing of the input
        :param events: list with the events
        """
        for event in events:
            if event.type != pygame.KEYDOWN:
                continue
            elif event.key in self.exit_keys:
                self.active = False
            elif event.key in self.exclude_keys:
                continue
            elif event.key == pygame.K_RIGHT:
                if self.cursor_index >= len(self.text):
                    continue
                self.cursor_index += 1
            elif event.key == pygame.K_LEFT:
                if self.cursor_index <= 0:
                    continue
                self.cursor_index -= 1
            elif event.key == pygame.K_BACKSPACE:
                if self.cursor_index == 0:
                    continue

                self.text = self.text[:self.cursor_index-1] + self.text[self.cursor_index:]
                self.cursor_index -= 1
            elif event.key == pygame.K_DELETE:
                if self.cursor_index == len(self.text):
                    continue

                self.text = self.text[:self.cursor_index] + self.text[self.cursor_index+1:]
            else:
                if not self.allow_key(event.unicode):
                    continue

                self.text = self.text[:self.cursor_index] + event.unicode + self.text[self.cursor_index:]
                self.cursor_index += 1

        self.change_text(self.text)

    def draw_cursor(self, surface: pygame.Surface):
        """
        Draw the cursor
        :param surface: pygame.Surface where the cursor will be drawn
        """
        if not self.cursor:
            return

        font = pygame.font.SysFont(self.font_family, self.font_size)
        cursor_surface = font.render("|", True, self.active_text_color)

        text_to_cursor = Text(self.get_position(), self.text[:self.cursor_index], self.active_text_color,
                              self.font_size, self.font_family, self.centered)

        cursor_position = (self.rect.x + text_to_cursor.rect.width, self.rect.y)

        if self.centered:
            print((self.rect.width - self.get_text_rect_dimensions()[0])//2)
            cursor_position = (self.rect.x + (self.rect.width - self.get_text_rect_dimensions()[0]), self.rect.centery - text_to_cursor.rect.height//2)

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
            self.draw_cursor(surface)
            pygame.draw.rect(surface, self.active_border_color, self.rect, self.border_width, border_radius=self.border_radius)
        else:
            pygame.draw.rect(surface, self.passive_border_color, self.rect, self.border_width, border_radius=self.border_radius)

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
            self.handle_keys(events)
            if pygame.mouse.get_pressed()[0] == 1 and not self.is_clicked():
                self.active = False
                if self.text != "":
                    self.change_text(self.text)
                else:
                    self.change_text(self.hint)

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

        self.text_object = Text(position, content, text_color, font_size, font_family, width, height, centered)

        # Button attributes
        self.text = content
        self.color = color
        self.hover_color = hover_color
        self.click_color = click_color
        self.border_radius = border_radius

        # Text attributes
        self.text_color = text_color
        self.text_hover_color = text_hover_color
        self.text_click_color = text_click_color

        # States
        self.hovered = False
        self.clicked = False

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the button
        :param surface: pygame.Surface where the button will be drawn
        """
        if not self.display:
            return

        if self.clicked:
            pygame.draw.rect(surface, self.click_color, self.rect, border_radius=self.border_radius)
            self.text_object.change_text_color(self.text_click_color)
        elif self.hovered:
            pygame.draw.rect(surface, self.hover_color, self.rect, border_radius=self.border_radius)
            self.text_object.change_text_color(self.text_hover_color)
        else:
            pygame.draw.rect(surface, self.color, self.rect, border_radius=self.border_radius)
            self.text_object.change_text_color(self.text_color)

        self.text_object.draw(surface)

    def update(self) -> None:
        """
        Update the button,
        Collects the events and updates the button
        """
        self.text_object.update()

        # Check if the button is hovered
        self.hovered = self.is_hovered()