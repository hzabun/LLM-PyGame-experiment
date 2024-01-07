# Main file prompt

## Beginning

### Text
mainFilePromptText = """Write Pygame code in an object oriented way to create a simple main file for a fantasy RPG game.
The main file will be used as controller for the whole game.
The main file has the following states: 'initialized', 'main_menu' and 'quitting'.
The main file will loop forever and decide which module of the game gets control depending on the state.
The main file creates a basic PyGame screen and instantiates the class 'Menu' with that screen. If the state of the main file is 'main_menu', the main file will pass control to the 'menu.py' file."""

### Prompt

mainFilePrompt = "Write Pygame code in an object oriented way to create a simple main file for a fantasy RPG game. The main file will be used as controller for the whole game. The main file has the following states: 'initialized', 'main_menu' and 'quitting'. The main file will loop forever and decide which module of the game gets control depending on the state. The main file creates a basic PyGame screen and imports from a 'menu.py' file. If the state of the main file is 'main_menu', it will pass the screen to 'menu.py' and run the loop in 'menu.py'. \n"

## Update with level.py and new window size

### Textv1
mainFilePromptText = """Write Pygame code in an object oriented way to create a simple main file for a game.
The main file will be used as controller for the whole game.
The main file has the following states: 'initialized', 'main_menu', 'level_generation' and 'quitting'.
The main file imports the following:
- from file 'menu' the class 'Menu'
- from file 'level' the class 'Level'.
The main file will loop forever and decide which module of the game gets control depending on the state.
The main file starts in the state 'initialized', then goes to 'main_menu' and then to 'level_generation'.
The main file creates a basic PyGame screen with resolutions 1200x800.
If in the state 'main_menu': instantiate the class 'Menu' with the screen object, run the method 'run()' in it and store what it returns in the variable 'menu_screen'.
If in the state 'level_generation': instantiate the class 'Level' with the 'menu_screen' object, run the method 'draw_platforms()' in it and store what it returns in the variable 'level_screen'. /n"""

### Promptv1
mainFilePromptText = "Write Pygame code in an object oriented way to create a simple main file for a game. The main file will be used as controller for the whole game. The main file has the following states: 'initialized', 'main_menu', 'level_generation' and 'quitting'. The main file imports the following:- from file 'menu' the class 'Menu'- from file 'level' the class 'Level'. The main file will loop forever and decide which module of the game gets control depending on the state. The main file starts in the state 'initialized', then goes to 'main_menu' and then to 'level_generation'. The main file creates a basic PyGame screen with resolutions 1200x800. If in the state 'main_menu': instantiate the class 'Menu' with the screen object, run the method 'run()' in it and store what it returns in the variable 'menu_screen'. If in the state 'level_generation': instantiate the class 'Level' with the 'menu_screen' object, run the method 'draw_platforms()' in it and store what it returns in the variable 'level_screen'. /n"

## Update with modified level.py, character.py and render.py

### Textv1
mainFilePromptTextv1 = """Write Pygame code in an object oriented way to create a simple main file for a game.
The main file will be used as controller for the whole game.
The main file has the following states: 'initialized', 'main_menu', 'level_generation', 'rendering' and 'quitting'.
The main file imports the following:
- from file 'menu' the class 'Menu'
- from file 'level' the class 'Level'
- from file 'character' the class 'Character'
- from file 'render' the class 'Render'.
The main file will loop forever and decide which module of the game gets control depending on the state.
The main file starts in the state 'initialized', then goes to 'main_menu', then goes to 'level_generation' and then to 'rendering'.
The main file creates a basic PyGame screen with resolutions 1200x800.
If in the state 'main_menu': instantiate the class 'Menu' with the screen object, run the method 'run()' in it and store what it returns in the variable 'menu_screen'.
If in the state 'level_generation': instantiate the class 'Level' with the 'menu_screen' object
If in the state 'rendering': first inantiate the class 'Character'. And then instantiate the class 'Render' with the following objects:
- level.screen
- level.platforms
- character
/n"""

### Promptv1
mainFilePromptv1 = "Write Pygame code in an object oriented way to create a simple main file for a game. The main file will be used as controller for the whole game. The main file has the following states: 'initialized', 'main_menu', 'level_generation', 'rendering' and 'quitting'. The main file imports the following: - from file 'menu' the class 'Menu' - from file 'level' the class 'Level' - from file 'character' the class 'Character' - from file 'render' the class 'Render'. The main file will loop forever and decide which module of the game gets control depending on the state. The main file starts in the state 'initialized', then goes to 'main_menu', then goes to 'level_generation' and then to 'rendering'. The main file creates a basic PyGame screen with resolutions 1200x800. If in the state 'main_menu': instantiate the class 'Menu' with the screen object, run the method 'run()' in it and store what it returns in the variable 'menu_screen'. If in the state 'level_generation': instantiate the class 'Level' with the 'menu_screen' object. If in the state 'rendering': first inantiate the class 'Character'. And then instantiate the class 'Render' with the following objects: - level.screen - level.platforms - character /n"

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

## Update with returning the screen object

### Textv1
menuPromptv1Text = """Write PyGame code to create a simple menu file called 'menu.py' in an object oriented way for a game.
The game is already initialized by another file. Implement ONLY the menu file.
The menu file gets instantiated by another file and receives a blank screen object.
The menu screen will have 3 selectable options, namely 'Start Game', 'Option' and 'Quit'. 
Implement a method called 'run' which loops forever, until one of the options is clicked on.
Add within the menu file the functionality to navigate the menu by accessing the keyboard strokes from the user.
If the user clicks on 'Start Game', return the screen object. If the user clicks on 'Quit', quit the program.
The background image for the menu screen is located in the following path: 'assets/images/background.png'. \n"""

### Promptv1
menuPromptv1Text = "Write PyGame code to create a simple menu file called 'menu.py' in an object oriented way for a game. The game is already initialized by another file. Implement ONLY the menu file. The menu file gets instantiated by another file and receives a blank screen object. The menu screen will have 3 selectable options, namely 'Start Game', 'Option' and 'Quit'. Implement a method called 'run' which loops forever, until one of the options is clicked on. Add within the menu file the functionality to navigate the menu by accessing the keyboard strokes from the user. If the user clicks on 'Start Game', return the screen object. If the user clicks on 'Quit', quit the program. The background image for the menu screen is located in the following path: 'assets/images/background.png'. \n"


# Level prompt  

### Textv1
levelPromptv1Text = """Write PyGame code to create a simple level file called 'level.py' in an object oriented way for a 2D game.  
The game is already initialized by another file. Implement ONLY the level file. Do not implement any other file.  
The level file gets instantiated by another file and receives a blank screen object.  
The level file generates a couple of platforms in the level.  
Once all the platforms are generated, the level file returns the whole screen back. \n"""  
      
### Prompt  
levelPromptv1 = "Write PyGame code to create a simple level file called 'level.py' in an object oriented way for a 2D game. The game is already initialized by another file. Implement ONLY the level file. Do not implement any other file. The level file gets instantiated by another file and receives a blank screen object. The level file generates a couple of platforms in the level. Once all the platforms are generated, the level file returns the whole screen back. \n"

### Textv1
levelPromptv2Text = """Write PyGame code to create a simple level file called 'level.py' in an object oriented way for a 2D game.  
The game is already initialized by another file. Implement ONLY the level file. Do not implement any other file.  
The level file gets instantiated by another file and receives a blank screen object. 
Keep the window size to 800x600.
The level file generates 4 different platforms.
Once all the platforms are generated, the level file returns the whole screen back. \n"""  
      
### Promptv2
levelPromptv2 = "Write PyGame code to create a simple level file called 'level.py' in an object oriented way for a 2D game. The game is already initialized by another file. Implement ONLY the level file. Do not implement any other file. Keep the window size to 800x600. The level file gets instantiated by another file and receives a blank screen object. The level file generates 4 platforms: - 1 on the left middle side of the screen - 1 on the middle bottom side of the screen - 1 on the middle top side of the screen - 1 on the right middle side of the screen  Once all the platforms are generated, the level file returns the whole screen back. \n"

### Textv2
levelPromptv3Text = """Write PyGame code to create a simple level file called 'level.py' in an object oriented way for a 2D game.  
The game is already initialized by another file. Implement ONLY the level file. Do not implement any other file.  
The level file gets instantiated by another file and receives a blank screen object. 
Keep the window size to 800x600.
The level file generates 4 different white colored platforms.
Once all the platforms are generated, the level file returns the whole screen back. \n"""

levelPromptv3 = "Write PyGame code to create a simple level file called 'level.py' in an object oriented way for a 2D game. The game is already initialized by another file. Implement ONLY the level file. Do not implement any other file. The level file gets instantiated by another file and receives a blank screen object.  Keep the window size to 800x600.  The level file generates 4 platforms: - 1 medium length on the left middle side of the screen - 1 large on the middle bottom side of the screen - 1 small on the middle top side of the screen - 1 medium length on the right middle side of the screen  Once all the platforms are generated, the level file returns the whole screen back. \n"

### Textv3
levelPromptv4Text = """Write PyGame code to create a simple level file called 'level.py' in an object oriented way for a 2D game.  
The game is already initialized by another file. Implement ONLY the level file. Do not implement any other file.  
The level file gets instantiated by another file and receives a blank screen object. 
Keep the window size to 1200x800.
The level file generates 4 platforms:
- 1 medium length on the left middle side of the screen
- 1 medium length on the right middle side of the screen
- 1 large on the middle bottom side of the screen
- 1 small on the middle upper side of the screen
Once all the platforms are generated, the level file returns the whole screen back. \n"""

### Promptv3
levelPromptv4 = "Write PyGame code to create a simple level file called 'level.py' in an object oriented way for a 2D game. The game is already initialized by another file. Implement ONLY the level file. Do not implement any other file. The level file gets instantiated by another file and receives a blank screen object.  Keep the window size to 1200x800.  The level file generates 4 platforms: - 1 medium length on the left middle side of the screen - 1 medium length on the right middle side of the screen - 1 large on the middle bottom side of the screen - 1 small on the middle upper side of the screen. Once all the platforms are generated, the level file returns the whole screen back. \n"

## Update with making screen blank before drawing

### Textv1
levelPromptv1Text = """Write PyGame code to create a simple level file called 'level.py' in an object oriented way for a 2D game.  
The game is already initialized by another file. Implement ONLY the level file. Do not implement any other file.  
The level file gets instantiated by another file and receives an already filled screen object.
Prepare the already filled screen object so that it's empty and can be drawn upon.
The level file generates 4 platforms:
- 1 medium length on the left middle side of the screen
- 1 medium length on the right middle side of the screen
- 1 large on the middle bottom side of the screen
- 1 small on the middle upper side of the screen
Make the 4 platforms properly fill a screen of size 1200x800.
Once all the platforms are generated, the level file returns the whole screen back. \n"""

### Promptv1
levelPromptv1 = "Write PyGame code to create a simple level file called 'level.py' in an object oriented way for a 2D game. The game is already initialized by another file. Implement ONLY the level file. Do not implement any other file. The level file gets instantiated by another file and receives an already filled screen object. Prepare the already filled screen object so that it's empty and can be drawn upon. The level file generates 4 platforms: - 1 medium length on the left middle side of the screen- 1 medium length on the right middle side of the screen - 1 large on the middle bottom side of the screen - 1 small on the middle upper side of the screen. Make the 4 platforms properly fill a screen of size 1200x800. Once all the platforms are generated, the level file returns the whole screen back. \n"


## Update with returning platforms as well

### Textv1
levelPromptv1Text = """Write PyGame code to create a simple level file called 'level.py' in an object oriented way for a 2D game.  
The game is already initialized by another class. Implement ONLY the level class. Do not implement any other class.  
The level class gets instantiated by another class and receives an already filled screen object.
Prepare the already filled screen object so that it's empty and can be drawn upon.
The level file generates 4 platforms:
- 1 medium length on the left middle side of the screen
- 1 medium length on the right middle side of the screen
- 1 large on the middle bottom side of the screen
- 1 small on the middle upper side of the screen
Make the 4 platforms properly fill a screen of size 1200x800.
Once all the platforms are generated, the level class returns the whole screen back as 'self.level.screen'
The level file also adds all the platforms to 'self.level.platforms'. \n"""

### Promptv1
levelPromptv1Text = "Write PyGame code to create a simple level file called 'level.py' in an object oriented way for a 2D game. The game is already initialized by another class. Implement ONLY the level class. Do not implement any other class. The level class gets instantiated by another class and receives an already filled screen object. Prepare the already filled screen object so that it's empty and can be drawn upon. The level file generates 4 platforms: - 1 medium length on the left middle side of the screen - 1 medium length on the right middle side of the screen - 1 large on the middle bottom side of the screen - 1 small on the middle upper side of the screen. Make the 4 platforms properly fill a screen of size 1200x800. Once all the platforms are generated, the level class returns the whole screen back as 'self.level.screen' The level file also adds all the platforms to 'self.level.platforms'. \n"


# Character prompt

### Textv1
characterPromptv1Text = """Write PyGame code to create a simple character file called 'character.py' in an object-oriented way for a 2D game.
The game is already initialized by another file. Implement ONLY the character file. Do not implement any other file.
The character has hit points which indicate its health. The character starts with 5 hit points.
The character also has a list of equipments, namely:
- A bow and arrow
- A shield
- A health potion
The image for the character can be found in the following locaiton: 'assets/images/character.bmp'. \n"""

### Promptv1
characterPromptv1 = "Write PyGame code to create a simple character file called 'character.py' in an object-oriented way for a 2D game. The game is already initialized by another file. Implement ONLY the character file. Do not implement any other file. The character has hit points which indicate its health. The character starts with 5 hit points. The character also has a list of equipments, namely: - A bow and arrow - A shield - A health potion. The image for the character can be found in the following locaiton: 'assets/images/character.bmp'. \n"


### Textv2
characterPromptv2Text = """Write PyGame code to create a simple character file called 'character.py' in an object-oriented way for a 2D game.
The game is already initialized by another file. Implement ONLY the character file. Do not implement any other file.
The character file gets instantiated by another file. Initialize the character file with only itself, nothing else.
The character has hit points which indicate its health. The character starts with 5 hit points.
The character also has a list of equipments, namely:
- A bow and arrow
- A shield
- A health potion
The image for the character can be found in the following locaiton: 'assets/images/character.bmp'. \n"""

### Promptv2
characterPromptv2 = "Write PyGame code to create a simple character file called 'character.py' in an object-oriented way for a 2D game. The game is already initialized by another file. Implement ONLY the character file. Do not implement any other file. The character file gets instantiated by another file. Initialize the character file with only itself, nothing else. The character has hit points which indicate its health. The character starts with 5 hit points. The character also has a list of equipments, namely: - A bow and arrow - A shield - A health potion. The image for the character can be found in the following locaiton: 'assets/images/character.bmp'. \n"


# Render prompt

### Textv1
renderPromptv1Text = """Write PyGame code to create a simple render file called 'remder.py' in an object-oriented way for a 2D game.
The game is already initialized by another file. Implement ONLY the render file. Do not implement any other file.
The render file gets instantiated by another file and receives a screen object with a level in it and a character sprite object.  
The render file's task is to render the characters movement on the level screen.
The character can stand on the platforms of the level.
Include ability to move the character left and right and make it jump by recording keyboard strokes. \n"""

### Promptv1
renderPromptv1Text = """Write PyGame code to create a simple render file called 'remder.py' in an object-oriented way for a 2D game. The game is already initialized by another file. Implement ONLY the render file. Do not implement any other file. The render file gets instantiated by another file and receives a screen object with a level in it and a character sprite object. The render file's task is to render the characters movement on the level screen. The character can stand on the platforms of the level. Include ability to move the character left and right and make it jump by recording keyboard strokes. \n"""


### Textv2
renderPromptv2Text = """Write PyGame code to create a simple render file called 'remder.py' in an object-oriented way for a 2D game.
The game is already initialized by another file. Implement ONLY the render class. Do not implement any other class.
The render class gets instantiated by another class and receives an already filled screen object with a level in it and a character sprite object.  
The render classes task is to implement the characters movement on the level screen.
The character can stand on the platforms of the level.
Include ability to move the character left and right and the ability to jump by recording keyboard strokes. \n"""

### Promptv2
renderPromptv2Text = "Write PyGame code to create a simple render file called 'remder.py' in an object-oriented way for a 2D game. The game is already initialized by another file. Implement ONLY the render class. Do not implement any other class. The render class gets instantiated by another class and receives an already filled screen object with a level in it and a character sprite object. The render classes task is to implement the characters movement on the level screen. The character can stand on the platforms of the level. Include ability to move the character left and right and the ability to jump by recording keyboard strokes. \n"

### Textv3
renderPromptv3Text = """Write PyGame code to create a simple render file called 'remder.py' in an object-oriented way for a 2D game.
The game is already initialized by another file. Implement ONLY the render class. Do not implement any other class.
The render class gets instantiated by another class and receives an already filled screen object with a level in it and a character sprite object.  
The render classes task is to implement the characters movement on the level screen.
Add ability to detect collision with the platforms on the level, so that the character can stand on the platforms in the level.
Include ability to move the character left and right and the ability to jump by recording keyboard strokes. \n"""

### Promptv3
renderPromptv3Text = "Write PyGame code to create a simple render file called 'remder.py' in an object-oriented way for a 2D game. The game is already initialized by another file. Implement ONLY the render class. Do not implement any other class. The render class gets instantiated by another class and receives an already filled screen object with a level in it and a character sprite object. The render classes task is to implement the characters movement on the level screen. Add ability to detect collision with the platforms on the level, so that the character can stand on the platforms in the level. Include ability to move the character left and right and the ability to jump by recording keyboard strokes. \n"

### Textv4
renderPromptv4Text = """Write PyGame code to create a simple render file called 'remder.py' in an object-oriented way for a 2D game.
The game is already initialized by another file. Implement ONLY the render class. Do not implement any other class.
The render class gets instantiated by another class and receives an already filled screen object with a level in it and a character sprite object.  
The render classes task is to implement the characters movement on the level screen.
The render class has a method called 'run()' which loops forever. The 'run()' method detects collision of the character with the platforms on the level, so that the character can stand on the platforms in the level.
The 'run()' method also records keyboard strokes from the user to move the character left and right and make the character jump. \n"""

### Promptv4
renderPromptv4Text = "Write PyGame code to create a simple render file called 'remder.py' in an object-oriented way for a 2D game. The game is already initialized by another file. Implement ONLY the render class. Do not implement any other class. The render class gets instantiated by another class and receives an already filled screen object with a level in it and a character sprite object. The render classes task is to implement the characters movement on the level screen. The render class has a method called 'run()' which loops forever. The 'run()' method detects collision of the character with the platforms on the level, so that the character can stand on the platforms in the level. The 'run()' method also records keyboard strokes from the user to move the character left and right and make the character jump. \n"

