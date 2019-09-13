import cv2
import numpy as np
import webbrowser
import time

from controller import Controller
from vision import Vision

url = 'https://chromedino.com/'
webbrowser.open(url, new=2)  # open in new tab

time.sleep(5)
controller = Controller()
vision = Vision()

controller.set_mouse_position(250, 250)
controller.click_left() #click to set active window with game
controller.press_space() #start game
controller.press_space() #start game
vision.find_cactus()

while True:
    if (vision.find_cactus()):
        controller.press_space()
        time.sleep(0.1)
    time.sleep(0.0001)
    #time.sleep(0.1)

