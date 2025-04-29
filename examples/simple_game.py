"""
Simple Game Example using PygameUI
----------------------------------
This example demonstrates how to create a simple clicker game with UI components
for score tracking, upgrades, and settings.
"""

import pygame
import pygameui
import time

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PygameUI Clicker Game")
clock = pygame.time.Clock()

# Game state
game_state = {
    "score": 0,
    "click_value": 1,
    "passive_income": 0,
    "last_tick": time.time(),
    "background_color": (30, 30, 50)
}

# UI State
current_screen = "main"  # "main", "shop", "settings"

# -------------------------
# UI Components - Main Screen
# -------------------------

# Game title
game_title = pygameui.Text(
    position=(400, 50),
    content="PygameUI Clicker",
    color=(255, 255, 255),
    font_size=36,
    centered=True
)

# Score display
score_display = pygameui.Text(
    position=(400, 120),
    content=f"Score: {game_state['score']}",
    color=(220, 220, 100),
    font_size=24,
    centered=True
)

# Click value display
click_value_display = pygameui.Text(
    position=(400, 160),
    content=f"+{game_state['click_value']} per click",
    color=(150, 220, 150),
    font_size=18,
    centered=True
)

# Passive income display
passive_income_display = pygameui.Text(
    position=(400, 190),
    content=f"+{game_state['passive_income']} per second",
    color=(150, 150, 220),
    font_size=18,
    centered=True
)

# Main clicker button
clicker_button = pygameui.Button(
    position=(400, 300),
    width=150,
    height=150,
    label="CLICK",
    color=(70, 100, 200),
    hover_color=(90, 120, 220),
    click_color=(50, 80, 180),
    text_color=(255, 255, 255),
    border_radius=75,  # Make it circular
    font_size=28,
    centered=True
)

# Shop button
shop_button = pygameui.Button(
    position=(200, 500),
    width=180,
    height=60,
    label="Shop",
    color=(80, 150, 80),
    hover_color=(100, 170, 100),
    click_color=(60, 130, 60),
    text_color=(255, 255, 255),
    border_radius=10,
    centered=True
)

# Settings button
settings_button = pygameui.Button(
    position=(600, 500),
    width=180,
    height=60,
    label="Settings",
    color=(150, 80, 80),
    hover_color=(170, 100, 100),
    click_color=(130, 60, 60),
    text_color=(255, 255, 255),
    border_radius=10,
    centered=True
)

home_elements = [
    game_title,
    score_display,
    click_value_display,
    passive_income_display,
    clicker_button,
    shop_button,
    settings_button
]

# -------------------------
# UI Components - Shop Screen
# -------------------------

shop_title = pygameui.Text(
    position=(400, 50),
    content="Upgrade Shop",
    color=(255, 255, 255),
    font_size=36,
    centered=True
)

shop_score_display = pygameui.Text(
    position=(400, 100),
    content=f"Score: {game_state['score']}",
    color=(220, 220, 100),
    font_size=24,
    centered=True
)

# Back button in shop
shop_back_button = pygameui.Button(
    position=(100, 50),
    width=100,
    height=40,
    label="Back",
    color=(100, 100, 100),
    hover_color=(120, 120, 120),
    click_color=(80, 80, 80),
    text_color=(255, 255, 255),
    border_radius=5,
    centered=True
)

cant_afford_message = pygameui.Text(
    position=(400, 450),
    content="",
    color=(255, 100, 100),
    font_size=18,
    centered=True
)

shop_elements = [
    shop_title,
    shop_score_display,
    shop_back_button,
    cant_afford_message
]

# Shop items
shop_items = [
    {
        "name": "Better Clicker",
        "description": "Increases click value by 1",
        "cost": 10,
        "effect": lambda state: state.update(click_value=state["click_value"] + 1),
        "button": pygameui.Button(
            position=(400, 200),
            width=300,
            height=60,
            label="Better Clicker (10 points)",
            color=(70, 100, 150),
            hover_color=(90, 120, 170),
            click_color=(50, 80, 130),
            text_color=(255, 255, 255),
            border_radius=5,
            centered=True
        )
    },
    {
        "name": "Auto Clicker",
        "description": "Adds 1 point per second",
        "cost": 50,
        "effect": lambda state: state.update(passive_income=state["passive_income"] + 1),
        "button": pygameui.Button(
            position=(400, 280),
            width=300,
            height=60,
            label="Auto Clicker (50 points)",
            color=(70, 100, 150),
            hover_color=(90, 120, 170),
            click_color=(50, 80, 130),
            text_color=(255, 255, 255),
            border_radius=5,
            centered=True
        )
    },
    {
        "name": "Score Multiplier",
        "description": "Doubles your click value",
        "cost": 200,
        "effect": lambda state: state.update(click_value=state["click_value"] * 2),
        "button": pygameui.Button(
            position=(400, 360),
            width=300,
            height=60,
            label="Score Multiplier (200 points)",
            color=(70, 100, 150),
            hover_color=(90, 120, 170),
            click_color=(50, 80, 130),
            text_color=(255, 255, 255),
            border_radius=5,
            centered=True
        )
    }
]

# -------------------------
# UI Components - Settings Screen
# -------------------------

settings_title = pygameui.Text(
    position=(400, 50),
    content="Settings",
    color=(255, 255, 255),
    font_size=36,
    centered=True
)

# Back button in settings
settings_back_button = pygameui.Button(
    position=(100, 50),
    width=100,
    height=40,
    label="Back",
    color=(100, 100, 100),
    hover_color=(120, 120, 120),
    click_color=(80, 80, 80),
    text_color=(255, 255, 255),
    border_radius=5,
    centered=True
)

# Color theme setting
theme_title = pygameui.Text(
    position=(400, 150),
    content="Background Theme:",
    color=(255, 255, 255),
    font_size=24,
    centered=True
)

theme_options = ["Dark Blue", "Dark Gray", "Dark Purple", "Dark Green"]
theme_colors = {
    "Dark Blue": (30, 30, 50),
    "Dark Gray": (40, 40, 40),
    "Dark Purple": (40, 30, 50),
    "Dark Green": (30, 50, 30)
}

theme_dropdown = pygameui.DropdownMenu(
    position=(400, 200),
    width=200,
    height=40,
    options=theme_options,
    color=(60, 60, 60),
    hover_color=(80, 80, 80),
    text_color=(255, 255, 255),
    border_radius=5,
    element_height=23,
    centered=True
)

# Reset game button
reset_title = pygameui.Text(
    position=(400, 300),
    content="Reset Game:",
    color=(255, 255, 255),
    font_size=24,
    centered=True
)

reset_button = pygameui.Button(
    position=(400, 350),
    width=200,
    height=60,
    label="Reset Score",
    color=(200, 60, 60),
    hover_color=(220, 80, 80),
    click_color=(180, 40, 40),
    text_color=(255, 255, 255),
    border_radius=10,
    centered=True
)

settings_elements = [
    settings_title,
    settings_back_button,
    theme_title,
    reset_title,
    reset_button,
    theme_dropdown,
]

# Reset confirmation dialog
reset_confirm_bg = pygameui.Element(
    position=(400, 300),
    width=400,
    height=200,
    color=(40, 40, 40),
    border_color=(150, 150, 150),
    border_width=2,
    border_radius=10,
    centered=True
)

reset_confirm_text = pygameui.Text(
    position=(400, 250),
    content="Are you sure you want to reset?",
    color=(255, 255, 255),
    font_size=24,
    centered=True
)

reset_confirm_yes = pygameui.Button(
    position=(300, 330),
    width=120,
    height=50,
    label="Yes",
    color=(200, 60, 60),
    hover_color=(220, 80, 80),
    click_color=(180, 40, 40),
    text_color=(255, 255, 255),
    border_radius=5,
    centered=True
)

reset_confirm_no = pygameui.Button(
    position=(500, 330),
    width=120,
    height=50,
    label="No",
    color=(60, 60, 200),
    hover_color=(80, 80, 220),
    click_color=(40, 40, 180),
    text_color=(255, 255, 255),
    border_radius=5,
    centered=True
)

# Game states
showing_reset_confirm = False

# Helper functions for cleaner code
def handle_reset_confirmation(events):
    global showing_reset_confirm
    
    # Update dialog elements
    reset_confirm_bg.update(events)
    reset_confirm_text.update(events)
    reset_confirm_yes.update(events)
    reset_confirm_no.update(events)
    
    # Draw dialog elements
    reset_confirm_bg.draw(screen)
    reset_confirm_text.draw(screen)
    reset_confirm_yes.draw(screen)
    reset_confirm_no.draw(screen)
    
    # Handle button actions
    if reset_confirm_yes.was_clicked():
        # Reset the game
        game_state["score"] = 0
        game_state["click_value"] = 1
        game_state["passive_income"] = 0
        showing_reset_confirm = False
    
    if reset_confirm_no.was_clicked():
        showing_reset_confirm = False

# -------------------------
# Game Loop
# -------------------------

running = True
while running:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
    # Calculate passive income
    current_time = time.time()
    elapsed = current_time - game_state["last_tick"]
    if elapsed >= 1.0:  # Every second
        game_state["score"] += game_state["passive_income"]
        game_state["last_tick"] = current_time

    # Update score displays
    score_display.set_content(f"Score: {game_state['score']}")
    shop_score_display.set_content(f"Score: {game_state['score']}")
    click_value_display.set_content(f"+{game_state['click_value']} per click")
    passive_income_display.set_content(f"+{game_state['passive_income']} per second")
    
    # Clear screen with current background color
    screen.fill(game_state["background_color"])
    
    # -------------------------
    # Main Screen
    # -------------------------
    if current_screen == "main":
        # Update UI elements
        for element in home_elements:
            element.update(events)
        
        # Handle button clicks
        if clicker_button.was_clicked():
            game_state["score"] += game_state["click_value"]
            # Add a little animation
            clicker_button.flow(
                start_position=clicker_button.get_position(),
                end_position=(clicker_button.get_position()[0], clicker_button.get_position()[1] + 10),
                time=100,
                loop=False
            )
            clicker_button.set_animate(True)
            
        if shop_button.was_clicked():
            current_screen = "shop"
            
        if settings_button.was_clicked():
            current_screen = "settings"
            
        # Draw UI elements
        for element in home_elements:
            element.draw(screen)
    
    # -------------------------
    # Shop Screen
    # -------------------------
    elif current_screen == "shop":
        # Update UI elements
        for element in shop_elements:
            element.update(events)
        
        # Handle back button
        if shop_back_button.was_clicked():
            current_screen = "main"
            cant_afford_message.set_content("")

        # Update & handle shop items
        for item in shop_items:
            item["button"].update(events)
            if item["button"].was_clicked():
                if game_state["score"] >= item["cost"]:
                    game_state["score"] -= item["cost"]
                    item["effect"](game_state)
                    cant_afford_message.set_content(f"Purchased: {item['name']}")
                    cant_afford_message.set_color((100, 255, 100))
                else:
                    cant_afford_message.set_content(f"Not enough points! Need {item['cost']}")
                    cant_afford_message.set_color((255, 100, 100))
        
        # Draw UI elements
        for element in shop_elements:
            element.draw(screen)
        for item in shop_items:
            item["button"].draw(screen)
            
    # -------------------------
    # Settings Screen
    # -------------------------
    elif current_screen == "settings":
        # Update UI elements
        for element in settings_elements:
            element.update(events)
        
        # Handle back button
        if settings_back_button.was_clicked():
            current_screen = "main"
            
        # Handle theme selection
        selected_theme = theme_dropdown.get_selected_option()
        if selected_theme in theme_colors:
            game_state["background_color"] = theme_colors[selected_theme]
            
        # Handle reset button
        if reset_button.was_clicked():
            showing_reset_confirm = True
            
        # Draw UI elements
        for element in settings_elements:
            element.draw(screen)
        
        # Handle reset confirmation dialog
        if showing_reset_confirm:
            handle_reset_confirmation(events)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()