import cv2
import numpy as np
import webbrowser
import time

from controller import Controller
from vision import Vision

url = 'index.html'
webbrowser.open(url, new=2)  # open in new tab

time.sleep(5)
controller = Controller()
vision = Vision()

controller.set_mouse_position(250, 250)
controller.click_left() #click to set active window with game
controller.press_space() #start game
vision.find_cactus()
i = 0
while i < 3:
    controller.press_space()
    vision.find_cactus()
    time.sleep(2)
    i = i + 1

