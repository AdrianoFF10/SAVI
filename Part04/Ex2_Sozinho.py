

import cv2
import copy
import csv
import numpy as np
from random import randint
from track_sozinho import Track
from colorama import Fore, Back, Style

# Initialization  -------------------
cap = cv2.VideoCapture('/home/adrianoff10/Desktop/savi_23-24/Parte04/docs/OxfordTownCentre/TownCentreXVID.mp4')

file = '/home/adrianoff10/Desktop/savi_23-24/Parte04/docs/OxfordTownCentre/TownCentre-groundtruth.top'
get_tracks = csv.reader(open(file))

video_frame = 0
tracks = {}

# Execution  ------------------------

while cap.isOpened():

    ret, video = cap.read()
    if not ret:
        break
    
    image_gui = copy.deepcopy(video)
    get_tracks = csv.reader(open(file))

    height, width,_ = video.shape

    for row_idx, get_track in enumerate(get_tracks):

        if not len(get_track) == 12:  # column 12 does not work well, so dont use it!
            continue
        
        person_number, file_frame_number, head_valid, body_valid, head_left, head_top, head_right, head_bottom, body_left, body_top, body_right, body_bottom = get_track
        file_frame_number = int(file_frame_number)
        person_number = int(float(person_number))
        body_left = int(float(body_left))
        body_right = int(float(body_right))
        body_top = int(float(body_top))
        body_bottom = int(float(body_bottom))

        if video_frame == file_frame_number:    # Analysing the same frame in the video and the file with information
            
            if body_valid is False:   #Verify is the person is in this frame
                continue

            if person_number in tracks:   #Need to update this position

                #print(Fore.YELLOW + 'Person ' + str(person_number) + ' already being tracked. Updating!'+ Style.RESET_ALL)
                tracks[person_number].update(body_left, body_right, body_top, body_bottom)
                tracks[person_number].draw2(image_gui)
                print(tracks[0])
            else:    #Need to add this person
                 
                 #print(Fore.BLUE + 'Person ' + str(person_number) + ' not tracked. Creating new!' + Style.RESET_ALL)
                 color = (randint(0,255), randint(0,255), randint(0,255))
                 track = Track(person_number, body_left, body_right, body_top, body_bottom, color=color)
                 tracks[person_number] = track
                 track.draw2(image_gui)

    #Visualization  -------------------------------

    cv2.namedWindow('Image GUI', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image GUI', width//2, height//2)
    cv2.imshow('Image GUI', image_gui)

    if cv2.waitKey(25) & 0xFF==27:
        break

    video_frame +=1








