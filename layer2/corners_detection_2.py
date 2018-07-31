__author__ = 'Leon'
# -*- coding: utf-8 -*-

import cv2
import numpy as np
 
# img = cv2.imread('2.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# # binary_inv = cv2.bitwise_not(binary)
# # cv2.namedWindow('binary_inv', 0) 
# # cv2.imshow("binary_inv", binary_inv)


def get_box_2(binary): 
    _, contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    # cv2.drawContours(img,contours,-1,(0,255,0),2)

    for i in range(0,len(contours)):
        cnt = contours[i]
        if cv2.contourArea(cnt) < 1000:
            continue
        
        # 轮廓近似
        # epsilon = 0.1*cv2.arcLength(cnt,True)
        # approx = cv2.approxPolyDP(cnt,epsilon,True)
        # cv2.drawContours(img,[approx],-1,(0,255,0),2)
        # # hull = cv2.convexHull([approx])
        
        # 最小外接矩阵
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        # box = np.int0(box)
        # im = cv2.drawContours(img,[box],0,(0,0,255),2)
        
        # 极点
        # leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
        # cv2.circle(img, leftmost, 20, (255, 0, 0), 3)
        # rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
        # cv2.circle(img, rightmost, 20, (255, 0, 0), 3)
        # topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
        # cv2.circle(img, topmost, 20, (255, 0, 0), 3)
        # bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
        # cv2.circle(img, bottommost, 20, (255, 0, 0), 3)

    # cv2.namedWindow('img', 0) 
    # cv2.imshow("img", img)
    # cv2.waitKey(0)
    
    return box
