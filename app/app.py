import eel

# Set web files folder
eel.init('../web')
eel.browsers.set_path('electron', 'node_modules/electron/dist/electron.exe')

# Expose a function to JavaScript
@eel.expose
def say_hello_py(x):
    print(f"Hello from {x}")

# Start the application
eel.start('index.html', mode='electron')
