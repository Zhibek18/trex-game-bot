import cv2
from mss import mss
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np

class Vision:
    def __init__(self):
        self.monitor = {'top': 0, 'left': 0, 'width': 1366, 'height': 768}#screen size
        self.screen = mss()
        self.dino_template = cv2.imread('assets/dino.png', 0)

    def take_screenshot(self):
        img = self.screen.grab(self.monitor)
        img = Image.frombytes('RGB', img.size, img.rgb)
        return img

    def find_template(self, screenshot, template):
        screenshot_array = np.array(screenshot)
        screenshot_array = cv2.cvtColor(screenshot_array, cv2.COLOR_RGB2GRAY)
        res = cv2.matchTemplate(screenshot_array, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        return max_loc

    #grab small area next to dino where trees can apear
    def take_small_screenshot(self, dino):  
        box = {'top': dino[1] + 10, 'left': dino[0] + 20, 'width': 40, 'height': 50}
        img = self.screen.grab(box)
        return img

    def find_cactus(self):
        screenshot = self.take_screenshot()
        screenshot_copy = screenshot.copy()
        dino = self.find_template(screenshot_copy, self.dino_template)
        box = (dino[0] + 20, dino[1] + 10, dino[0]+ 40, dino[1] - 40)
        finding_area = screenshot.crop(box).load()
        findin_area = np.array(finding_area)
        #plt.imshow(finding_area,cmap = 'gray')
        #plt.show()
        a = finding_area.getcolors()
        print(a.sum())
