import pygame
import pygameui

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create form UI elements
title = pygameui.Text(
    position=(400, 60),
    content="Registration Form",
    color=(255, 255, 255),
    font_size=36,
    centered=True
)

# Form fields
fields = {
    "name": {
        "label": pygameui.Text(
            position=(250, 150),
            content="Name:",
            color=(220, 220, 220),
            font_size=20,
            centered=True
        ),
        "input": pygameui.Input(
            position=(500, 150),
            width=300,
            height=40,
            hint="Enter your name",
            passive_text_color=(150, 150, 150),
            active_text_color=(255, 255, 255),
            passive_border_color=(100, 100, 100),
            active_border_color=(150, 150, 255),
            border_radius=5,
            centered=True
        )
    },
    "email": {
        "label": pygameui.Text(
            position=(250, 220),
            content="Email:",
            color=(220, 220, 220),
            font_size=20,
            centered=True
        ),
        "input": pygameui.Input(
            position=(500, 220),
            width=300,
            height=40,
            hint="Enter your email",
            passive_text_color=(150, 150, 150),
            active_text_color=(255, 255, 255),
            passive_border_color=(100, 100, 100),
            active_border_color=(150, 150, 255),
            border_radius=5,
            centered=True
        )
    },
    "age": {
        "label": pygameui.Text(
            position=(250, 290),
            content="Age:",
            color=(220, 220, 220),
            font_size=20,
            centered=True
        ),
        "input": pygameui.Input(
            position=(500, 290),
            width=300,
            height=40,
            hint="Enter your age (numbers only)",
            passive_text_color=(150, 150, 150),
            active_text_color=(255, 255, 255),
            passive_border_color=(100, 100, 100),
            active_border_color=(150, 150, 255),
            border_radius=5,
            centered=True
        )
    }
}

# Set filter for age field to only allow numbers
fields["age"]["input"].set_filter("0123456789", only_allow_filter=True)
fields["age"]["input"].set_max_length(3)  # Max 3 digits for age

# Agreement checkbox
agreement_checkbox = pygameui.Checkbox(
    position=(250, 360),
    width=30,
    height=30,
    style="checkmark",
    color=(150, 255, 150),
    background_color=(40, 40, 40),
    border_color=(200, 200, 200),
    border_width=1
)

agreement_text = pygameui.Text(
    position=(500, 360),
    content="I agree to the terms and conditions",
    color=(220, 220, 220),
    font_size=20
)

# Submit button
submit_button = pygameui.Button(
    position=(400, 430),
    label="Submit",
    width=200,
    height=50,
    color=(75, 185, 75),
    hover_color=(85, 205, 85),
    click_color=(65, 165, 65),
    text_color=(255, 255, 255),
    border_radius=8,
    centered=True
)

submit_button_disabled = pygameui.Button(
    position=(400, 430),
    label="Submit",
    width=200,
    height=50,
    color=(100, 100, 100),
    hover_color=(100, 100, 100),
    click_color=(100, 100, 100),
    text_color=(150, 150, 150),
    border_radius=8,
    centered=True
)

# Status message
status_message = pygameui.Text(
    position=(400, 500),
    content="",
    color=(255, 255, 255),
    font_size=16,
    centered=True
)

# Validate form function
def validate_form():
    if not fields["name"]["input"].get_value():
        return "Please enter your name"
    
    if not fields["email"]["input"].get_value():
        return "Please enter your email"
    
    if "@" not in fields["email"]["input"].get_value():
        return "Please enter a valid email address"
    
    if not fields["age"]["input"].get_value():
        return "Please enter your age"
    
    if not agreement_checkbox.is_checked():
        return "Please agree to the terms and conditions"
    
    return None  # No errors

# Main loop
running = True
while running:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Reset screen
    screen.fill((30, 30, 30))  # Dark background
    
    # Update UI elements
    title.update(events)
    
    for field in fields.values():
        field["label"].update(events)
        field["input"].update(events)
    
    agreement_checkbox.update(events)
    agreement_text.update(events)
    
    # Determine which submit button to show based on checkbox state
    active_submit = submit_button if agreement_checkbox.is_checked() else submit_button_disabled
    active_submit.update(events)
    
    status_message.update(events)

    # Handle submit button click
    if submit_button.was_clicked() and agreement_checkbox.is_checked():
        validation_error = validate_form()
        
        if validation_error:
            status_message.set_content(validation_error)
            status_message.set_color((255, 100, 100))  # Red for error
        else:
            status_message.set_content("Form submitted successfully!")
            status_message.set_color((100, 255, 100))  # Green for success
    
    # Draw UI elements
    title.draw(screen)
    
    for field in fields.values():
        field["label"].draw(screen)
        field["input"].draw(screen)
    
    agreement_checkbox.draw(screen)
    agreement_text.draw(screen)
    active_submit.draw(screen)
    status_message.draw(screen)

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Quit pygame
pygame.quit()