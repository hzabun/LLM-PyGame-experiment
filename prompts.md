# Main file prompt

### Text
mainFilePromptText = """Write Pygame code in an object oriented way to create a simple main file for a fantasy RPG game.
The main file will be used as controller for the whole game.
The main file has the following states: 'initialized', 'main_menu' and 'quitting'.
The main file will loop forever and decide which module of the game gets control depending on the state.
The main file creates a basic PyGame screen and instantiates the class 'Menu' with that screen. If the state of the main file is 'main_menu', the main file will pass control to the 'menu.py' file."""

### Prompt

mainFilePrompt = "Write Pygame code in an object oriented way to create a simple main file for a fantasy RPG game. The main file will be used as controller for the whole game. The main file has the following states: 'initialized', 'main_menu' and 'quitting'. The main file will loop forever and decide which module of the game gets control depending on the state. The main file creates a basic PyGame screen and imports from a 'menu.py' file. If the state of the main file is 'main_menu', it will pass the screen to 'menu.py' and run the loop in 'menu.py'. \n"

# Menu prompt

### Textv1
menuPromptText = """Write PyGame code to create a simple menu file called 'menu.py' in an object oriented way for a game.
The game is controlled by another file, which instantiates the menu file.
The menu file receives a blank screen object from another file.
The menu screen will have 3 selectable fields, namely 'Start Game', 'Option' and 'Quit'.
The background image for the menu screen is located in the following path: 'assets/images/background.png'. \n"""

### Promptv1
menuPrompt = "Write PyGame code to create a simple menu file called 'menu.py' in an object oriented way for a game. The game is controlled by a file called 'main.py', which instantiates the menu file. The menu file receives from 'main.py' a blank screen object. The menu screen will have 3 selectable fields, namely 'Start Game', 'Option' and 'Quit'. The background image for the menu screen is located in the following path: 'assets/images/background.bmp'. \n"

### Textv2
menuPromptv2Text = """Write PyGame code to create a simple menu file called 'menu.py' in an object oriented way for a game.
The game is controlled by another file, which instantiates the menu file. Implement only the menu file.
The menu file receives a blank screen object from another file.
The menu screen will have 3 selectable fields, namely 'Start Game', 'Option' and 'Quit'. Add functionality to navigate the menu.
The background image for the menu screen is located in the following path: 'assets/images/background.png'. \n"""

### Promptv2
menuPromptv2 = "Write PyGame code to create a simple menu file called 'menu.py' in an object oriented way for a game. The game is controlled by another file, which instantiates the menu file. Implement only the menu file. The menu file receives a blank screen object from another file. The menu screen will have 3 selectable fields, namely 'Start Game', 'Option' and 'Quit'. Add functionality to navigate the menu. The background image for the menu screen is located in the following path: 'assets/images/background.bmp'. \n"

### Textv3
menuPromptv3Text = """Write PyGame code to create a simple menu file called 'menu.py' in an object oriented way for a game.
The game is controlled by another file, which instantiates the menu file. Implement ONLY the menu file.
The menu file receives a blank screen object from another file.
The menu screen will have 3 selectable fields, namely 'Start Game', 'Option' and 'Quit'. Add functionality to navigate the menu by accessing the keyboard strokes from the user.
The background image for the menu screen is located in the following path: 'assets/images/background.png'. \n"""

### Promptv3
menuPromptv3 = "Write PyGame code to create a simple menu file called 'menu.py' in an object oriented way for a game. The game is controlled by another file, which instantiates the menu file. Implement ONLY the menu file. The menu file receives a blank screen object from another file. The menu screen will have 3 selectable fields, namely 'Start Game', 'Option' and 'Quit'. Add functionality to navigate the menu by accessing the keyboard strokes from the user. The background image for the menu screen is located in the following path: 'assets/images/background.bmp'. \n"

### Textv4
menuPromptv4Text = """Write PyGame code to create a simple menu file called 'menu.py' in an object oriented way for a game.
The game is controlled by another file, which instantiates the menu file. Implement ONLY the menu file.
The menu file receives a blank screen object from another file.
The menu screen will have 3 selectable options, namely 'Start Game', 'Option' and 'Quit'. 
Run the menu screen in a loop which never stops, until one of the options is clicked on.
Add within the menu file the functionality to navigate the menu by accessing the keyboard strokes from the user.
The background image for the menu screen is located in the following path: 'assets/images/background.png'. \n"""

### Promptv4
menuPromptv4 = "Write PyGame code to create a simple menu file called 'menu.py' in an object oriented way for a game. The game is controlled by another file, which instantiates the menu file. Implement ONLY the menu file. The menu file receives a blank screen object from another file. The menu screen will have 3 selectable options, namely 'Start Game', 'Option' and 'Quit'.  Run the menu screen in a loop which never stops, until one of the options is clicked on. Add within the menu file the functionality to navigate the menu by accessing the keyboard strokes from the user. The background image for the menu screen is located in the following path: 'assets/images/background.bmp'. \n"

### Textv5
menuPromptv5Text = """Write PyGame code to create a simple menu file called 'menu.py' in an object oriented way for a game.
The game is already initialized by another file. Implement ONLY the menu file.
The menu file gets instantiated by another file and receives a blank screen object.
The menu screen will have 3 selectable options, namely 'Start Game', 'Option' and 'Quit'. 
Implement a method called 'run' which loops forever, until one of the options is clicked on.
Add within the menu file the functionality to navigate the menu by accessing the keyboard strokes from the user.
The background image for the menu screen is located in the following path: 'assets/images/background.png'. \n"""

### Promptv5
menuPromptv5 = "Write PyGame code to create a simple menu file called 'menu.py' in an object oriented way for a game. The game is already initialized by another file. Implement ONLY the menu file. The menu file gets instantiated by another file and receives a blank screen object. The menu screen will have 3 selectable options, namely 'Start Game', 'Option' and 'Quit'.  Implement a method called 'run' which loops forever, until one of the options is clicked on. Add within the menu file the functionality to navigate the menu by accessing the keyboard strokes from the user. The background image for the menu screen is located in the following path: 'assets/images/background.bmp'. \n"

