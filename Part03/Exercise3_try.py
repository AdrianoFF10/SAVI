

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
cars1 = 0
cars2 = 0
cars3 = 0
cars4 = 0


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
    cv2.line(frame, (200, line_pos), (450, line_pos), (0, 0, 255), 2)      
    cv2.line(frame, (460, line_pos), (650, line_pos), (0, 255, 0), 2) 
    cv2.line(frame, (660, line_pos), (900, line_pos), (255, 0, 0), 2) 
    cv2.line(frame, (910, line_pos), (1100, line_pos), (176, 130, 39), 2)       

    for c in contour:            

        (x, y, w, h) = cv2.boundingRect(c)                
        good_size = (w >= min_width) and (h >= min_height)

        if not good_size:                 
           continue                      

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)                    
        center = set_center(x, y, w, h)                    
        detection.append(center)                     
        #cv2.circle(frame, center, 4, (0, 0, 255), -1)                    

        for (x, y) in detection:                 

            if (y < (line_pos + offset) and y > (line_pos)) and x > 200 and x < 450:                         

                cars1 += 1                          
                cv2.line(frame, (200, line_pos), (450, line_pos), (0, 127, 255), 3)                         
                detection.remove((x, y))
                c1hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                color1 = c1hsv[center[1], center[0]]
                if color1[0] < 30:
                    color1 = 'Red'
                elif color1[0] > 30 and color1[0] < 60:
                    color1 = 'Yellow'
                elif color1[0] > 60 and color1[0] < 90:
                    color1 = 'Green'
                elif color1[0] > 90 and color1[0] < 120:
                    color1 = 'Cyan'
                elif color1[0] > 120 and color1[0] < 150:
                    color1 = 'Blue'
                elif color1[0] > 150:
                    color1 = 'Magenta'                     
                print("No. of cars detected on 1st lane: {}, Color: {} ".format(str(cars1),color1))

            if (y < (line_pos + offset) and y > (line_pos)) and x > 450 and x < 650:                         

                cars2 += 1                          
                cv2.line(frame, (460, line_pos), (650, line_pos), (0, 127, 255), 3)                         
                detection.remove((x, y))
                c2hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                color2 = c2hsv[center[1], center[0]]
                if color2[0] < 30:
                    color2 = 'Red'
                elif color2[0] > 30 and color2[0] < 60:
                    color2 = 'Yellow'
                elif color2[0] > 60 and color2[0] < 90:
                    color2 = 'Green'
                elif color2[0] > 90 and color2[0] < 120:
                    color2 = 'Cyan'
                elif color2[0] > 120 and color2[0] < 150:
                    color2 = 'Blue'
                elif color2[0] > 150:
                    color2 = 'Magenta'
                print("No. of cars detected on 2nd lane: {}, Color: {} ".format(str(cars2), color2))

            if (y < (line_pos + offset) and y > (line_pos)) and x > 650 and x < 900:                         
                cars3 += 1                          
                cv2.line(frame, (660, line_pos), (900, line_pos), (0, 127, 255), 3)                         
                detection.remove((x, y))
                c3hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                #print(center)
                color3 = c3hsv[center[1], center[0]]
                #print(color3[0])
                if color3[0] < 30:
                    color3 = 'Red'
                elif color3[0] > 30 and color3[0] < 60:
                    color3 = 'Yellow'
                elif color3[0] > 60 and color3[0] < 90:
                    color3 = 'Green'
                elif color3[0] > 90 and color3[0] < 120:
                    color3 = 'Cyan'
                elif color3[0] > 120 and color3[0] < 150:
                    color3 = 'Blue'
                elif color3[0] > 150:
                    color3 = 'Magenta'                     
                print("No. of cars detected on 3rd lane: {}, Color: {} ".format(str(cars3),color3))

            if (y < (line_pos + offset) and y > (line_pos)) and x > 900 and x < 1100:                         
                cars4 += 1                          
                cv2.line(frame, (910, line_pos), (1100, line_pos), (0, 127, 255), 3)                         
                detection.remove((x, y))
                c4hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                color4 = c4hsv[center[1], center[0]]
                if color4[0] < 30:
                    color4 = 'Red'
                elif color4[0] > 30 and color4[0] < 60:
                    color4 = 'Yellow'
                elif color4[0] > 60 and color4[0] < 90:
                    color4 = 'Green'
                elif color4[0] > 90 and color4[0] < 120:
                    color4 = 'Cyan'
                elif color4[0] > 120 and color4[0] < 150:
                    color4 = 'Blue'
                elif color4[0] > 150:
                    color4 = 'Magenta'                     
                print("No. of cars detected on 4th lane: {}, Color: {} ".format(str(cars4),color4))

    cv2.putText(frame, "Cars 1st lane: "+str(cars1), (30, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.putText(frame, "Cars 2nd lane: "+str(cars2), (30, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.putText(frame, "Cars 3rd lane: "+str(cars3), (30, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.putText(frame, "Cars 4th lane: "+str(cars4), (30, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)

    cv2.imshow("Video Original", frame)
    cv2.imshow(" Thresh ", thresh)

    if cv2.waitKey(1) == 27:

        break        

cv2.destroyAllWindows()
cap.release()