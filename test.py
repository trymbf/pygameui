import pygame
import pygameui
import os
import sys

# Initialize pygame
pygame.init()

# Create window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PygameUI Test")
clock = pygame.time.Clock()
FPS = 60

# Background color
BG_COLOR = (30, 30, 30)

# Test control variables
current_test = 0
test_names = ["Basic UI", "Element Setters/Getters", "Text Setters/Getters", "Input Features", "Image Features"]
test_change_cooldown = 0

# Create UI elements
def create_ui_elements():
    ui_elements = {}
    
    # Basic Element
    ui_elements["basic_element"] = pygameui.Element(
        position=(100, 50),
        width=100,
        height=50,
        color=(255, 0, 0),
        border_radius=10
    )
    
    # Text
    ui_elements["title"] = pygameui.Text(
        position=(WIDTH // 2, 30),
        content="PygameUI Test Demo",
        color=(255, 255, 255),
        font_size=30,
        centered=True
    )
    
    ui_elements["description"] = pygameui.Text(
        position=(WIDTH // 2, 70),
        content="Testing all components and features",
        color=(200, 200, 200),
        font_size=18,
        centered=True
    )
    
    # Button
    ui_elements["button"] = pygameui.Button(
        position=(400, 150),
        width=200,
        height=50,
        label="Click Me!",
        color=(100, 100, 255),
        hover_color=(150, 150, 255),
        click_color=(50, 50, 200),
        text_color=(255, 255, 255),
        text_hover_color=(255, 255, 255),
        text_click_color=(200, 200, 200),
        centered=True
    )
    
    # Moving element
    ui_elements["moving_element"] = pygameui.Element(
        position=(50, 250),
        width=80,
        height=40,
        color=(0, 255, 0),
        border_radius=20
    )
    
    # Jumping element
    ui_elements["jumping_element"] = pygameui.Element(
        position=(50, 350),
        width=80,
        height=40,
        color=(255, 255, 0),
        border_radius=5
    )
    
    # Input
    ui_elements["input"] = pygameui.Input(
        position=(400, 250),
        width=300,
        height=40,
        hint="Type something...",
        font_size=18,
        border_radius=5,
        centered=True
    )
    
    # Image (create a placeholder image if needed)
    placeholder_img_path = create_placeholder_image()
    if placeholder_img_path:
        ui_elements["image"] = pygameui.Image(
            position=(650, 150),
            image_path=placeholder_img_path,
            width=100,
            height=100,
            centered=True
        )
    
    # Status text
    ui_elements["status"] = pygameui.Text(
        position=(400, 450),
        content="Hover or click on elements to see interactions",
        color=(180, 180, 180),
        font_size=16,
        centered=True
    )
    
    # Set up movement for the moving element
    ui_elements["moving_element"].flow(
        start_position=(50, 250),
        end_position=(300, 250),
        time=2000,
        loop=True
    )
    
    # Set up jumping for the jumping element
    ui_elements["jumping_element"].jump(
        start_position=(50, 350),
        end_position=(300, 350),
        time=1500,
        loop=True
    )
    
    # Test Elements (for testing setters/getters)
    ui_elements["test_info"] = pygameui.Text(
        position=(WIDTH // 2, 520),
        content=f"Test: {test_names[current_test]} (Press Left/Right to navigate tests)",
        color=(255, 255, 255),
        font_size=16,
        centered=True
    )
    
    # Element Setters/Getters Test
    ui_elements["element_test"] = pygameui.Element(
        position=(150, 200),
        width=120,
        height=60,
        color=(100, 200, 150),
        border_radius=5
    )
    
    # Text Setters/Getters Test
    ui_elements["text_test"] = pygameui.Text(
        position=(400, 350),
        content="Text Test",
        color=(255, 200, 100),
        font_size=22,
        centered=True
    )
    
    # Second test image for testing setters
    ui_elements["test_image"] = pygameui.Image(
        position=(600, 350),
        image_path=placeholder_img_path,
        width=80,
        height=80,
        centered=True
    )
    
    # Input with filter test
    ui_elements["filtered_input"] = pygameui.Input(
        position=(WIDTH // 2, 400),
        width=300,
        height=40,
        hint="Numbers only...",
        font_size=18,
        border_radius=5,
        centered=True
    )
    # Set a filter for numbers only
    ui_elements["filtered_input"].set_filter("0123456789", False)
    
    return ui_elements

def create_placeholder_image():
    """Create a simple placeholder image for testing"""
    try:
        img_path = os.path.join(os.path.dirname(__file__), "test_image.png")
        # Create a simple surface
        surf = pygame.Surface((100, 100))
        surf.fill((100, 100, 100))
        pygame.draw.circle(surf, (255, 0, 0), (50, 50), 40)
        pygame.draw.rect(surf, (0, 0, 255), (20, 20, 60, 60), 5)
        pygame.image.save(surf, img_path)
        
        # Also create a second test image
        img_path2 = os.path.join(os.path.dirname(__file__), "test_image2.png")
        surf2 = pygame.Surface((100, 100))
        surf2.fill((0, 0, 100))
        pygame.draw.circle(surf2, (0, 255, 0), (50, 50), 40)
        pygame.image.save(surf2, img_path2)
        
        return img_path
    except Exception as e:
        print(f"Could not create placeholder image: {e}")
        return None

def handle_button_click(button, status_text):
    if button.was_clicked():
        status_text.set_content("Button was clicked!")
        status_text.set_color((0, 255, 0))

def run_element_tests(elements, elapsed_time):
    """Test Element class setters and getters"""
    test_element = elements["element_test"]
    
    # Set visibility based on test mode
    test_element.set_display(current_test == 1)
    if current_test != 1:
        return
    
    # Test element setters with time-based changes
    cycle = (elapsed_time // 1000) % 8
    
    if cycle == 0:
        test_element.set_position((150, 200))
        test_element.set_color((100, 200, 150))
        elements["status"].set_content("Element: Default state")
    elif cycle == 1:
        test_element.set_position((250, 200))
        elements["status"].set_content("Element: set_position()")
    elif cycle == 2:
        test_element.set_color((200, 100, 150))
        elements["status"].set_content("Element: set_color()")
    elif cycle == 3:
        test_element.set_border_radius(20)
        elements["status"].set_content("Element: set_border_radius()")
    elif cycle == 5:
        position = test_element.get_position()
        elements["status"].set_content(f"Element: get_position() = {position}")
    elif cycle == 6:
        test_element.toggle_display()
        elements["status"].set_content("Element: toggle_display()")
    elif cycle == 7:
        test_element.toggle_display()
        test_element.set_border_radius(5)
        elements["status"].set_content("Element: Reset to default")

def run_text_tests(elements, elapsed_time):
    """Test Text class setters and getters"""
    test_text = elements["text_test"]
    
    # Set visibility based on test mode
    test_text.set_display(current_test == 2)
    if current_test != 2:
        return
    
    # Test text setters with time-based changes
    cycle = (elapsed_time // 1000) % 6
    
    if cycle == 0:
        test_text.set_content("Text Test")
        test_text.set_color((255, 200, 100))
        test_text.set_font_size(22)
        test_text.set_font_family("Arial")
        elements["status"].set_content("Text: Default state")
    elif cycle == 1:
        test_text.set_content("Changed Text")
        elements["status"].set_content("Text: set_content()")
    elif cycle == 2:
        test_text.set_color((100, 255, 200))
        elements["status"].set_content("Text: set_color()")
    elif cycle == 3:
        test_text.set_font_size(28)
        elements["status"].set_content("Text: set_font_size()")
    elif cycle == 4:
        test_text.set_font_family("Impact")
        elements["status"].set_content("Text: set_font_family()")

def run_input_tests(elements, elapsed_time):
    """Test Input class features"""
    test_input = elements["filtered_input"]
    
    # Set visibility based on test mode
    test_input.set_display(current_test == 3)
    if current_test != 3:
        return
    
    elements["status"].set_content("Input: Try typing - only numbers allowed due to set_filter()")

def run_image_tests(elements, elapsed_time):
    """Test Image class setters and getters"""
    test_image = elements["test_image"]
    
    # Set visibility based on test mode
    test_image.set_display(current_test == 4)
    if current_test != 4:
        return
    
    # Test image setters with time-based changes
    cycle = (elapsed_time // 1500) % 4
    
    if cycle == 0:
        elements["status"].set_content("Image: Default state")
    elif cycle == 1:
        # Get the second test image path
        img_path2 = os.path.join(os.path.dirname(__file__), "test_image2.png")
        if os.path.exists(img_path2):
            test_image.set_image(img_path2)
            elements["status"].set_content("Image: set_image()")
    elif cycle == 2:
        if test_image.get_scale() == 1:
            test_image.scale(1.5)
        elements["status"].set_content("Image: set_scale()")
    elif cycle == 3:
        # Reset to original state
        img_path = os.path.join(os.path.dirname(__file__), "test_image.png")
        if os.path.exists(img_path):
            test_image.set_image(img_path)
            test_image.scale(1)
            elements["status"].set_content("Image: Reset to default")

def handle_test_navigation(events):
    """Handle keyboard inputs for test navigation"""
    global current_test, test_change_cooldown
    
    if test_change_cooldown > 0:
        test_change_cooldown -= 1
        return
    
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_test = (current_test + 1) % len(test_names)
                test_change_cooldown = 20  # Prevent rapid switching
            elif event.key == pygame.K_LEFT:
                current_test = (current_test - 1) % len(test_names)
                test_change_cooldown = 20  # Prevent rapid switching

def main():
    ui_elements = create_ui_elements()
    running = True
    start_time = pygame.time.get_ticks()
    
    # Main game loop
    while running:
        elapsed_time = pygame.time.get_ticks() - start_time
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
        
        # Handle test navigation
        handle_test_navigation(events)
        
        # Update test info
        ui_elements["test_info"].set_content(f"Test: {test_names[current_test]} (Press Left/Right to navigate tests)")
        
        # Clear screen
        screen.fill(BG_COLOR)
        
        # Run specific tests based on current_test
        run_element_tests(ui_elements, elapsed_time)
        run_text_tests(ui_elements, elapsed_time)
        run_input_tests(ui_elements, elapsed_time)
        run_image_tests(ui_elements, elapsed_time)
        
        # Only show basic UI elements in the first test
        for key in ["basic_element", "button", "moving_element", "jumping_element", "input", "image"]:
            if key in ui_elements:
                ui_elements[key].set_display(current_test == 0)
        
        # Update all UI elements
        for element in ui_elements.values():
            if isinstance(element, pygameui.Input):
                element.update(events)
            else:
                element.update()
        
        # Handle button interaction (only in first test)
        if current_test == 0:
            if "button" in ui_elements and "status" in ui_elements:
                handle_button_click(ui_elements["button"], ui_elements["status"])
            
            # Update status based on hover
            if "button" in ui_elements and "status" in ui_elements:
                if ui_elements["button"].is_hovered():
                    ui_elements["status"].set_content("Button is hovered!")
                    ui_elements["status"].set_color((255, 255, 0))
            
            # Display input value
            if "input" in ui_elements and "status" in ui_elements:
                if ui_elements["input"].active:
                    ui_elements["status"].set_content(f"Input: {ui_elements['input'].get_value()}")
                    ui_elements["status"].set_color((0, 200, 255))
        
        # Draw all UI elements
        for element in ui_elements.values():
            element.draw(screen)
        
        # Update the display
        pygame.display.flip()
        clock.tick(FPS)
    
    # Clean up
    pygame.quit()
    
    # Remove test images if they were created
    try:
        os.remove(os.path.join(os.path.dirname(__file__), "test_image.png"))
        os.remove(os.path.join(os.path.dirname(__file__), "test_image2.png"))
    except:
        pass

if __name__ == "__main__":
    main()