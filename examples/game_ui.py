import pygame
import sys
import pygameui
import random

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("PyGameUI Game Interface Example")

# Define colors
BG_COLOR = (15, 20, 30)
PANEL_COLOR = (30, 35, 45)
DARK_PANEL = (25, 25, 35)
ACCENT_COLOR = (86, 140, 235)
ACCENT_HOVER = (120, 170, 255)
TEXT_COLOR = (230, 230, 240)
HEALTH_COLOR = (235, 86, 86)
MANA_COLOR = (86, 110, 235)
XP_COLOR = (86, 235, 120)
GOLD_COLOR = (235, 200, 86)

# Game state
health = 75
max_health = 100
mana = 50
max_mana = 100
experience = 35
max_experience = 100
gold = 1250
player_name = "Hero"
level = 5

# Create UI elements
# Main game panel (simulating game window)
game_panel = pygameui.Element((400, 250), 780, 390, DARK_PANEL, border_radius=10, centered=True)
game_title = pygameui.Text((400, 250), "GAME AREA", (100, 100, 130), font_size=72, centered=True)

# Top bar - player info
top_panel = pygameui.Element((400, 20), 780, 50, PANEL_COLOR, border_radius=8, centered=True)
player_name_text = pygameui.Text((70, 20), player_name, TEXT_COLOR, font_size=22, centered=True)
level_text = pygameui.Text((140, 20), f"Level {level}", GOLD_COLOR, font_size=20, centered=True)
gold_text = pygameui.Text((700, 20), f"Gold: {gold}", GOLD_COLOR, font_size=20, centered=True)

# Bottom bar - health, mana, experience
bottom_panel = pygameui.Element((400, 570), 780, 70, PANEL_COLOR, border_radius=8, centered=True)

# Health bar
health_label = pygameui.Text((70, 550), "HP", TEXT_COLOR, font_size=18, centered=True)
health_bg = pygameui.Element((200, 550), 200, 20, (60, 40, 40), centered=True)
health_bar = pygameui.Element((200 - (200-(health/max_health*200))/2, 550), health/max_health*200, 20, HEALTH_COLOR, centered=True)
health_text = pygameui.Text((200, 570), f"{health}/{max_health}", TEXT_COLOR, font_size=14, centered=True)

# Mana bar
mana_label = pygameui.Text((350, 550), "MP", TEXT_COLOR, font_size=18, centered=True)
mana_bg = pygameui.Element((480, 550), 200, 20, (40, 40, 60), centered=True)
mana_bar = pygameui.Element((480 - (200-(mana/max_mana*200))/2, 550), mana/max_mana*200, 20, MANA_COLOR, centered=True)
mana_text = pygameui.Text((480, 570), f"{mana}/{max_mana}", TEXT_COLOR, font_size=14, centered=True)

# Experience bar
xp_bg = pygameui.Element((400, 595), 600, 15, (40, 60, 40), centered=True)
xp_bar = pygameui.Element((400 - (600-(experience/max_experience*600))/2, 595), experience/max_experience*600, 15, XP_COLOR, centered=True)
xp_text = pygameui.Text((730, 595), f"XP: {experience}/{max_experience}", TEXT_COLOR, font_size=14, centered=True)

# Action buttons
attack_btn = pygameui.Button((690, 550), 120, 40, 5, "Attack", HEALTH_COLOR, (255, 100, 100), text_color=TEXT_COLOR, centered=True)
spell_btn = pygameui.Button((690, 500), 120, 40, 5, "Spell", MANA_COLOR, (100, 140, 255), text_color=TEXT_COLOR, centered=True)
item_btn = pygameui.Button((560, 550), 120, 40, 5, "Item", GOLD_COLOR, (255, 220, 100), text_color=TEXT_COLOR, centered=True)
run_btn = pygameui.Button((560, 500), 120, 40, 5, "Run", (150, 150, 150), (200, 200, 200), text_color=TEXT_COLOR, centered=True)

# Action log
log_panel = pygameui.Element((110, 500), 200, 140, DARK_PANEL, border_radius=5, centered=True)
log_title = pygameui.Text((110, 445), "Combat Log", TEXT_COLOR, font_size=16, centered=True)
log_entry1 = pygameui.Text((110, 470), "Battle started", TEXT_COLOR, font_size=12, centered=True)
log_entry2 = pygameui.Text((110, 490), "Enemy appeared", TEXT_COLOR, font_size=12, centered=True)
log_entry3 = pygameui.Text((110, 510), "Waiting for action...", TEXT_COLOR, font_size=12, centered=True)

# Group all elements
elements = [
    game_panel, game_title,
    top_panel, player_name_text, level_text, gold_text,
    bottom_panel, 
    health_label, health_bg, health_bar, health_text,
    mana_label, mana_bg, mana_bar, mana_text,
    xp_bg, xp_bar, xp_text,
    attack_btn, spell_btn, item_btn, run_btn,
    log_panel, log_title, log_entry1, log_entry2, log_entry3
]

# Action functions
def perform_attack():
    global health, mana, gold, experience
    
    # Update combat log
    log_entry3.change_text(log_entry2._content)
    log_entry2.change_text(log_entry1._content)
    log_entry1.change_text("You attack! Damage dealt!")
    
    # Simulate battle effects
    health -= random.randint(5, 15)
    health = max(0, health)
    mana += random.randint(5, 10)
    mana = min(mana, max_mana)
    experience += random.randint(3, 8)
    gold += random.randint(10, 30)
    
    # Update UI
    update_stats()

def cast_spell():
    global health, mana, gold, experience
    
    if mana < 15:
        log_entry3.change_text(log_entry2._content)
        log_entry2.change_text(log_entry1._content)
        log_entry1.change_text("Not enough mana!")
        return
    
    # Update combat log
    log_entry3.change_text(log_entry2._content)
    log_entry2.change_text(log_entry1._content)
    log_entry1.change_text("You cast a spell! Critical hit!")
    
    # Simulate battle effects
    health += random.randint(5, 15)
    health = min(health, max_health)
    mana -= random.randint(10, 20)
    mana = max(0, mana)
    experience += random.randint(5, 12)
    gold += random.randint(15, 40)
    
    # Update UI
    update_stats()

def use_item():
    global health, mana, gold
    
    if gold < 50:
        log_entry3.change_text(log_entry2._content)
        log_entry2.change_text(log_entry1._content)
        log_entry1.change_text("Not enough gold!")
        return
    
    # Update combat log
    log_entry3.change_text(log_entry2._content)
    log_entry2.change_text(log_entry1._content)
    log_entry1.change_text("You used a health potion!")
    
    # Simulate item use
    health += random.randint(20, 35)
    health = min(health, max_health)
    gold -= 50
    
    # Update UI
    update_stats()

def attempt_run():
    # Update combat log
    log_entry3.change_text(log_entry2._content)
    log_entry2.change_text(log_entry1._content)
    
    if random.random() > 0.5:
        log_entry1.change_text("You escaped successfully!")
    else:
        log_entry1.change_text("Failed to escape!")
        # Take damage for trying to run
        global health
        health -= random.randint(10, 20)
        health = max(0, health)
        update_stats()

def update_stats():
    # Update text elements
    health_text.change_text(f"{health}/{max_health}")
    mana_text.change_text(f"{mana}/{max_mana}")
    xp_text.change_text(f"XP: {experience}/{max_experience}")
    gold_text.change_text(f"Gold: {gold}")
    
    # Update bar elements - adjust width and position
    health_bar._rect.width = (health/max_health) * 200
    health_bar._rect.centerx = 200 - (200-(health/max_health*200))/2
    
    mana_bar._rect.width = (mana/max_mana) * 200
    mana_bar._rect.centerx = 480 - (200-(mana/max_mana*200))/2
    
    xp_bar._rect.width = (experience/max_experience) * 600
    xp_bar._rect.centerx = 400 - (600-(experience/max_experience*600))/2

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
            if attack_btn.is_hovered():
                perform_attack()
            elif spell_btn.is_hovered():
                cast_spell()
            elif item_btn.is_hovered():
                use_item()
            elif run_btn.is_hovered():
                attempt_run()
    
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
