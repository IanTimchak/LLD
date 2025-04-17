from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))


from util.base import Player
import eel

# Set web files folder
eel.init('web')
eel.browsers.set_path('electron', 'node_modules/electron/dist/electron.exe')



# Expose a function to JavaScript
@eel.expose
def say_hello_py(x):
    print(f"Calling JavaScript function from Python with argument: {x}")
    eel.addAiMessage(x);

# Send the AI response 
def send_ai_response(response):
    print(f"Sending AI response: {response}")
    eel.addAiMessage(response)

player = Player("Goredawn the Gladiator")


player.connect()
player.add_subscriber(send_ai_response)

# Start the application
eel.start('index.html', mode='electron')

