__author__ = 'Leon'
# -*- coding: utf-8 -*-

import cv2
from flood_fill_1 import flood_fill_1
from corners_detection_1 import box_corners_1
from get_box_corners_1 import get_box_corners_1
from perspective_transformation_1 import perspective_transformation_1


def transform_1(img):
    # 读取图片
    # filename = '2.jpg' 
    # img = cv2.imread(filename)

    # 转化成灰度图，二值化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh0 = cv2.threshold(gray, 180, 255, cv2.THRESH_TOZERO_INV)
    ret, thresh = cv2.threshold(thresh0, 50, 255, cv2.THRESH_BINARY)

    # 膨胀腐蚀
    element = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    dilation = cv2.dilate(thresh, element, iterations=3)
    # erosion = cv2.erode(dilation, element, iterations = 3)

    # 漫水填充
    flood_image = flood_fill_1(dilation)
    # flood_image = flood_fill(erosion)

    # 提取角点并筛选
    box = box_corners_1(flood_image)
    corners = get_box_corners_1(box, img.shape[0], img.shape[1])

    # 在图上绘制提取到的角点
    # for i in range(len(corners)):
    # cv2.circle(img, (corners[i][0], corners[i][1]), 10, (0, 0, 255), 3)
    # cv2.namedWindow('corners', cv2.WINDOW_NORMAL) 
    # cv2.imshow('corners', img)
    # cv2.waitKey(0)

    # 透视变换p
    dst = perspective_transformation_1(img, corners)

    return dst

# transform_1()
