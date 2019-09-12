import cv2
from mss import mss
from PIL import Image
from matplotlib import pyplot as plt

class Vision:
    def __init__(self):
        self.monitor = {'top': 0, 'left': 0, 'width': 1366, 'height': 768}#screen size
        self.screen = mss()

    def take_screenshot(self):
        img = self.screen.grab(self.monitor)
        return img

vision = Vision()
img = vision.take_screenshot()
imgplot = plt.imshow(img)
plt.show()
