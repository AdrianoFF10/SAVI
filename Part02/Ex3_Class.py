

import cv2 as cv
import numpy as np
import math

# define callback function
pointStart = None
pointEnd = None

def mouseCallback(event, x, y, flags, param):
    global pointEnd, pointStart
    if event == cv.EVENT_LBUTTONDOWN:
        pointStart = (x, y) 
        print('Recorded point start')
    elif event == cv.EVENT_LBUTTONUP:
        pointEnd = (x, y)
        print(pointEnd)
        print('Recorded point end')


#Load image 1
img1 = cv.imread('/home/adrianoff10/Desktop/SAVI/Part02/images/school.jpg')
assert img1 is not None, 'could not read this file'

cv.imshow('Scene', img1)
cv.setMouseCallback('Scene',mouseCallback)

while True:     # wait for template definition

    if pointEnd is not None and pointEnd is not None:
        break

    cv.waitKey(20)

#create template
template1 = img1[pointStart[1]:pointEnd[1], pointStart[0]:pointEnd[0]]
cv.imshow('Template 1', template1)
cv.waitKey(100)

# Find Wally
res1 = cv.matchTemplate(img1, template1, cv.TM_CCOEFF_NORMED)  # saida col, row, w, h
minVal1, maxVal1, minLoc1, maxLoc1 = cv.minMaxLoc(res1)
center1 = [maxLoc1[0] + template1.shape[1]//2, maxLoc1[1] + template1.shape[0]//2]

cv.circle(img1, (center1[0], center1[1]), 30, (0,0,0), 4)

'''
#reset template points
pointStart = None
pointEnd = None
'''
#Load image
img2 = cv.imread('/home/adrianoff10/Desktop/SAVI/Part02/images/beach.jpg')
assert img2 is not None, 'could not read this file'

#show image and call function
cv.imshow('Beach', img2)
cv.setMouseCallback('Beach', mouseCallback)

#close as soon as points are defined
while True:
    if pointEnd is not None and pointStart is not None:
        break

#Create template
template2 = img2[pointStart[0] : pointEnd[0], pointStart[1] : pointEnd[1]]
cv.imshow('Template2', template2)
cv.waitKey(100)

#Where is Wally
res2 = cv.matchTemplate(img2, template2, cv.TM_CCOEFF_NORMED)     
_, maxVal2, _, maxLoc2 = cv.minMaxLoc(res2)    #saida row col  
center2 = (maxLoc2[0] + template2.shape[1]//2, maxLoc2[1] +  template2.shape[0]//2)

cv.circle(img2, center2, 30, 0, 5)

cv.imshow('School', img1)
cv.imshow('Beach', img2)
cv.waitKey(0)
cv.destroyAllWindows()



