import pygame

pygame.init()


VERSION = 1.2

class Text():
    def __init__(self, position: tuple, content:str, color:tuple, centerMode = True, fontName = "freesansbold.ttf", fontSize = 20):
        # Basic variables
        # Pos
        self.x, self.y = position
        # Show, if false the text will not be drawn
        self.hide = False
        # Font
        self.fontName = fontName
        self.fontSize = fontSize
        self.font = pygame.font.SysFont(self.fontName, self.fontSize)  # Load font
        # Text
        self.color = color
        self.content = content
        self.text = self.font.render(self.content, True, color) # Create surface object
        self.textRect = self.text.get_rect() # Get rect of text
        # centerMode
        self.centerMode = centerMode
        # Position textRect based on centerMode
        self.textRect.topleft = (self.x - (self.textRect.width // 2), self.y - (self.textRect.height // 2)) if self.centerMode else (self.x, self.y)
        
        # Other moving variables
        # Flowing
        self.flowing = False
        self.currentFlowPos = None
        self.otherFlowPos = None
        self.Xstep = 0
        self.Ystep = 0
        # Jumping
        self.jumping = False
        self.currentJumpPos = None
        self.otherJumpPos = None
        self.frames = 0
        self.frames_counter = 0
    
    def hide_toggle(self):
        self.hide = not self.hide

    def change(self, newContent = None, newColor = None, newFont = None, newFontSize = None):
        # If no new values are given, the old ones will be used
        if not newContent: newContent = self.content
        if not newColor: newColor = self.color
        if not newFont: newFont = self.fontName
        if not newFontSize: newFontSize = self.fontSize

        # Create new surface object 
        self.font = pygame.font.SysFont(newFont, newFontSize)  # Load font
        self.text = self.font.render(newContent, True, self.color)
        self.textRect = self.text.get_rect() # Get rect
        # centerMode
        self.textRect.topleft = (self.x - (self.textRect.width // 2), self.y - (self.textRect.height // 2)) if self.centerMode else (self.x, self.y)

    # Draws text on screen if not hidden
    def draw(self, win):
        if not self.hide: win.blit(self.text, self.textRect)
    
    # Updates and moves the text if needed
    def update(self):
        if self.flowing: # If flowing
            # Check if flow has reached a flowpoint
            if self.centerMode: # If centermode is activated we will use the rects centerposition, if not the topleft
                if (self.Xstep == 0 or self.Ystep == 0):
                    if ((self.Xstep > 0) and (self.textRect.centerx > self.currentFlowPos[0])) or ((self.Xstep < 0) and (self.textRect.centerx < self.currentFlowPos[0])) or ((self.Ystep < 0) and (self.textRect.centery < self.currentFlowPos[1])) or ((self.Ystep > 0) and (self.textRect.centery > self.currentFlowPos[1])):
                        self.Xstep, self.Ystep = -self.Xstep, -self.Ystep # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos
                else:
                    if (((self.Xstep > 0) and (self.textRect.centerx > self.currentFlowPos[0])) and ((self.Ystep > 0) and (self.textRect.centery > self.currentFlowPos[1]))) or (((self.Xstep > 0) and (self.textRect.centerx > self.currentFlowPos[0])) and ((self.Ystep < 0) and (self.textRect.centery < self.currentFlowPos[1]))) or (((self.Xstep < 0) and (self.textRect.centerx < self.currentFlowPos[0])) and ((self.Ystep > 0) and (self.textRect.centery > self.currentFlowPos[1])))or (((self.Xstep < 0) and (self.textRect.centerx < self.currentFlowPos[0])) and ((self.Ystep < 0) and (self.textRect.centery < self.currentFlowPos[1]))):
                        self.Xstep, self.Ystep = -self.Xstep, -self.Ystep # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos
            else:
                if (self.Xstep == 0 or self.Ystep == 0):
                    if ((self.Xstep > 0) and (self.textRect.x > self.currentFlowPos[0])) or ((self.Xstep < 0) and (self.textRect.x < self.currentFlowPos[0])) or ((self.Ystep < 0) and (self.textRect.y < self.currentFlowPos[1])) or ((self.Ystep > 0) and (self.textRect.y > self.currentFlowPos[1])):
                        self.Xstep, self.Ystep = -self.Xstep, -self.Ystep # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos
                else:
                    if (((self.Xstep > 0) and (self.textRect.x > self.currentFlowPos[0])) and ((self.Ystep > 0) and (self.textRect.y > self.currentFlowPos[1]))) or (((self.Xstep > 0) and (self.textRect.x > self.currentFlowPos[0])) and ((self.Ystep < 0) and (self.textRect.y < self.currentFlowPos[1]))) or (((self.Xstep < 0) and (self.textRect.x < self.currentFlowPos[0])) and ((self.Ystep > 0) and (self.textRect.y > self.currentFlowPos[1])))or (((self.Xstep < 0) and (self.textRect.x < self.currentFlowPos[0])) and ((self.Ystep < 0) and (self.textRect.y < self.currentFlowPos[1]))):
                        self.Xstep, self.Ystep = -self.Xstep, -self.Ystep # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos

            self.move(self.Xstep, self.Ystep) # Apply movement
        
        elif self.jumping: # If jumping
            self.frames_counter += 1 # Increase frame counter
            if self.frames_counter >= self.frames: # If it has gone enough time to switch position
                self.move_to(self.otherJumpPos[0], self.otherJumpPos[1]) # Apply movement
                self.currentJumpPos, self.otherJumpPos = self.otherJumpPos, self.currentJumpPos
                self.frames_counter = 0 # Reset counter

    # Moves to specific cordinates
    def move_to(self, x: int, y: int):
        if self.centerMode:
            self.x = x - (self.textRect.width // 2)
            self.y = y - (self.textRect.height // 2)
            self.textRect.topleft = (self.x, self.y)
        else:
            self.x, self.y = x, y
            self.textRect.topleft = (self.x, self.y)
    
    # Moves in x and y direction
    def move(self, xMovement: float, yMovement: float):
        # Used to make small movements posible (self.x is a float, self.textRect.x is an int)
        self.x += xMovement
        self.y += yMovement
        self.textRect.x = self.x
        self.textRect.y = self.y

    def is_hovered(self):
        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self.textRect.collidepoint(mouse_pos):
            return True 

    # Flow lets the text flow between two points
    def flow(self, position1: tuple, position2: tuple, iterations: int):
        # Move to flowpoint
        self.move_to(position1[0], position1[1])
        # Set flowpostions
        self.otherFlowPos, self.currentFlowPos = position1, position2 
        # Get amount to move per iteration
        Xdistance, Ydistance = (position2[0] - position1[0]), (position2[1] - position1[1])
        self.Xstep = Xdistance / iterations
        self.Ystep = Ydistance / iterations
        # Activate flowing
        self.flowing = True
    
    # Jump lets the user toggle the text between two points on a userSpecified timer
    def jump(self, position1: tuple, position2: tuple, frames: int):
        # Move to jumppoint
        self.move_to(position1[0], position1[1])
        # Set jumpPostions
        self.otherJumpPos, self.currentJumpPos = position2, position1
        # Frames
        self.frames = frames
        # Activate jumping
        self.jumping = True

class Element():     
    def __init__(self, position: tuple, content=None, textColor=(231, 111, 81), centerText=True, centerMode=True, fontName="freesansbold.ttf", fontSize=20, rectWidth=200, rectHeight=75, rectColor=(233, 196, 106), rectBorderRadius=10):
        # Common variables
        self.centerMode = centerMode
        self.content = content
        # Rect
        self.rectWidth = rectWidth
        self.rectHeight = rectHeight
        # Show
        self.hide = False
        # Flowing
        self.flowing = False
        self.currentFlowPos = None
        self.otherFlowPos = None
        self.Xstep = 0
        self.Ystep = 0
        # Jumping
        self.jumping = False
        self.currentJumpPos = None
        self.otherJumpPos = None
        self.frames = 0
        self.frames_counter = 0
        # Clicking
        self.clicked = True

        if isinstance(self.content, str):
            self.type = "text"
            # Pos
            self.x, self.y = (position[0] - (rectWidth // 2), position[1] - (rectHeight // 2)) if self.centerMode else (position[0], position[1])
            # Rect
            self.rect = pygame.rect.Rect(self.x, self.y, rectWidth, rectHeight)
            self.rectColor = rectColor
            self.borderRadius = rectBorderRadius
            # Load font
            self.fontName = fontName
            self.fontSize = fontSize
            self.font = pygame.font.SysFont(self.fontName, self.fontSize)  # Load font
            # Text
            self.centerText = centerText
            self.text = self.font.render(content, True, textColor) # Create surface object
            self.textRect = self.text.get_rect() # Get rect
            # centering the text
            if centerText: self.textRect.center = self.rect.center
            else: self.textRect.topleft = self.rect.topleft
        # If there is an image
        elif self.content:
            self.type = "image"
            try:
                self.content = pygame.transform.scale(self.content, (self.rectWidth, self.rectHeight))
                self.rect = self.content.get_rect()
            except:
                raise Exception(f"{self.content} is not a pygame image")
            
            if self.centerMode:
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
            self.x, self.y = (position[0] - (self.rectWidth // 2), position[1] - (self.rectHeight // 2)) if self.centerMode else (position[0], position[1])
            # Rect
            self.rect = pygame.rect.Rect(self.x, self.y, self.rectWidth, self.rectHeight)
            self.borderRadius = rectBorderRadius
            self.rectColor = rectColor

    def hide_toggle(self):
        self.hide = not self.hide

    def draw(self, win):
        if not self.hide:
            # If the element has text
            if self.type == "text":
                # Draw text
                pygame.draw.rect(win, self.rectColor, self.rect, border_radius = self.borderRadius)
                win.blit(self.text, self.textRect)
            # If the element has an image
            elif self.type == "image":
                # Draw img
                win.blit(self.content, self.rect)
            # If the element is a just rectangle
            elif self.type == "rectangle":
                pygame.draw.rect(win, self.rectColor, self.rect, border_radius = self.borderRadius)

    def is_hovered(self):
        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            return True 

    def is_clicked(self, button_elements: list):
        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1: # == 1 is left click
                return True
        else:
            for element in button_elements: # Checks if user is howering any other buttons
                if element.rect.collidepoint(mouse_pos):
                    break
            else: # If not howering any other buttons: set cursor to arrow
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def was_clicked(self, button_elements: list):
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
            for element in button_elements:
                if element.rect.collidepoint(mouse_pos):
                    break
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
        if pygame.mouse.get_pressed()[0] == 0: #  No mousebuttons down
            self.clicked = False

        return action

    # Updates and moves the text if needed
    def update(self):
        if self.flowing: # If flowing
            # Check if flow has reached a flowpoint
            if self.centerMode: # If centermode is activated we will use the rects centerposition, if not the topleft
                if (self.Xstep == 0 or self.Ystep == 0):
                    if ((self.Xstep > 0) and (self.rect.centerx > self.currentFlowPos[0])) or ((self.Xstep < 0) and (self.rect.centerx < self.currentFlowPos[0])) or ((self.Ystep < 0) and (self.rect.centery < self.currentFlowPos[1])) or ((self.Ystep > 0) and (self.rect.centery > self.currentFlowPos[1])):
                        self.Xstep, self.Ystep = -self.Xstep, -self.Ystep # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos
                else:
                    if (((self.Xstep > 0) and (self.rect.centerx > self.currentFlowPos[0])) and ((self.Ystep > 0) and (self.rect.centery > self.currentFlowPos[1]))) or (((self.Xstep > 0) and (self.rect.centerx > self.currentFlowPos[0])) and ((self.Ystep < 0) and (self.rect.centery < self.currentFlowPos[1]))) or (((self.Xstep < 0) and (self.rect.centerx < self.currentFlowPos[0])) and ((self.Ystep > 0) and (self.rect.centery > self.currentFlowPos[1])))or (((self.Xstep < 0) and (self.rect.centerx < self.currentFlowPos[0])) and ((self.Ystep < 0) and (self.rect.centery < self.currentFlowPos[1]))):
                        self.Xstep, self.Ystep = -self.Xstep, -self.Ystep # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos
            else:
                if (self.Xstep == 0 or self.Ystep == 0):
                    if ((self.Xstep > 0) and (self.rect.x > self.currentFlowPos[0])) or ((self.Xstep < 0) and (self.rect.x < self.currentFlowPos[0])) or ((self.Ystep < 0) and (self.rect.y < self.currentFlowPos[1])) or ((self.Ystep > 0) and (self.rect.y > self.currentFlowPos[1])):
                        self.Xstep, self.Ystep = -self.Xstep, -self.Ystep # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos
                else:
                    if (((self.Xstep > 0) and (self.rect.x > self.currentFlowPos[0])) and ((self.Ystep > 0) and (self.rect.y > self.currentFlowPos[1]))) or (((self.Xstep > 0) and (self.rect.x > self.currentFlowPos[0])) and ((self.Ystep < 0) and (self.rect.y < self.currentFlowPos[1]))) or (((self.Xstep < 0) and (self.rect.x < self.currentFlowPos[0])) and ((self.Ystep > 0) and (self.rect.y > self.currentFlowPos[1])))or (((self.Xstep < 0) and (self.rect.x < self.currentFlowPos[0])) and ((self.Ystep < 0) and (self.rect.y < self.currentFlowPos[1]))):
                        self.Xstep, self.Ystep = -self.Xstep, -self.Ystep # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos

            self.move(self.Xstep, self.Ystep) # Apply movement
        
        elif self.jumping: # If jumping
            self.frames_counter += 1 # Increase frame counter
            if self.frames_counter >= self.frames: # If it has gone enough time to switch position
                self.move_to(self.otherJumpPos[0], self.otherJumpPos[1]) # Apply movement
                self.currentJumpPos, self.otherJumpPos = self.otherJumpPos, self.currentJumpPos
                self.frames_counter = 0 # Reset counter

    # Moves to specific cordinates
    def move_to(self, x: int, y:  int):
        if self.centerMode:
            self.rect.center = (x, y)
            self.x, self.y = self.rect.center
            if self.type == "text": # Only affect the textRect if there is text
                if self.centerText:
                    self.textRect.center = self.rect.center
                else:
                    self.textRect.topleft = self.rect.topleft
        else:
            self.rect.topleft = (x, y)
            self.x, self.y = self.rect.topleft
            if self.type == "text": # Only affect the textRect if there is text
                if self.centerText:
                    self.textRect.center = self.rect.center
                else:
                    self.textRect.topleft = self.rect.topleft
    
    # Moves in x and y direction
    def move(self, xMovement: float, yMovement: float):
        # Used to make small movements posible (self.x is a float, self.textRect.x is an int)
        self.x += xMovement
        self.y += yMovement
        if self.centerMode:
            self.rect.center = (self.x, self.y)
            if self.type == "text": # Only affect the textRect if there is text
                if self.centerText:
                    self.textRect.center = self.rect.center
                else:
                    self.textRect.topleft = self.rect.topleft
        else:
            self.rect.topleft = (self.x, self.y)
            if self.type == "text": # Only affect the textRect if there is text
                if self.centerText:
                    self.textRect.center = self.rect.center
                else:
                    self.textRect.topleft = self.rect.topleft

    # Flow lets the text flow between two points
    def flow(self, position1: tuple, position2: tuple, iterations: int):
        # Move to flowpoint
        self.move_to(position1[0], position1[1])
        # Set flowpostions
        self.otherFlowPos, self.currentFlowPos = position1, position2 
        # Get amount to move per iteration
        Xdistance, Ydistance = (position2[0] - position1[0]), (position2[1] - position1[1])
        self.Xstep = Xdistance / iterations
        self.Ystep = Ydistance / iterations
        # Activate flowing
        self.flowing = True
    
    # Jump lets the user toggle the text between two points on a userSpecified timer
    def jump(self, position1: tuple, position2: tuple, frames: int):
        # Move to jumppoint
        self.move_to(position1[0], position1[1])
        # Set jumpPostions
        self.otherJumpPos, self.currentJumpPos = position2, position1
        # Frames
        self.frames = frames
        # Activate jumping
        self.jumping = True

class Input():
    def __init__(self, position: tuple, fontName = "freesansbold.ttf", fontSize = 30, exampleContent = "Click me to input!", prefilledContent = "", characterLimit = 100, normalTextColor = (231, 111, 81), exampleTextColor = (100, 100, 100), rectWidth = 200, rectHeight = 50, rectColorActive = (233, 196, 106), rectColorPassive = (200, 200, 200), rectBorderRadius = 1, rectBorderWidth = 5, centerMode = True):
        pygame.scrap.init()
        pygame.scrap.set_mode(pygame.SCRAP_CLIPBOARD)
        
        # Create position variables and font
        self.centerMode = centerMode
        # Pos
        self.x, self.y = (position[0] - (rectWidth // 2), position[1] - (rectHeight // 2)) if centerMode else (position[0], position[1])
        # Rect
        self.rect = pygame.rect.Rect(self.x, self.y, rectWidth, rectHeight)
        self.borderRadius = rectBorderRadius
        self.rectBorderWidth = rectBorderWidth
        self.rectColorPassive = rectColorPassive
        self.rectColorActive = rectColorActive
        # Text
        self.normalTextColor = normalTextColor
        self.exampleTextColor = exampleTextColor
        self.characterLimit = characterLimit
        self.fontName = fontName
        self.fontSize = fontSize
        self.font = pygame.font.SysFont(self.fontName, self.fontSize)  # Load font
        self.prefilledContent = prefilledContent
        self.userText = self.prefilledContent
        self.exampleContent = exampleContent
        self.userTextSurface = self.font.render(self.userText, True, self.normalTextColor) # Create surface object for the userText
        self.exampleTextSurface = self.font.render(self.exampleContent, True, self.exampleTextColor) # Create surface object the exampleText

        self.userTextRect = self.userTextSurface.get_rect() # Get rect
        self.exampleTextRect = self.exampleTextSurface.get_rect() # Get rect
        # centering the text
        self.userTextRect.center = self.rect.center
        self.exampleTextRect.center = self.rect.center
        # Show
        self.hide = False
        # Flowing
        self.flowing = False
        self.currentFlowPos = None
        self.otherFlowPos = None
        self.Xstep = 0
        self.Ystep = 0
        # Jumping
        self.jumping = False
        self.currentJumpPos = None
        self.otherJumpPos = None
        self.frames = 0
        self.frames_counter = 0
        # Clicking
        self.clicked = False
        self.active = False

    def hide_toggle(self):
        self.hide = not self.hide

    def draw(self, win):
        if not self.hide:
            if self.userText != "":
                win.blit(self.userTextSurface, self.userTextRect)
            else:
                if not self.active:
                    win.blit(self.exampleTextSurface, self.exampleTextRect)
                    
            if self.active:
                pygame.draw.rect(win, self.rectColorActive, self.rect, self.rectBorderWidth, border_radius = self.borderRadius)
            else:
                pygame.draw.rect(win, self.rectColorPassive, self.rect, self.rectBorderWidth, border_radius = self.borderRadius)

    def getText(self):
        return self.userText

    def work(self, events: list, clickable_elements: list):
        # Make activating work
        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # == 1 is left click
                self.active = not self.active
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

        # Make writing work
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_v and event.mod & pygame.KMOD_CTRL:
                        self.userText = pygame.scrap.get("text/plain;charset=utf-8").decode()
                        self.userText = self.userText.replace("\x00", "")
                    elif event.key == pygame.K_BACKSPACE:
                        self.userText = self.userText[0: -1] # Removes last character
                    elif (len(self.userText) <= self.characterLimit) and event.key != pygame.K_RETURN: # Keep text under character limit and don't enterperate enter as a key
                        self.userText += event.unicode # Adds the userinput to the text
                    self.userTextSurface = self.font.render(self.userText, True, self.normalTextColor) # Create surface object for the userText
                    self.userTextRect = self.userTextSurface.get_rect() # Get rect
                    self.userTextRect.center = self.rect.center

    # Updates and moves the text if needed
    def update(self):
        if self.flowing: # If flowing
            # Check if flow has reached a flowpoint
            if self.centerMode: # If centermode is activated we will use the rects centerposition, if not the topleft
                if (self.Xstep == 0 or self.Ystep == 0):
                    if ((self.Xstep > 0) and (self.rect.centerx > self.currentFlowPos[0])) or ((self.Xstep < 0) and (self.rect.centerx < self.currentFlowPos[0])) or ((self.Ystep < 0) and (self.rect.centery < self.currentFlowPos[1])) or ((self.Ystep > 0) and (self.rect.centery > self.currentFlowPos[1])):
                        self.Xstep, self.Ystep = -self.Xstep, -self.Ystep # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos
                else:
                    if (((self.Xstep > 0) and (self.rect.centerx > self.currentFlowPos[0])) and ((self.Ystep > 0) and (self.rect.centery > self.currentFlowPos[1]))) or (((self.Xstep > 0) and (self.rect.centerx > self.currentFlowPos[0])) and ((self.Ystep < 0) and (self.rect.centery < self.currentFlowPos[1]))) or (((self.Xstep < 0) and (self.rect.centerx < self.currentFlowPos[0])) and ((self.Ystep > 0) and (self.rect.centery > self.currentFlowPos[1])))or (((self.Xstep < 0) and (self.rect.centerx < self.currentFlowPos[0])) and ((self.Ystep < 0) and (self.rect.centery < self.currentFlowPos[1]))):
                        self.Xstep, self.Ystep = -self.Xstep, -self.Ystep # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos
            else:
                if (self.Xstep == 0 or self.Ystep == 0):
                    if ((self.Xstep > 0) and (self.rect.x > self.currentFlowPos[0])) or ((self.Xstep < 0) and (self.rect.x < self.currentFlowPos[0])) or ((self.Ystep < 0) and (self.rect.y < self.currentFlowPos[1])) or ((self.Ystep > 0) and (self.rect.y > self.currentFlowPos[1])):
                        self.Xstep, self.Ystep = -self.Xstep, -self.Ystep # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos
                else:
                    if (((self.Xstep > 0) and (self.rect.x > self.currentFlowPos[0])) and ((self.Ystep > 0) and (self.rect.y > self.currentFlowPos[1]))) or (((self.Xstep > 0) and (self.rect.x > self.currentFlowPos[0])) and ((self.Ystep < 0) and (self.rect.y < self.currentFlowPos[1]))) or (((self.Xstep < 0) and (self.rect.x < self.currentFlowPos[0])) and ((self.Ystep > 0) and (self.rect.y > self.currentFlowPos[1])))or (((self.Xstep < 0) and (self.rect.x < self.currentFlowPos[0])) and ((self.Ystep < 0) and (self.rect.y < self.currentFlowPos[1]))):
                        self.Xstep, self.Ystep = -self.Xstep, -self.Ystep # Switch direction
                        self.currentFlowPos, self.otherFlowPos = self.otherFlowPos, self.currentFlowPos

            self.move(self.Xstep, self.Ystep) # Apply movement
        
        elif self.jumping: # If jumping
            self.frames_counter += 1 # Increase frame counter
            if self.frames_counter >= self.frames: # If it has gone enough time to switch position
                self.move_to(self.otherJumpPos[0], self.otherJumpPos[1]) # Apply movement
                self.currentJumpPos, self.otherJumpPos = self.otherJumpPos, self.currentJumpPos
                self.frames_counter = 0 # Reset counter

    # Moves to specific cordinates
    def move_to(self, x: int, y:  int):
        if self.centerMode:
            self.rect.center = (x, y)
            self.x, self.y = self.rect.center
            self.userTextRect.center = (x, y)
            self.exampleTextRect.center = (x, y)
        else:
            self.rect.topleft = (x, y)
            self.x, self.y = self.rect.topleft
            self.userTextRect.topleft = (self.x, self.y)
            self.exampleTextRect.topleft = (self.x, self.y)
    
    # Moves in x and y direction
    def move(self, xMovement: float, yMovement: float):
        # Used to make small movements posible (self.x is a float, self.textRect.x is an int)
        self.x += xMovement
        self.y += yMovement
        if self.centerMode:
            self.rect.center = (self.x, self.y)
            self.userTextRect.center = (self.x, self.y)
            self.exampleTextRect.center = (self.x, self.y)
        else:
            self.rect.topleft = (self.x, self.y)
            self.userTextRect.topleft = (self.x, self.y)
            self.exampleTextRect.topleft = (self.x, self.y)
    
    def is_hovered(self):
        # Get mouse pos
        mouse_pos = pygame.mouse.get_pos()

        # Check mouse over and clicked conditions
        if self.rect.collidepoint(mouse_pos):
            return True 

    # Flow lets the text flow between two points
    def flow(self, position1: tuple, position2: tuple, iterations: int):
        # Move to flowpoint
        self.move_to(position1[0], position1[1])
        # Set flowpostions
        self.otherFlowPos, self.currentFlowPos = position1, position2 
        # Get amount to move per iteration
        Xdistance, Ydistance = (position2[0] - position1[0]), (position2[1] - position1[1])
        self.Xstep = Xdistance / iterations
        self.Ystep = Ydistance / iterations
        # Activate flowing
        self.flowing = True
    
    # Jump lets the user toggle the text between two points on a userSpecified timer
    def jump(self, position1: tuple, position2: tuple, frames: int):
        # Move to jumppoint
        self.move_to(position1[0], position1[1])
        # Set jumpPostions
        self.otherJumpPos, self.currentJumpPos = position2, position1
        # Frames
        self.frames = frames
        # Activate jumping
        self.jumping = True
