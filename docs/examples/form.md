# Input Form Example

This example demonstrates how to create a complete registration form with validation using PygameUI.

## Features Demonstrated

- Creating and styling input fields
- Form validation
- Checkboxes for agreement confirmation
- Dynamic button states (enabled/disabled)
- Error messaging

## Code Walkthrough

### Form Fields

The example creates a structured form with multiple input fields:

```python
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
    # Additional fields for email and age
}

# Set filter for age field to only allow numbers
fields["age"]["input"].set_filter("0123456789", only_allow_filter=True)
fields["age"]["input"].set_max_length(3)  # Max 3 digits for age
```

### Agreement Checkbox

The form includes a checkbox for accepting terms and conditions:

```python
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
```

### Form Validation

The example implements comprehensive form validation:

```python
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
```

### Conditional Button States

The submit button's appearance changes based on the checkbox state:

```python
# Determine which submit button to show based on checkbox state
active_submit = submit_button if agreement_checkbox.is_checked() else submit_button_disabled
active_submit.update(events)
```

### Form Submission

The form processes the submission and displays success or error messages:

```python
# Handle submit button click
if submit_button.was_clicked() and agreement_checkbox.is_checked():
    validation_error = validate_form()
    
    if validation_error:
        status_message.set_content(validation_error)
        status_message.set_color((255, 100, 100))  # Red for error
    else:
        status_message.set_content("Form submitted successfully!")
        status_message.set_color((100, 255, 100))  # Green for success
```

## Form Design Best Practices

This example demonstrates several form design best practices:

1. **Clear Labels**: Each input has a descriptive label
2. **Input Validation**: Validates both presence and format of inputs
3. **Field Constraints**: Restricts age field to numbers only
4. **Visual Feedback**: Shows errors in red, success in green
5. **Disabled States**: Submit button appears disabled until agreement is checked
6. **Consistent Styling**: Maintains consistent colors and spacing

## Full Example Code

See the complete [input_form_example.py](https://github.com/trymbf/pygameui/blob/main/examples/input_form_example.py) file in the examples directory.

```python
# See full implementation in examples/input_form_example.py
```