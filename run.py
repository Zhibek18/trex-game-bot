import cv2
import numpy as np
import webbrowser
import time

from controller import Controller

url = 'index.html'
webbrowser.open(url, new=2)  # open in new tab

time.sleep(5)
controller = Controller()
controller.set_mouse_position(250, 250)
controller.click_left()
time.sleep(5)
while True:
    controller.press_space()
    time.sleep(2)

