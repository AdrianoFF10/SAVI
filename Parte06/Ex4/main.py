#!/usr/bin/env python3
# Sistemas Avançados de Visão Industrial (SAVI 22-23)
# Miguel Riem Oliveira, DEM, UA


from copy import deepcopy
from random import randint

import cv2


def main():

    # --------------------------------------
    # Initialization
    # --------------------------------------
    train_image = cv2.imread("Parte06/images/castle/1.png")
    query_image = cv2.imread("Parte06/images/castle/2.png")

    train_image_gui = deepcopy(train_image)
    query_image_gui = deepcopy(query_image)

    height_t, width_t, nc_t = train_image.shape
    height_q, width_q, nc_q = query_image.shape
    # print(query_image.shape)
    # print(train_image.shape)

    # --------------------------------------
    # Execution
    # --------------------------------------

    # Sift features  -----------------------
    sift_detector = cv2.SIFT_create(nfeatures=100)

    t_key_points, t_descriptors = sift_detector.detectAndCompute(train_image, None)
    q_key_points, q_descriptors = sift_detector.detectAndCompute(query_image, None)

    # Match the keypoints
    index_params = dict(algorithm = 1, trees = 15)
    search_params = dict(checks = 50)
    flann_matcher = cv2.FlannBasedMatcher(index_params, search_params)
    two_best_matches = flann_matcher.knnMatch(q_descriptors, t_descriptors, k=2)

    # Create a list of matches
    matches = []
    for match_idx, match in enumerate(two_best_matches):

        best_match = match[0] # to get the cv2.DMatch from the tuple [match = (cv2.DMatch)]
        second_match = match[1]

        # David Lowe's ratio
        if best_match.distance < 0.3 * second_match.distance: # this is a robust match, keep it
            matches.append(best_match) # create a list to show with drawMatches

    matches_image = cv2.drawMatches(query_image, q_key_points, train_image, t_key_points, matches, None)


    # Visualization -----------------------

    # Draw the keypoints on the images
    for key_point in t_key_points: # iterate all keypoints
        x, y = int(key_point.pt[0]), int(key_point.pt[1])
        color = (randint(0, 255), randint(0, 255),randint(0, 255))
        cv2.circle(train_image_gui, (x,y), 15, color, 1)

    for key_point in q_key_points: # iterate all keypoints
        x, y = int(key_point.pt[0]), int(key_point.pt[1])
        color = (randint(0, 255), randint(0, 255),randint(0, 255))
        cv2.circle(query_image_gui, (x,y), 15, color, 1)

    cv2.namedWindow('train image', cv2.WINDOW_NORMAL)
    cv2.imshow('train image', train_image_gui)

    cv2.namedWindow('query image', cv2.WINDOW_NORMAL)
    cv2.imshow('query image', query_image_gui)

    cv2.namedWindow('matches image', cv2.WINDOW_NORMAL)
    cv2.imshow('matches image', matches_image)

    cv2.waitKey(0)
    # --------------------------------------
    # Termination
    # --------------------------------------


if __name__ == "__main__":
    main()
