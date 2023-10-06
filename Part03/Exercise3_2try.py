

import cv2
import numpy as np

check_x = None
check_y = None
offset = 12
line_pos = 400

detection = []
cars1 = 0
cars2 = 0
cars3 = 0
cars4 = 0
cars=0

red_lower = np.array([136, 87, 111], np.uint8)
red_upper = np.array([180, 255, 255], np.uint8)

green_lower = np.array([25, 52, 72], np.uint8)
green_upper = np.array([102, 255, 255], np.uint8)

blue_lower = np.array([94, 80, 2], np.uint8)
blue_upper = np.array([120, 255, 255], np.uint8)

lower_yellow = np.array([25,100,100])
upper_yellow = np.array([30,255,255])

lower_dark_teal = np.array([0,0,200])
upper_dark_teal = np.array([180,255,255])

lower_bright_teal = np.array([0,0,0])
upper_bright_teal = np.array([180,255,100])

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

while (1):

    ret, frame = cap.read()

    if ret is not True:
        break
   
    fg_mask = bg_subtractor.apply(frame)
    _, thresh = cv2.threshold(fg_mask, 220, 255, cv2.THRESH_BINARY)
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

            if check_x is None and check_y is None:
                detection.append(center)

            else:
                if check_x - offset <= center[0] <= check_x + offset and check_y - offset <= center[1] <= check_y + offset:
                    pass
                else:
                    detection.append(center)
            
            #cv2.circle(frame, center, 4, (0, 0, 255), -1)  
              
        for (x, y) in detection:                 

            if (y < (line_pos + offset) and y > (line_pos - offset)):                         

                check_x = x
                check_y = y
                if x >= 200 and x <= 370:
                    cars1 += 1  
                    cars+=1                        
                    cv2.line(frame, (200, line_pos), (370, line_pos), (0, 127, 255), 3)                         
                    detection.remove((x, y))               
                    c1hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    color1 = c1hsv[center[1], center[0]]
                    print(color1)
                    if red_lower[0] <= color1[0] <= red_upper[0] and red_lower[1] <= color1[1]<= red_upper[1] and red_lower[2] <= color1[2] <= red_upper[2]:
                        color2 =  'Red'
                    elif green_lower[0] <= color1[0] <= green_upper[0] and green_lower[1] <= color1[1]<= green_upper[1] and green_lower[2] <= color1[2] <= green_upper[2]:
                        color1 = 'Green'
                    elif blue_lower[0] <= color1[0] <= blue_upper[0] and blue_lower[1] <= color1[1]<= blue_upper[1] and blue_lower[2] <= color1[2] <= blue_upper[2]:
                        color1 = 'Blue'
                    elif lower_yellow[0] <= color1[0] <= upper_yellow[0] and lower_yellow[1] <= color1[1]<= upper_yellow[1] and lower_yellow[2] <= color1[2] <= upper_yellow[2]:
                        color1 = 'Yellow'
                    elif lower_dark_teal[0] <= color1[0] <= upper_dark_teal[0] and lower_dark_teal[1] <= color1[1]<= upper_dark_teal[1] and lower_dark_teal[2] <= color1[2] <= upper_dark_teal[2]:
                        color1 = 'Dark Color'
                    elif lower_bright_teal[0] <= color1[0] <= upper_bright_teal[0] and lower_bright_teal[1] <= color1[1]<= upper_bright_teal[1] and lower_bright_teal[2] <= color1[2] <= upper_bright_teal[2]:
                        color1 = 'Bright Color'
                    else:
                        color1 = 'Other'
                    print("No. of cars detected on 2nd lane: {}, Color: {} ".format(str(cars1), color1))


                elif x > 370 and x <= 660:
                    cars2 += 1
                    cars+=1                           
                    cv2.line(frame, (380, line_pos), (660, line_pos), (0, 127, 255), 3)                         
                    detection.remove((x, y))
                    c2hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    color2 = c2hsv[center[1], center[0]]
                    print(color2)
                    if red_lower[0] <= color2[0] <= red_upper[0] and red_lower[1] <= color2[1]<= red_upper[1] and red_lower[2] <= color2[2] <= red_upper[2]:
                        color2 =  'red'
                    elif green_lower[0] <= color2[0] <= green_upper[0] and green_lower[1] <= color2[1]<= green_upper[1] and green_lower[2] <= color2[2] <= green_upper[2]:
                        color2 = 'green'
                    elif blue_lower[0] <= color2[0] <= blue_upper[0] and blue_lower[1] <= color2[1]<= blue_upper[1] and blue_lower[2] <= color2[2] <= blue_upper[2]:
                        color2 = 'blue' 
                    elif lower_yellow[0] <= color2[0] <= upper_yellow[0] and lower_yellow[1] <= color2[1]<= upper_yellow[1] and lower_yellow[2] <= color2[2] <= upper_yellow[2]:
                        color2 = 'Yellow'
                    elif lower_dark_teal[0] <= color2[0] <= upper_dark_teal[0] and lower_dark_teal[1] <= color2[1]<= upper_dark_teal[1] and lower_dark_teal[2] <= color2[2] <= upper_dark_teal[2]:
                        color2 = 'Dark Color' 
                    elif lower_bright_teal[0] <= color2[0] <= upper_bright_teal[0] and lower_bright_teal[1] <= color2[1]<= upper_bright_teal[1] and lower_bright_teal[2] <= color2[2] <= upper_bright_teal[2]:
                        color2 = 'Bright Color'
                    else:
                        color2 = 'Other'
                    print("No. of cars detected on 2nd lane: {}, Color: {} ".format(str(cars2), color2))

                elif x > 660 and x <= 870:
                    cars3 += 1   
                    cars+=1                        
                    cv2.line(frame, (660, line_pos), (870, line_pos), (0, 127, 255), 3)                         
                    detection.remove((x, y))              
                    c3hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    color3 = c3hsv[center[1], center[0]]
                    #print(color3)
                    if red_lower[0] <= color3[0] <= red_upper[0] and red_lower[1] <= color3[1]<= red_upper[1] and red_lower[2] <= color3[2] <= red_upper[2]:
                        color3 =  'red'
                    elif green_lower[0] <= color3[0] <= green_upper[0] and green_lower[1] <= color3[1] <= green_upper[1] and green_lower[2] <= color3[2] <= green_upper[2]:
                        color3 = 'green'
                    elif blue_lower[0] <= color3[0] <= blue_upper[0] and blue_lower[1] <= color3[1]<= blue_upper[1] and blue_lower[2] <= color3[2] <= blue_upper[2]:
                        color3 = 'blue' 
                    elif lower_yellow[0] <= color3[0] <= upper_yellow[0] and lower_yellow[1] <= color3[1]<= upper_yellow[1] and lower_yellow[2] <= color3[2] <= upper_yellow[2]:
                        color3 = 'Yellow'
                    elif lower_dark_teal[0] <= color3[0] <= upper_dark_teal[0] and lower_dark_teal[1] <= color3[1]<= upper_dark_teal[1] and lower_dark_teal[2] <= color3[2] <= upper_dark_teal[2]:
                        color3 = 'Dark Color' 
                    elif lower_bright_teal[0] <= color3[0] <= upper_bright_teal[0] and lower_bright_teal[1] <= color3[1]<= upper_bright_teal[1] and lower_bright_teal[2] <= color3[2] <= upper_bright_teal[2]:
                        color3 = 'Bright Color'
                    else:
                        color3 = 'Other'
                    print("No. of cars detected on 2nd lane: {}, Color: {} ".format(str(cars3), color3))

                        

                elif x > 870 and x <= 1200:
                    cars4 += 1  
                    cars+=1                         
                    cv2.line(frame, (870, line_pos), (1100, line_pos), (0, 127, 255), 3)                         
                    detection.remove((x, y))
                    c4hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                    color4 = c4hsv[center[1], center[0]]
                    print(color4)
                    if red_lower[0] <= color4[0] <= red_upper[0] and red_lower[1] <= color4[1]<= red_upper[1] and red_lower[2] <= color4[2] <= red_upper[2]:
                        color4 =  'red'
                    elif green_lower[0] <= color4[0] <= green_upper[0] and green_lower[1] <= color4[1]<= green_upper[1] and green_lower[2] <= color4[2] <= green_upper[2]:
                        color4 = 'green'
                    elif blue_lower[0] <= color4[0] <= blue_upper[0] and blue_lower[1] <= color4[1]<= blue_upper[1] and blue_lower[2] <= color4[2] <= blue_upper[2]:
                        color4 = 'blue' 
                    elif lower_yellow[0] <= color4[0] <= upper_yellow[0] and lower_yellow[1] <= color4[1]<= upper_yellow[1] and lower_yellow[2] <= color4[2] <= upper_yellow[2]:
                        color4 = 'Yellow'
                    elif lower_dark_teal[0] <= color4[0] <= upper_dark_teal[0] and lower_dark_teal[1] <= color4[1]<= upper_dark_teal[1] and lower_dark_teal[2] <= color4[2] <= upper_dark_teal[2]:
                        color4 = 'Dark Color' 
                    elif lower_bright_teal[0] <= color4[0] <= upper_bright_teal[0] and lower_bright_teal[1] <= color4[1]<= upper_bright_teal[1] and lower_bright_teal[2] <= color4[2] <= upper_bright_teal[2]:
                        color4 = 'Bright Color'
                    else:
                        color4 = 'Other'
                    print("No. of cars detected on 2nd lane: {}, Color: {} ".format(str(cars4), color4))


    cv2.putText(frame, "Cars 1st lane: "+str(cars1), (30, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.putText(frame, "Cars 2nd lane: "+str(cars2), (30, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.putText(frame, "Cars 3rd lane: "+str(cars3), (30, 150), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.putText(frame, "Cars 4th lane: "+str(cars4), (30, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 4)
    cv2.putText(frame, "Cars, Total: "+str(cars), (30, 250), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 0), 4)

    cv2.imshow("Video Original", frame)
    cv2.imshow(" Thresh ", thresh)
    
    if cv2.waitKey(30) == 27:

        break   
     

cv2.destroyAllWindows()
cap.release()
