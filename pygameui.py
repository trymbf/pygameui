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
                return True

        return False

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

        # Get the dimensions of the text
        if width != 0 and height != 0:
            text_dimensions = (width, height)
        else:
            text_dimensions = self.get_text_rect_dimensions()

        super().__init__(position, text_dimensions[0], text_dimensions[1], color, centered)

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

    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw the text in the surface
        :param surface: pygame.Surface where the text will be drawn
        :return: None
        """

        if not self.display:
            return

        surface.blit(self.text_surface, self.rect)

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

        super().__init__(position, content=hint, color=passive_text_color, font_size=font_size, font_family=font_family, width=width, height=height, centered=centered)

        # Visual attributes
        self.passive_text_color = passive_text_color
        self.active_text_color = active_text_color
        self.passive_border_color = passive_border_color
        self.active_border_color = active_border_color
        self.border_radius = border_radius
        self.border_width = border_width

        # States
        self.active = False

    def draw(self, surface: pygame.surface):
        super().draw(surface)

        if self.active:
            pygame.draw.rect(surface, self.active_border_color, self.rect, self.border_width, border_radius=self.border_radius)
        else:
            pygame.draw.rect(surface, self.passive_border_color, self.rect, self.border_width, border_radius=self.border_radius)