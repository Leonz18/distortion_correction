__author__ = 'Leon'
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from flood_fill_2 import flood_fill_2
from corners_detection_2 import get_box_2
from perspective_transformation_2 import perspective_transformation_2


def transform_2(img):
    # 读取图片
    # filename = 'temp.jpg' 
    # img = cv2.imread(filename)

    # 转化成灰度图，二值化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh0 = cv2.threshold(gray, 140, 255, cv2.THRESH_TOZERO_INV)
    ret, thresh = cv2.threshold(thresh0, 60, 255, cv2.THRESH_BINARY)
    # cv2.namedWindow('thresh', cv2.WINDOW_NORMAL) 
    # cv2.imshow('thresh', thresh)
    # cv2.waitKey(0)

    # 膨胀腐蚀
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilation = cv2.dilate(thresh, element, iterations=3)
    # erosion = cv2.erode(dilation, element, iterations = 3)
    # cv2.namedWindow('dilation', cv2.WINDOW_NORMAL) 
    # cv2.imshow('dilation', dilation)
    # cv2.imwrite('binary.jpg', dilation)
    # cv2.namedWindow('erosion', cv2.WINDOW_NORMAL) 
    # cv2.imshow('erosion', erosion)

    # 漫水填充
    # filename = 'flood_image.jpg' 
    # dilation = cv2.imread(filename)
    flood_image = flood_fill_2(dilation)
    # flood_image = flood_fill(erosion)

    # 提取角点并筛选
    corners = get_box_2(flood_image)
    print(corners)
    box = np.zeros((4, 2), dtype="float32")
    box[0][0] = corners[1][0]
    box[0][1] = corners[1][1]
    box[1][0] = corners[2][0]
    box[1][1] = corners[2][1]
    box[2][0] = corners[0][0]
    box[2][1] = corners[0][1]
    box[3][0] = corners[3][0]
    box[3][1] = corners[3][1]

    # 在图上绘制提取到的角点
    # for i in range(len(corners)):
    # cv2.circle(img, (corners[i][0], corners[i][1]), 10, (0, 0, 255), 3)
    # cv2.namedWindow('corners', cv2.WINDOW_NORMAL) 
    # cv2.imshow('corners', img)
    # cv2.waitKey(0)

    # 透视变换p
    dst = perspective_transformation_2(img, box)

    return dst
# transform_2()
