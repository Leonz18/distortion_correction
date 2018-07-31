__author__ = 'Leon'
# -*- coding: utf-8 -*-

import cv2
import numpy as np
# from corners_detection import box_corners

def get_distance(vec1, vec2):
    return ((vec1[0]-vec2[0])**2+(vec1[1]-vec2[1])**2)**0.5

def get_box_corners_1(corners, h, w):
    size = len(corners)
    minD = float('inf')
    box = np.zeros((4, 2), dtype="float32")
    x0=0
    y0=0
    
    # 找左上角点
    for i in range(size):
        # print(corners[i])
        for x, y in corners[i]:
            distance = get_distance((x, y), (0, 0))
            if distance < minD:
                minD = distance
                x0 = x
                y0 = y
    box[0][0] = x0-10
    box[0][1] = y0-10
    
    # 找右上角点
    minD = float('inf')
    for i in range(size):
        # print(corners[i])
        for x, y in corners[i]:
            distance = get_distance((x, y), (w, 0))
            if distance < minD:
                minD = distance
                x0 = x
                y0 = y
    box[1][0] = x0+20
    box[1][1] = y0
    
    # 找左下角点
    minD = float('inf')
    for i in range(size):
        # print(corners[i])
        for x, y in corners[i]:
            distance = get_distance((x, y), (0, h))
            if distance < minD:
                minD = distance
                x0 = x
                y0 = y
    box[2][0] = x0
    box[2][1] = y0
    
    # 找右下角点
    minD = float('inf')
    for i in range(size):
        # print(corners[i])
        for x, y in corners[i]:
            distance = get_distance((x, y), (w, h))
            if distance < minD:
                minD = distance
                x0 = x
                y0 = y
    box[3][0] = x0
    box[3][1] = y0
    
    return box
