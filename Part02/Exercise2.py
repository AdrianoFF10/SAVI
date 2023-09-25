

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('/home/adrianoff10/Desktop/SAVI/Part02/images/scene.jpg')
assert img is not None, 'Could not read this file'

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


template = cv.imread('/home/adrianoff10/Desktop/SAVI/Part02/images/wally.png', cv.IMREAD_GRAYSCALE)
assert template is not None, 'could not read this file'

h, w = template.shape[:2]

print('{} {}'.format(h,w))
res = cv.matchTemplate(imgray, template, cv.TM_CCOEFF)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

center = (max_loc[0] + w//2, max_loc[1] + h//2)


cv.circle(img, center, 20 ,(0,255,255), 5)

plt.subplot(121), plt.imshow(imgray), plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img), plt.title('Wally was found'), plt.xticks([]), plt.yticks([])
plt.show()






