# LLM PyGame experiment

<!-- TOC -->
* [Project description](#project-description)
  * [Initial goal](#initial-goal)
  * [Tools used](#tools-used)
  * [End result](#end-result)
  * [Next steps](#next-steps)
* [Google Colab Llama.cpp code](#google-colab-llamacpp-code)
  * [Context window size 512 (default)](#context-window-size-512-default)
  * [Context window size 2048](#context-window-size-2048)
  * [Context window size 4096](#context-window-size-4096)
<!-- TOC -->

## Project description

### Initial goal
Test the ability of an LLM to create custom-tailored games for everyone's specific tastes.

Game development requires lots of resources, including time, money and knowledge. Not everyone has the resources to create a whole game from scratch. However, LLMs do have the coding knowledge and don't cost much to run.  

LLMs are currently still quite in active development though, which is why this experiment is conducted to measure how good they are as of now for this use case.

### Tools used
- **Llama-cpp-python**
  - Inference for llama models
  - Able to distribute weights between GPU and system RAM
- **Phind-CodeLlama-34B-v2**
  - LLM fine-tuned specifically for coding
  - One of the top scorers in Hugging Face code model leaderboard
- **PyGame**
  - Python game development library
  - Chose PyGame as it's purely text based and has no UI
  - Initial assumption: pure text based should make the coding  easier 

### End result
Turns out that my initial assumption was completely wrong.

The lack of a UI in PyGame means that every little connection between modules needs to be programmed. On top of that, LLMs have a limited context window size, so it cannot write a whole file containing every single logic in the game. To circumvent that, I tried to keep modules as isolated as possible to make it easier for the LLM to understand the general project folder structure. But that meant that I have to tell the LLM every time exactly which modules it should consider.

This requires lots of knowledge about programming, game development and tons of thinking, which beats the point of this experiment.  


### Next steps
Currently experimenting with using LLMs with the Unity game engine to see if a UI can help solve the module communication issue.

## Google Colab Llama.cpp code

### Context window size 512 (default)

```python
!CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python

from llama_cpp import Llama

model_path="drive/MyDrive/ColabNotebooks/Models/TheBloke/WizardCoder-Python-34B-V1.0-GGUF/wizardcoder-python-34b-v1.0.Q5_K_M.gguf"
temperature = 0
top_p = 1
n_gpu_layers = 25 # make sure to adjust this according to your available VRAM

llm = Llama(model_path=model_path, temperature=temperature, n_gpu_layers=n_gpu_layers)

marioPrompt = "Write PyGame code to create a 'Super Mario Bros.' game. Implement just the first level of the 'Super Mario Bros.' game. \n"

squarePrompt = "Write PyGame code to create a video game. The background is black. Create a sprite as a small white square. The player controls the sprite and can move up, down, left and right. The player moves the sprite with the arrow keys on the keyboard. \n"

llm(squarePrompt, echo=False, stop=None, max_tokens=1000)
```


### Context window size 2048

```python
!CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python

from llama_cpp import Llama

model_path="drive/MyDrive/ColabNotebooks/Models/TheBloke/Phind-CodeLlama-34B-Python-v1-GGUF/phind-codellama-34b-python-v1.Q5_K_M.gguf"
temperature = 0
top_p = 1
n_gpu_layers = 25 # make sure to adjust this according to your available VRAM
n_ctx = 2048

llm = Llama(model_path=model_path, temperature=temperature, n_gpu_layers=n_gpu_layers, n_ctx = n_ctx)

marioPrompt = "Write PyGame code to create a 'Super Mario Bros.' game. Implement just the first level of the 'Super Mario Bros.' game. \n"

squarePrompt = "Write PyGame code to create a video game. The background is black. Create a sprite as a small white square. The player controls the sprite and can move up, down, left and right. The player moves the sprite with the arrow keys on the keyboard. \n"

output = llm(marioPrompt, echo=False, stop=None, max_tokens=2048)

output['choices'][0]['text']

output['choices'][0]['finish_reason']

output['usage']
```


### Context window size 4096

```python
!CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python

from llama_cpp import Llama

model_path="drive/MyDrive/ColabNotebooks/Models/TheBloke/Phind-CodeLlama-34B-Python-v1-GGUF/phind-codellama-34b-python-v1.Q5_K_M.gguf"
temperature = 0
top_p = 1
n_gpu_layers = 25 # make sure to adjust this according to your available VRAM
n_ctx = 4096

llm = Llama(model_path=model_path, temperature=temperature, n_gpu_layers=n_gpu_layers, n_ctx = n_ctx)

renderFilePrompt = "Write PyGame code to create a simple render file called 'render.py' in an object-oriented way for a 2D game. The game is already initialized by another file. Implement ONLY the render class. Do not implement any other class. The render class gets instantiated by another class and receives an already filled screen object with a level in it and a character sprite object. The render classes task is to implement the characters movement on the level screen. The render class has a method called 'run()' which loops forever. The 'run()' method detects collision of the character with the platforms on the level, so that the character can stand on the platforms in the level. The 'run()' method also records keyboard strokes from the user to move the character left and right and make the character jump. \n"

output = llm(renderFilePrompt, echo=False, stop=None, max_tokens=4096)

output['choices'][0]['text']

output['choices'][0]['finish_reason']

output['usage']
```

## Attribution

Background image in menu:
<a href="https://www.freepik.com/free-vector/medieval-castle-tavern-room-with-stone-walls_32665649.htm#query=fantasy%20background%20tavern&position=2&from_view=search&track=ais&uuid=58602a07-ec55-4f8d-9604-611dd27e6f6b">Image by upklyak</a> on Freepik
