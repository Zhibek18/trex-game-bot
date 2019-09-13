import cv2
import matplotlib.image as mpimg
from matplotlib import pyplot as plt

screenshot = cv2.imread('assets/screenshot_end.png', 0)
template = cv2.imread('assets/dino.png', 0)
h = template.shape[0]
w = template.shape[1]
res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = max_loc

bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(screenshot, top_left, bottom_right, 0, 1)

plt.imshow(screenshot,cmap = 'gray')
plt.show()
