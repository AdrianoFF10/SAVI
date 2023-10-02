

import cv2
import numpy as np
from time import sleep

min_width = 80
min_height = 80
#largura_max = 250
#altura_max = 250
offset = 35
line_pos = 510

# FPS to vídeo
delay = 60

detection = []
cars = 0

def set_center(x, y, w, h):

    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

# video source input
cap = cv2.VideoCapture('/home/adrianoff10/Desktop/traffic.mp4')

bg_subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows = True)
erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))


while (1):

    ret, frame = cap.read()

    if ret is not True:
        break

    stime = float(1/delay)         
    sleep(stime)   

    fg_mask = bg_subtractor.apply(frame)
    _, thresh = cv2.threshold(fg_mask, 249, 255, cv2.THRESH_BINARY)
    cv2.erode(thresh, erode_kernel, thresh, iterations=6)
    cv2.dilate(thresh, dilate_kernel, thresh, iterations=6)


    contour, h = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE  )          
    cv2.line(frame, (25, line_pos), (1200, line_pos), (176, 130, 39), 3)            

    for c in contour:            

        (x, y, w, h) = cv2.boundingRect(c)                
        good_size = (w >= min_width) and (h >= min_height)

        if not good_size:                 
           continue                      

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)                    
        center = set_center(x, y, w, h)                    
        detection.append(center)                     
        cv2.circle(frame, center, 4, (0, 0, 255), -1)                    

        for (x, y) in detection:                 

            if (y < (line_pos + offset) and y > (line_pos)):                         

                cars += 1                          
                cv2.line(frame, (25, line_pos), (1200, line_pos), (0, 127, 255), 3)                         
                detection.remove((x, y))                        
                print("No. of cars detected : " + str(cars))                        

    cv2.putText(frame, "VEHICLE COUNT : "+str(cars), (320, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.imshow("Video Original", frame)
    cv2.imshow(" Thresh ", thresh)

    if cv2.waitKey(1) == 27:

        break        

cv2.destroyAllWindows()
cap.release()
