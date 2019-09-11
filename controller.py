from pynput.keyboard import Key, Controller as KeyController
import time

class Controller:
    def __init__(self):
        self.keyboard = KeyController()

    def press_space(self):
        self.keyboard.press(Key.space)
        time.sleep(0.05)
        print("jump")
        self.keyboard.release(Key.space)
