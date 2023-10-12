#'''

import cv2
import numpy as np

with open('/home/adrianoff10/Desktop/savi_23-24/Parte04/docs/OxfordTownCentre/TownCentre-groundtruth.top','r') as f:
    l = [[float(num) for num in line.split(',')] for line in f]

l = [[int(num) for num in line] for line in l]

video = cv2.VideoCapture("/home/adrianoff10/Desktop/savi_23-24/Parte04/docs/OxfordTownCentre/TownCentreXVID.mp4")
ret, frame = video.read()
frame_height, frame_width = frame.shape[:2]

frame = cv2.resize(frame, (frame_width//2, frame_height//2))

if not ret:
    print('Cannot read the video')

frameNumber = 0

# Create some random colors
color = np.random.randint(0, 255, 3)
color = (int(color[0]), int(color[1]), int(color[2]))

#print(l)
for line in l:   #forma de l :personNumber, frameNumber, headValid, bodyValid, headLeft, headTop, headRight, headBottom, bodyLeft, bodyTop, bodyRight, bodyBottom

    if frameNumber == line[1]:
        print(line)

        ret, frame = video.read()
        frame = cv2.resize(frame, (frame_width//2, frame_height//2))
        frameNumber += 1

        if not ret:
            print('Something went wrong')
            break



    left = line[8] // 2
    top = line[9] // 2
    right = line[10] // 2
    bottom = line[11] // 2
    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
    cv2.circle(frame, ((line[4] // 2 + line[6] // 2) // 2, (line[7] // 2 + line[5] // 2) // 2), 4, color, -1)

    cv2.imshow("Tracking", frame)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
        
video.release()
cv2.destroyAllWindows()

#'''




'''
# import the necessary packages
import numpy as np
import cv2
 
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cv2.startWindowThread()

# open video file
cap = cv2.VideoCapture('/home/adrianoff10/Desktop/savi_23-24/Parte04/docs/OxfordTownCentre/TownCentreXVID.mp4')

# params for ShiTomasi corner detection
feature_params = dict(maxCorners = 100,
                      qualityLevel = 0.3,
                      minDistance = 7,
                      blockSize = 7)

# params for ShiTomasi corner detection
feature_params = dict(maxCorners = 100,
                      qualityLevel = 0.3,
                      minDistance = 7,
                      blockSize = 7)

# Parameters for lucas kanade optical flow
lk_params = dict( winSize = (15, 15), maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0, 255, (100, 3))

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

# the output will be written to output.avi
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 15., (640,480))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print('Could not read file')
        break

    # resizing for faster detection
    #frame = cv2.resize(frame, (640, 480))
    # using a greyscale picture, also for faster detection
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(frame, winStride=(4,4), padding = (8,8), scale = 1.2)

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB),
                          (0, 255, 0), 2)
    
    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)


    # Select good points
    if p1 is not None:
        good_new = p1[st==1]
        good_old = p0[st==1]

    # draw the tracks
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)
        frame = cv2.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)
        img = cv2.add(frame, mask)

    # Write the output video 
    out.write(frame.astype('uint8'))
    # Display the resulting frame
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)
    
# When everything done, release the capture
cap.release()
# and release the output
out.release()
# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)
'''

'''

import cv2
import numpy as np

with open('/home/adrianoff10/Desktop/savi_23-24/Parte04/docs/OxfordTownCentre/TownCentre-groundtruth.top','r') as f:
    l = [[float(num) for num in line.split(',')] for line in f]

l = [[int(num) for num in line] for line in l]

video = cv2.VideoCapture("/home/adrianoff10/Desktop/savi_23-24/Parte04/docs/OxfordTownCentre/TownCentreXVID.mp4")
ret, frame = video.read()
frame_height, frame_width = frame.shape[:2]

frame = cv2.resize(frame, (frame_width//2, frame_height//2))

ret, old_frame = video.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# Create a mask image for drawing purposes
mask = np.zeros_like(frame)

if not ret:
    print('Cannot read the video')

frameNumber = 0

# Parameters for lucas kanade optical flow
lk_params = dict( winSize = (15, 15), maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0, 255, (100, 3))


#print(l)
for line in l:   #forma de l :personNumber, frameNumber, headValid, bodyValid, headLeft, headTop, headRight, headBottom, bodyLeft, bodyTop, bodyRight, bodyBottom

    if frameNumber == line[1]:
        print(line)

        ret, frame = video.read()
        frame = cv2.resize(frame, (frame_width//2, frame_height//2))
        frameNumber += 1
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if not ret:
            print('Something went wrong')
            break
    
    p0 = ((line[4] // 2 + line[6] // 2) // 2, (line[7] // 2 + line[5] // 2) // 2)

    # calculate optical flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # Select good points
    if p1 is not None:
        good_new = p1[st==1]
        good_old = p0[st==1]

    # draw the tracks
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)
        frame = cv2.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)
        img = cv2.add(frame, mask)

    left = line[8] // 2
    top = line[9] // 2
    right = line[10] // 2
    bottom = line[11] // 2
    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
    #cv2.circle(frame, ((line[4] // 2 + line[6] // 2) // 2, (line[7] // 2 + line[5] // 2) // 2), 4, color, -1)

    cv2.imshow("Tracking", frame)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

     # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)
        
video.release()
cv2.destroyAllWindows()

'''


