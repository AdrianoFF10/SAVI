

import cv2 as cv
import numpy as np
import copy

img = cv.imread('/home/adrianoff10/Desktop/SAVI/Part02/images/lake.jpg')
assert img is not None, 'file coud not de read' 

cv.imshow('Lake',img)

img2 = copy.deepcopy(img)
rows, cols = img.shape[:2]

frames=[]

for i in range(8):
    for row in range(rows):
        for col in range(cols//2, cols):

            img[row, col, 0] = max(img2[row, col, 0] - 8 * i, 0)   #blue chanel
            img[row, col, 1] = max(img2[row, col, 1] - 8 * i, 0)   #green chanel
            img[row, col, 2] = max(img2[row, col, 2] - 8 * i, 0)   #red chanel

    cv.imshow('image', img)
    cv.waitKey(100)
    frames.append(img)



height, width, channels = img.shape
size = (width, height)

fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('Nightfallvid_Class.avi', fourcc, 8.0, size)

for n in range(len(frames)):
    out.write(frames[n])

out.release()
cv.destroyAllWindows()





















