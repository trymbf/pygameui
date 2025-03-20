import pygame
import sys
import pygameui

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("PyGameUI Login Example")

# Define colors
BG_COLOR = (25, 25, 35)
PANEL_COLOR = (35, 35, 45)
ACCENT_COLOR = (86, 140, 235)
ACCENT_HOVER = (120, 170, 255)
TEXT_COLOR = (230, 230, 240)
ERROR_COLOR = (235, 86, 86)
SUCCESS_COLOR = (86, 235, 120)

# Create UI elements
header = pygameui.Text((250, 100), "Login", TEXT_COLOR, font_size=48, centered=True)
subheader = pygameui.Text((250, 150), "Enter your credentials", TEXT_COLOR, font_size=18, centered=True)

# Panel background
login_panel = pygameui.Element((250, 350), 400, 400, PANEL_COLOR, border_radius=10, centered=True)

# Username input
username_label = pygameui.Text((250, 230), "Username", TEXT_COLOR, font_size=18, centered=True)
username_input = pygameui.Input((250, 270), 300, 50, 
                               passive_text_color=(150, 150, 150),
                               active_text_color=TEXT_COLOR,
                               passive_border_color=ACCENT_COLOR,
                               active_border_color=ACCENT_HOVER,
                               border_radius=5,
                               border_width=2,
                               hint="Enter username",
                               centered=True)

# Password input
password_label = pygameui.Text((250, 330), "Password", TEXT_COLOR, font_size=18, centered=True)
password_input = pygameui.Input((250, 370), 300, 50, 
                               passive_text_color=(150, 150, 150),
                               active_text_color=TEXT_COLOR,
                               passive_border_color=ACCENT_COLOR,
                               active_border_color=ACCENT_HOVER,
                               border_radius=5,
                               border_width=2,
                               hint="Enter password",
                               centered=True)

# Login button
login_btn = pygameui.Button((250, 450), 300, 50, 5, "LOGIN", 
                           ACCENT_COLOR, ACCENT_HOVER, 
                           text_color=TEXT_COLOR, 
                           font_size=20,
                           centered=True)

# Status message
status_msg = pygameui.Text((250, 500), "", TEXT_COLOR, font_size=16, centered=True)

# Group all elements
elements = [
    login_panel, header, subheader, 
    username_label, username_input,
    password_label, password_input,
    login_btn, status_msg
]

# Handle login attempt
def attempt_login():
    username = username_input.get_text()
    password = password_input.get_text()
    
    if username == "admin" and password == "password":
        status_msg.change_text("Login successful!")
        status_msg.change_text_color(SUCCESS_COLOR)
    else:
        status_msg.change_text("Invalid username or password")
        status_msg.change_text_color(ERROR_COLOR)

# Main game loop
running = True
while running:
    events = pygame.event.get()
    
    # Handle events
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
        # Handle button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if login_btn.is_hovered():
                attempt_login()
    
    # Update all elements
    for element in elements:
        if isinstance(element, pygameui.Input):
            element.update(events)
        else:
            element.update()
    
    # Draw everything
    screen.fill(BG_COLOR)
    for element in elements:
        element.draw(screen)
    
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
