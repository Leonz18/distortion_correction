__author__ = 'Leon'
# -*- coding: utf-8 -*-

import cv2
import numpy as np
# from get_box_corners import get_box_corners

# #读入图像
# filename = 'flood_fill.jpg' 
# img = cv2.imread(filename)
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray_img = np.float32(gray_img)
# image = cv2.medianBlur(gray_img, 3)


def box_corners_1(img):
    img = cv2.medianBlur(img, 3)
    #在图像中提取角点
    corners = cv2.goodFeaturesToTrack(img, 12, 0.05, 10)
    
    # 显示角点
    # for i in range(len(corners)):
        # for x, y in corners[i]:
            # cv2.circle(img, (x, y), 20, (255, 0, 0), 3)
    # cv2.namedWindow('corners', cv2.WINDOW_NORMAL) 
    # cv2.imshow('corners', img)
    # cv2.waitKey(0)

    return corners
    
# corners = box_corners(image)
# box = get_box_corners(corners, img.shape[0], img.shape[1])
# print(box)

