

import cv2 as cv
import numpy as np
import math


img1 = cv.imread('/home/adrianoff10/Desktop/SAVI/Part02/images/school.jpg')
assert img1 is not None, 'could not read this file'

img2 = cv.imread('/home/adrianoff10/Desktop/SAVI/Part02/images/beach.jpg')
assert img1 is not None, 'could not read this file'


res1 = cv.selectROI('Select your template', img1)   # resultado e o y, x, altura, largura
template1 = img1[int(res1[1]) : int(res1[1] + res1[3]), int(res1[0]) : int(res1[0] + res1[2])]
h, w  = template1.shape[:2]


match1 = cv.matchTemplate(img1, template1, cv.TM_CCOEFF)
minVal1, maxVal1, minLoc1, maxLoc1 = cv.minMaxLoc(match1)
center1 = [maxLoc1[0] + int(res1[3])//2, maxLoc1[1] + int(res1[2])//2]
r1 = min(w,h) + 2

res2 = cv.selectROI('Select your template', img2)   # resultado e o y, x, altura, largura
template2 = img2[int(res2[1]) : int(res2[1] + res2[3]), int(res2[0]) : int(res2[0] + res2[2])]
h, w = template2.shape[:2]


match2 = cv.matchTemplate(img2, template2, cv.TM_CCOEFF)
minVal2, maxVal2, minLoc2, maxLoc2 = cv.minMaxLoc(match2)
center2 = [maxLoc2[0] + res2[3]//2, maxLoc2[1] + res2[2]//2]
r2 = min(w,h) + 2

cv.destroyAllWindows()    #cv.selectROI opens windows that needs to be closed

cv.circle(img1, (center1[0], center1[1]), r1, 0, 4)
cv.circle(img2, (center2[0], center2[1]), r2, 0, 4)

cv.imshow('School', img1)
cv.imshow('Beach', img2)

cv.waitKey(0)
cv.destroyAllWindows()


