from pynput.keyboard import Key, Controller as KeyController
from pynput.mouse import Button, Controller as MouseController
import time

class Controller:
    def __init__(self):
        self.keyboard = KeyController()
        self.mouse = MouseController()

    def press_space(self):
        self.keyboard.press(Key.space)
        time.sleep(0.05)
        print("jump")
        self.keyboard.release(Key.space)

    def click_left(self):
        print("click")
        self.mouse.click(Button.left)

    def set_mouse_position(self, x, y):
        self.mouse.position = (int(x), int(y))
