

import cv2
import numpy as np

check_x = None
check_y = None
offset = 12
line_pos = 400

detection = []
cars = 0

def set_center(x, y, w, h):

    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

# video source input

bg_subtractor = cv2.createBackgroundSubtractorMOG2(detectShadows = True)

erode_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
dilate_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 31))

cap = cv2.VideoCapture('/home/adrianoff10/Desktop/traffic.mp4')
sucess, frame = cap.read()

while sucess:

    fg_mask = bg_subtractor.apply(frame)
    _, thresh = cv2.threshold(fg_mask, 220, 255, cv2.THRESH_BINARY)
    cv2.erode(thresh, erode_kernel, thresh, iterations=3)
    cv2.dilate(thresh, dilate_kernel, thresh, iterations=3)

    cv2.line(frame, (25, line_pos), (1200, line_pos), (176, 130, 39), 3)            
    contour, h = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE  )          

    for c in contour:     

        if cv2.contourArea(c) > 1000:
            (x, y, w, h) = cv2.boundingRect(c)                
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)                    
            center = set_center(x, y, w, h)   

            if check_x is None and check_y is None:
                detection.append(center)

            else:
                if check_x - offset <= center[0] <= check_x + offset and check_y - offset <= center[1] <= check_y + offset:
                    pass
                else:
                    detection.append(center)
            
            cv2.circle(frame, center, 4, (0, 0, 255), -1)  
              
        for (x, y) in detection:                 

            if (y < (line_pos + offset) and y > (line_pos - offset)):                         

                cars += 1                          
                cv2.line(frame, (25, line_pos), (1200, line_pos), (0, 127, 255), 3)                         
                detection.remove((x, y))      
                check_x = x
                check_y = y  
                print("No. of cars detected : " + str(cars))   
                     

    cv2.putText(frame, "VEHICLE COUNT : "+str(cars), (320, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.imshow("Video Original", frame)
    cv2.imshow(" Thresh ", thresh)
    
    if cv2.waitKey(30) == 27:

        break   

    success, frame = cap.read()
     

cv2.destroyAllWindows()
cap.release()
