# CustomMenu
CustomMenu is a Python class that generates a customizable text-based menu for user input. It allows you to create a menu with a list of options and presents it to the user in a neat, formatted way. The user can then select a choice by entering the corresponding index.

## Features
- Customizable Menu Name: Set a custom name for the menu.
- Dynamic Choices: You can pass any number of options for the user to choose from.
- Formatted Output: The menu is displayed with centered headers, properly aligned choices, and bordered by `~` characters for better readability.
- User Input Handling: Allows users to select an option by entering its index, and validates the input.

## Technologies Used
- Python: The entire implementation is written in Python 3.x.

## Installation
This project doesn't have external dependencies, so no installation is required. Simply clone or download the repository, and you're good to go!
1. Clone the repository:
`git clone https://github.com/yourusername/CustomMenu.git`
3. Navigate to the project directory:
`cd CustomMenu`
5. Use the CustomMenu class in your code:
```python
from custom_menu import CustomMenu

# Initialize the menu with custom options
menu = CustomMenu(name="Main Menu", choices=["Start", "Settings", "Exit"])

# Display the menu and get the user's choice
user_choice = menu.ask()

if user_choice:
    print(f"You selected: {user_choice}")
else:
    print("Invalid choice.")
`
```

## Class Methods
```__init__(self, name="Menu", choices: list=["Yes", "No"])```
Initializes the `CustomMenu` instance with a given `name` and a list of `choices`. The default name is "Menu", and the default choices are "Yes" and "No".
Parameters:
- `name` (str): The name of the menu (default: "Menu").
- `choices` (list): A list of strings representing the available options (default: `["Yes", "No"]`).
```__str__(self)```
Generates a string representation of the menu, which includes the header, choices, and a bottom border. It automatically adjusts the alignment to create a neat output.
```max_length_needed(self)```
Calculates the maximum length required to align the choices and the menu name properly.
```ask(self)```
Displays the menu to the user, waits for input, and returns the selected choice based on the index input by the user. If an invalid index is entered, it returns `None`.

## Example Usage
```python
from custom_menu import CustomMenu

# Define a custom menu
menu = CustomMenu(name="Options", choices=["Play Game", "Settings", "Exit"])

# Ask user for input
selected_option = menu.ask()

# Handle the user's choice
if selected_option:
    print(f"You selected: {selected_option}")
else:
    print("Invalid choice. Please try again.")
```

## Contributing
Feel free to fork this repository and submit pull requests for improvements or bug fixes. If you have suggestions or find any issues, please open an issue in the repository.

## License
This project is open source and available under the MIT License.

## Acknowledgments
- This project was developed as a simple way to create customizable text-based menus in Python. Thanks to the Python community for continuous learning and support!
