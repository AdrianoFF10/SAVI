

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('/home/adrianoff10/Desktop/SAVI/Part02/images/scene.jpg')
assert img is not None, 'Could not read this file'

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


template = cv.imread('/home/adrianoff10/Desktop/SAVI/Part02/images/wally.png')
assert template is not None, 'could not read this file'
tempgray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

w, h = template.shape[:2]


res = cv.matchTemplate(imgray, tempgray, cv.TM_CCOEFF)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

top_left = max_loc

imgray = cv.cvtColor(imgray, cv.COLOR_GRAY2BGR)
print(img.shape)
print(template.shape)

print(top_left[0])
print(top_left[0] + w)
print(top_left[1] )
print(top_left[1] + h)


imgray[top_left[1] : top_left[1] + w, top_left[0] : top_left[0] + h] = template

cv.imshow('Image', imgray)
cv.waitKey(0)
cv.destroyAllWindows()




