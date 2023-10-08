
#'''
import cv2 as cv

tracker_type = 'BOOSTING'
tracker = cv.legacy.TrackerBoosting_create()

# Get the video file and read it
cap = cv.VideoCapture('/home/adrianoff10/Desktop/savi_23-24/Parte04/docs/OxfordTownCentre/TownCentreXVID.mp4')
ret, frame = cap.read()

frame_height, frame_width = frame.shape[:2]

# Resize the video for a more convenient view
frame = cv.resize(frame, [frame_width//2, frame_height//2])

# Initialize video writer to save the results
output = cv.VideoWriter(f'{tracker_type}.avi', cv.VideoWriter_fourcc(*'XVID'), 60, (frame_width//2, frame_height//2), True) 

if not ret:
    print('Could not reade the video!')

bbox = cv.selectROI(frame, False)
ret = tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    frame = cv.resize(frame, [frame_width//2, frame_height//2])
    if not ret:
        print('Could not read the video')
        break

    timer = cv.getTickCount()
    ret, bbox = tracker.update(frame)
    fps = cv.getTickFrequency() / (cv.getTickCount() - timer)

    if ret:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))   #bbox e do tipo row, col, height, width
        cv.rectangle(frame, p1, p2, (255,0,0), 2, 1)

    else:
        cv.putText(frame, 'Tracking Failure Detection', (100, 80), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)

    cv.putText(frame, tracker_type + " Tracker", (100,20), cv.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
    cv.putText(frame, "FPS : " + str(int(fps)), (100,50), cv.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
    cv.imshow("Tracking", frame)
    output.write(frame)
    k = cv.waitKey(20) & 0xff
    if k == 27 : 
        break
        
cap.release()
output.release()
cv.destroyAllWindows()    

#'''

'''
import cv2

#tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
#tracker_type = tracker_types[5]

#if tracker_type == 'BOOSTING':
#    tracker = cv2.legacy.TrackerBoosting_create()
#if tracker_type == 'MIL':
#    tracker = cv2.TrackerMIL_create() 
#if tracker_type == 'KCF':
#    tracker = cv2.TrackerKCF_create() 
#if tracker_type == 'TLD':
#    tracker = cv2.legacy.TrackerTLD_create() 
#if tracker_type == 'MEDIANFLOW':
#    tracker = cv2.legacy.TrackerMedianFlow_create() 
#if tracker_type == 'GOTURN':
#    tracker = cv2.TrackerGOTURN_create()
#if tracker_type == 'MOSSE':
#    tracker = cv2.legacy.TrackerMOSSE_create()
#if tracker_type == "CSRT":
#    tracker = cv2.TrackerCSRT_create()

tracker_type = 'MOSSE'
tracker = cv2.legacy.TrackerMOSSE_create()

# Get the video file and read it
video = cv2.VideoCapture("/home/adrianoff10/Desktop/savi_23-24/Parte04/docs/OxfordTownCentre/TownCentreXVID.mp4")
ret, frame = video.read()

frame_height, frame_width = frame.shape[:2]
# Resize the video for a more convinient view
frame = cv2.resize(frame, [frame_width//2, frame_height//2])
# Initialize video writer to save the results
output = cv2.VideoWriter(f'{tracker_type}.avi', 
                         cv2.VideoWriter_fourcc(*'XVID'), 60.0, 
                         (frame_width//2, frame_height//2), True)
if not ret:
    print('cannot read the video')
# Select the bounding box in the first frame
bbox = cv2.selectROI(frame, False)
ret = tracker.init(frame, bbox)
# Start tracking
while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, [frame_width//2, frame_height//2])
    if not ret:
        print('something went wrong')
        break
    timer = cv2.getTickCount()
    ret, bbox = tracker.update(frame)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    if ret:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else:
        cv2.putText(frame, "Tracking failure detected", (100,80), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
    cv2.putText(frame, tracker_type + " Tracker", (100,20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
    cv2.imshow("Tracking", frame)
    output.write(frame)
    k = cv2.waitKey(25) & 0xff
    if k == 27 : break
        
video.release()
output.release()
cv2.destroyAllWindows()


'''
