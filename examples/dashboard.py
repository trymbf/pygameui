"""
Dashboard UI using pygameui
This code creates a simple dashboard UI using the pygameui library.
It includes a user profile section, a main content area with statistics,
and a notification area.
"""

import pygame
import pygameui

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGameUI Dashboard")

# Define colors
DARK_BG = (30, 30, 40)
LIGHT_BG = (45, 45, 60)
ACCENT = (86, 140, 235)
ACCENT_HOVER = (120, 170, 255)
TEXT_COLOR = (240, 240, 245)
ERROR_COLOR = (235, 86, 86)
SUCCESS_COLOR = (86, 235, 120)

# Create UI elements
header = pygameui.Text((400, 50), "Dashboard", TEXT_COLOR, font_size=40, centered=True)

# User profile section - using Element instead of Panel which doesn't exist
profile_bg = pygameui.Element((20, 100), 250, 480, LIGHT_BG, border_radius=10)
# Use proper Image parameters according to implementation
try:
    avatar = pygameui.Image((145, 180), "assets/imgs/avatar.jpeg", 
                         width=150, height=150, centered=True)
except Exception as e:
    # Fallback if image can't be loaded
    pass

username_display = pygameui.Text((145, 280), "trymbf", TEXT_COLOR, font_size=24, centered=True)
status = pygameui.Text((145, 310), "Online", SUCCESS_COLOR, font_size=18, centered=True)
logout_btn = pygameui.Button((145, 530), 200, 40, 4, "Logout", ACCENT, ACCENT_HOVER, text_color=TEXT_COLOR, centered=True)

# Main content area - using Element instead of Panel
content_bg = pygameui.Element((290, 100), 490, 480, LIGHT_BG, border_radius=10)
welcome_text = pygameui.Text((535, 140), "Welcome back!", TEXT_COLOR, font_size=28, centered=True)

# Stats section - remove ProgressBar and use Element instead
stats_title = pygameui.Text((535, 200), "Your Statistics", TEXT_COLOR, font_size=22, centered=True)
stat1_bg = pygameui.Element((535, 250), 400, 30, (100, 100, 120), centered=True)
stat1_fill = pygameui.Element((535 - (400-300)/2, 250), 300, 30, ACCENT, centered=True) # 75% filled
stat1_label = pygameui.Text((535, 280), "Projects Completed: 75%", TEXT_COLOR, font_size=16, centered=True)
stat2_bg = pygameui.Element((535, 330), 400, 30, (100, 100, 120), centered=True)
stat2_fill = pygameui.Element((535 - (400-160)/2, 330), 160, 30, ACCENT, centered=True) # 40% filled
stat2_label = pygameui.Text((535, 360), "Tasks Finished: 40%", TEXT_COLOR, font_size=16, centered=True)

# Notification area
notif_title = pygameui.Text((535, 410), "Recent Notifications", TEXT_COLOR, font_size=22, centered=True)
notif1 = pygameui.Text((535, 450), "New message from Alex", TEXT_COLOR, font_size=16, centered=True)
notif2 = pygameui.Text((535, 480), "Project deadline tomorrow", ERROR_COLOR, font_size=16, centered=True)
clear_notif_btn = pygameui.Button((535, 530), 200, 40, 4, "Clear All", ACCENT, ACCENT_HOVER, text_color=TEXT_COLOR, centered=True)

# Put all elements in a list for easy updating and drawing
elements = [
    header, profile_bg, username_display, status, logout_btn,
    content_bg, welcome_text, stats_title, stat1_bg, stat1_fill, stat1_label, 
    stat2_bg, stat2_fill, stat2_label, notif_title, notif1, notif2, clear_notif_btn
]

# Try to add avatar if it was loaded
try:
    if avatar:
        elements.append(avatar)
except:
    pass

run = True
while run:
    events = pygame.event.get()
    
    # Handle events
    for event in events:
        if event.type == pygame.QUIT:
            run = False

    if logout_btn.was_clicked():
        status.change_text("Logging out...")
        status.change_text_color(ERROR_COLOR)

    if clear_notif_btn.was_clicked():
        notif1.change_text("No new notifications")
        notif2.change_text("")

    # Update elements - the update method doesn't take parameters
    for element in elements:
        element.update()

    # Draw everything
    screen.fill(DARK_BG)
    
    for element in elements:
        element.draw(screen)

    # Update screen
    pygame.display.flip()