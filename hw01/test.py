import keyboard
import time

def key_press(key):
    if(key.name == '^[[A'):
        print("up")
    print(key.name)

keyboard.on_press(key_press)

while True:
    time.sleep(1)