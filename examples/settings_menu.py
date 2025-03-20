import pygame
import sys
import pygameui

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((700, 600))
pygame.display.set_caption("PyGameUI Settings Example")

# Define colors
BG_COLOR = (25, 25, 35)
PANEL_COLOR = (35, 35, 45)
ACCENT_COLOR = (86, 140, 235) 
ACCENT_HOVER = (120, 170, 255)
TEXT_COLOR = (230, 230, 240)
SLIDER_BG = (60, 60, 70)
SLIDER_FILL = (120, 140, 200)

# Create UI elements
header = pygameui.Text((350, 50), "Game Settings", TEXT_COLOR, font_size=42, centered=True)

# Settings panel
settings_panel = pygameui.Element((350, 300), 650, 450, PANEL_COLOR, border_radius=15, centered=True)

# Volume settings
volume_header = pygameui.Text((350, 130), "Volume Controls", TEXT_COLOR, font_size=28, centered=True)

music_label = pygameui.Text((190, 180), "Music Volume:", TEXT_COLOR, font_size=18, centered=True)
music_vol_bg = pygameui.Element((470, 180), 300, 20, SLIDER_BG, centered=True)
music_vol_fill = pygameui.Element((470 - (300-225)/2, 180), 225, 20, SLIDER_FILL, centered=True)  # 75% filled

sfx_label = pygameui.Text((190, 220), "SFX Volume:", TEXT_COLOR, font_size=18, centered=True)
sfx_vol_bg = pygameui.Element((470, 220), 300, 20, SLIDER_BG, centered=True)
sfx_vol_fill = pygameui.Element((470 - (300-210)/2, 220), 210, 20, SLIDER_FILL, centered=True)  # 70% filled

# Display settings
display_header = pygameui.Text((350, 270), "Display Settings", TEXT_COLOR, font_size=28, centered=True)

resolution_label = pygameui.Text((150, 320), "Resolution:", TEXT_COLOR, font_size=18, centered=True)
resolution_btn = pygameui.Button((380, 320), 200, 30, 5, "1920x1080", ACCENT_COLOR, ACCENT_HOVER, text_color=TEXT_COLOR, centered=True)

fullscreen_label = pygameui.Text((150, 360), "Fullscreen:", TEXT_COLOR, font_size=18, centered=True)
fullscreen_btn = pygameui.Button((380, 360), 200, 30, 5, "Enabled", ACCENT_COLOR, ACCENT_HOVER, text_color=TEXT_COLOR, centered=True)

vsync_label = pygameui.Text((150, 400), "VSync:", TEXT_COLOR, font_size=18, centered=True)
vsync_btn = pygameui.Button((380, 400), 200, 30, 5, "Disabled", ACCENT_COLOR, ACCENT_HOVER, text_color=TEXT_COLOR, centered=True)

# Bottom buttons
save_btn = pygameui.Button((250, 500), 200, 50, 5, "Save Changes", ACCENT_COLOR, ACCENT_HOVER, text_color=TEXT_COLOR, centered=True)
cancel_btn = pygameui.Button((470, 500), 200, 50, 5, "Cancel", (120, 120, 140), (150, 150, 170), text_color=TEXT_COLOR, centered=True)

# Status message
status_msg = pygameui.Text((350, 560), "", TEXT_COLOR, font_size=16, centered=True)

# Group all elements
elements = [
    settings_panel, header, 
    volume_header, music_label, music_vol_bg, music_vol_fill,
    sfx_label, sfx_vol_bg, sfx_vol_fill,
    display_header, resolution_label, resolution_btn,
    fullscreen_label, fullscreen_btn,
    vsync_label, vsync_btn,
    save_btn, cancel_btn, status_msg
]

# Toggle states
fullscreen_enabled = True
vsync_enabled = False
resolution_options = ["1920x1080", "1680x1050", "1600x900", "1366x768", "1280x720"]
resolution_index = 0

# Handle button clicks
def handle_button_click(button):
    global fullscreen_enabled, vsync_enabled, resolution_index
    
    if button == fullscreen_btn:
        fullscreen_enabled = not fullscreen_enabled
        fullscreen_btn._text = "Enabled" if fullscreen_enabled else "Disabled"
    
    elif button == vsync_btn:
        vsync_enabled = not vsync_enabled
        vsync_btn._text = "Enabled" if vsync_enabled else "Disabled"
    
    elif button == resolution_btn:
        resolution_index = (resolution_index + 1) % len(resolution_options)
        resolution_btn._text = resolution_options[resolution_index]
    
    elif button == save_btn:
        status_msg.change_text("Settings saved successfully!")
        status_msg.set_text_color((86, 235, 120))
    
    elif button == cancel_btn:
        status_msg.change_text("Changes discarded")
        status_msg.set_text_color((235, 86, 86))

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
            for button in [resolution_btn, fullscreen_btn, vsync_btn, save_btn, cancel_btn]:
                if button.is_hovered():
                    handle_button_click(button)
    
    # Update all elements
    for element in elements:
        element.update()
    
    # Draw everything
    screen.fill(BG_COLOR)
    for element in elements:
        element.draw(screen)
    
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
