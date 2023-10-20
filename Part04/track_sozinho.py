

import cv2



class Detection:
    
    def __init__(self, left, right, top, bottom):
        
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def draw1(self,image,color,id):

        start_point = (self.left, self.top)
        end_point = (self.right, self.bottom)
        cv2.rectangle(image, start_point, end_point, color, 3)
        cv2.putText(image, 'P: ' + str(id), (self.left, self.top - 7), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3, cv2.LINE_AA)
    
    def setLowerMidpoint(self):
        return((self.left - (self.left - self.right)//2, self.bottom))



class Track:

    def __init__(self, id, left, right, top, bottom, color = (0,255,0)):

        self.id = id
        self.color = color
        self.detections = [Detection(left, right,top, bottom)]

    def draw2(self, image):
        
        self.detections[-1].draw1(image, self.color, self.id)  # Draw the last element

        #Draw tracers
        
        for detection_1, detection2 in zip(self.detections[0:-1], self.detections[1:]):

            start_point = detection_1.setLowerMidpoint()
            end_point = detection2.setLowerMidpoint()     

            cv2.line(image, start_point, end_point, self.color, 3)


    def update(self, left, right, top, bottom):

        self.detections.append(Detection(left, right, top, bottom))   
        

    





