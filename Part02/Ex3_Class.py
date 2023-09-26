

import cv2 as cv
import numpy as np
import math


img1 = cv.imread('/home/adrianoff10/Desktop/SAVI/Part02/images/school.jpg')
assert img1 is not None, 'could not read this file'

img2 = cv.imread('/home/adrianoff10/Desktop/SAVI/Part02/images/beach.jpg')
assert img1 is not None, 'could not read this file'


cv.imshow('School', img1)
cv.waitKey(0)



pointStart = None
pointEnd = None

def make_template(event, img, x, y):
    global x1,y1, x2, y2, template1
    if event == cv.EVENT_LBUTTONDBLCLK:
        pointStart = (x, y) 

    elif event == cv.EVENT_LBUTTONUP:
        pointEnd = (x, y)

    cv.rectangle(img, (x1,y1), (x2,y1), 0, 5)

    template1 = img[x1 : x2, y1 : y2]
    cv.destroyAllWindows()

cv.namedWindow('School')
cv.setMouseCallback('School',make_template)

res1 = cv.matchTemplate(img1, template1, cv.TM_CCOEFF)
minVal1, maxVal1, minLoc1, maxLoc1 = cv.minMaxLoc(res1)
center1 = [maxLoc1[0] + int(res1[3])//2, maxLoc1[1] + int(res1[2])//2]

cv.circle(img1, (center1[0], center1[1]), 20, 0, 4)

cv.imshow('School', img1)
cv.waitKey(0)
cv.destroyAllWindows()
























