

import copy
import csv
import time
from random import randint

import cv2
import numpy as np
from matplotlib import cm
from track import Track
from colorama import Fore, Back, Style

# --------------------------------------
# Initialization
# --------------------------------------
cap = cv2.VideoCapture('/home/adrianoff10/Desktop/savi_23-24/Parte04/docs/OxfordTownCentre/TownCentreXVID.mp4')

file ='/home/adrianoff10/Desktop/savi_23-24/Parte04/docs/OxfordTownCentre/TownCentre-groundtruth.top'
gt_tracks = csv.reader(open(file))


video_frame_number = 0
tracks = {}

# assume that I will have no more than 160 person ids
#colormap = cm.hsv(np.linspace(0, 1, 160))


# --------------------------------------
# Execution
# --------------------------------------
while(cap.isOpened()): # iterate video frames

    
    result, image_rgb = cap.read() # Capture frame-by-frame
    if result is False:
        break

    height, width, _ = image_rgb.shape
    image_gui = copy.deepcopy(image_rgb) # good practice to have a gui image for drawing


    # Process ground truth
    gt_tracks = csv.reader(open(file))
    for row_idx, gt_track in enumerate(gt_tracks): # iterate file rows

        if not len(gt_track) == 12: # something wrong with this track, so don't use it
            continue

        person_number, file_frame_number, head_valid, body_valid, head_left, head_top, head_right, head_bottom, body_left, body_top, body_right, body_bottom = gt_track
        file_frame_number = int(file_frame_number)

        #print('row idx ' + str(row_idx) + ' has information ' + str(gt_track))
        # TODO compact this with Bruno's list comprehension
        person_number = int(float(person_number))
        body_left = int(float(body_left))
        body_right = int(float(body_right))
        body_top = int(float(body_top))
        body_bottom = int(float(body_bottom))

        if video_frame_number == file_frame_number:
            # print('row idx ' + str(row_idx) + ' has information ' + str(gt_track))
            if body_valid == False: # cannot draw invalid body
                continue

            print('testing if person ' + str(person_number) + ' is in tracks'  + str(list(tracks.keys())))
            if person_number in tracks: # run update of existing track
                print(Fore.YELLOW + 'Person ' + str(person_number) + ' already being tracked. Updating!'+ Style.RESET_ALL)
                tracks[person_number].update(body_left, body_right, body_top, body_bottom)
                tracks[person_number].draw(image_gui)

            else: # create new track and add to dictionary
                print(Fore.BLUE + 'Person ' + str(person_number) + ' not tracked. Creating new!' + Style.RESET_ALL)
                #color = list(colormap[person_number, 0:3]*255)
                # TODO list comprehensions here also
                color = (randint(0, 255), randint(0, 255), randint(0, 255))
                track = Track(person_number, body_left, body_right, body_top, body_bottom, color=color)
                tracks[person_number] = track
                track.draw(image_gui)

    #print(tracks)
            
    # --------------------------------------
    # Visualization
    # --------------------------------------
    cv2.namedWindow('GUI',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('GUI', int(width/2), int(height/2))
    cv2.imshow('GUI',image_gui)
        
    if cv2.waitKey(25) & 0xFF == ord('q') :
        break

    video_frame_number += 1



