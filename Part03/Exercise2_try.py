

import cv2
import numpy as np

min_width = 80
min_height = 80
#largura_max = 250
#altura_max = 250
offset = 20
line_pos = 510

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


bg_subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows = True)

erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 31))

cap = cv2.VideoCapture('/home/adrianoff10/Desktop/traffic.mp4')
sucess, frame = cap.read()


while sucess:

    fg_mask = bg_subtractor.apply(frame)
    _, thresh = cv2.threshold(fg_mask, 237, 255, cv2.THRESH_BINARY)
    cv2.erode(thresh, erode_kernel, thresh, iterations=3)
    cv2.dilate(thresh, dilate_kernel, thresh, iterations=3)


    contour, h = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE  )          
    cv2.line(frame, (200, line_pos), (370, line_pos), (0, 0, 255), 2)      
    cv2.line(frame, (380, line_pos), (660, line_pos), (0, 255, 0), 2) 
    cv2.line(frame, (670, line_pos), (870, line_pos), (255, 0, 0), 2) 
    cv2.line(frame, (880, line_pos), (1200, line_pos), (176, 130, 39), 2)       

    for c in contour:     

        if cv2.contourArea(c) > 1000:
            (x, y, w, h) = cv2.boundingRect(c)                
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)                    
            center = set_center(x, y, w, h)
            detection.append(center)                     
            cv2.circle(frame, center, 4, (0, 0, 255), -1)  
                              

        for (x, y) in detection:                 

            if (y < (line_pos + offset) and y > (line_pos - offset)) and x >= 200 and x <= 370:                         

                cars1 += 1                          
                cv2.line(frame, (200, line_pos), (370, line_pos), (0, 127, 255), 3)                         
                detection.remove((x, y))               
                print("No. of cars detected on 1st lane: {}".format(str(cars1)))

            if (y < (line_pos + offset) and y > (line_pos - offset)) and x > 370 and x <= 660:                         
                cars2 += 1                          
                cv2.line(frame, (380, line_pos), (660, line_pos), (0, 127, 255), 3)                         
                detection.remove((x, y))
                print("No. of cars detected on 2nd lane: {}".format(str(cars2)))

            if (y < (line_pos + offset) and y > (line_pos - offset)) and x > 660 and x <= 870:                         
                cars3 += 1                          
                cv2.line(frame, (660, line_pos), (870, line_pos), (0, 127, 255), 3)                         
                detection.remove((x, y))              
                print("No. of cars detected on 3rd lane: {}".format(str(cars3)))

            if (y < (line_pos + offset) and y > (line_pos - offset)) and x > 870 and x <= 1200:                         
                cars4 += 1                          
                cv2.line(frame, (870, line_pos), (1100, line_pos), (0, 127, 255), 3)                         
                detection.remove((x, y))
                print("No. of cars detected on 4th lane: {}".format(str(cars4)))

    cv2.putText(frame, "Cars 1st lane: "+str(cars1), (30, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.putText(frame, "Cars 2nd lane: "+str(cars2), (30, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.putText(frame, "Cars 3rd lane: "+str(cars3), (30, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.putText(frame, "Cars 4th lane: "+str(cars4), (30, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)

    cv2.imshow("Video Original", frame)
    cv2.imshow(" Thresh ", thresh)

    if cv2.waitKey(30) == 27:

        break 

    sucess, frame = cap.read()       

cv2.destroyAllWindows()
cap.release()