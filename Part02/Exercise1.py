

import cv2 as cv
import numpy as np

img = cv.imread('/home/adrianoff10/Desktop/SAVI/Part02/images/lake.jpg')
assert img is not None, 'file coud not de read' 

cv.imshow('Lake',img)


rows, cols = img.shape[:2]
print('{} {}'.format(rows, cols))

img_black = np.zeros((rows, cols//2),np.uint8)
img_black = cv.cvtColor(img_black, cv.COLOR_GRAY2BGR)

'''
img2 = cv.addWeighted(img[0:rows, cols//2:cols], 0.5, img_black,0.5,0)

cv.imshow('', img2)
cv.waitKey(0)
cv.destroyAllWindows()
'''

#print(img_black.shape)
#cv.imshow('',img_black)

imgR = img[0:rows, cols//2 : cols] # parte direita da imagem
#print(imgR.shape)

imgL = img[0:rows, 0:cols//2]      # parte esquerda da imagem
#print(imgL.shape)

frames = []


for i in range(9):

    alpha = 1 - i/10
    beta = i/10
    right_part = cv.addWeighted(imgR, alpha, img_black, beta, 0)  # podia fazer tudo de uma vez, isto e right part = cv.addWeighted(img[:, cols//2 : cols],...)
    new_img = np.hstack((imgL, right_part))

    cv.imshow('Nightfall', new_img)
    cv.waitKey(100)
    frames.append(new_img)


height, width, channels = new_img.shape
size = (width, height)

fourcc = cv.VideoWriter_fourcc(*'DIVX')
out = cv.VideoWriter('Nightfallvid.avi', fourcc, 8.0, size)

for n in range(len(frames)):
    out.write(frames[n])

out.release()

cv.imshow('Nightfall', new_img)
cv.waitKey(100)
cv.destroyAllWindows()




