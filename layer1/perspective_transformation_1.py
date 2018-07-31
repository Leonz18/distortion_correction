__author__ = 'Leon'
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('2.jpg')


def perspective_transformation_1(image, pts1):
    # 原图中卡片的四个角点
    # pts1 = np.float32([[135, 96], [1860, 136], [235, 1204], [1751, 1147]])
    # 变换后分别在左上、右上、左下、右下四个点
    pts2 = np.float32([[0, 0], [2048, 0], [0, 1536], [2048, 1536]])

    # 生成透视变换矩阵
    M = cv2.getPerspectiveTransform(pts1, pts2)
    # 进行透视变换
    dst = cv2.warpPerspective(image, M, (2048, 1536))
    cv2.imwrite('dst.jpg', dst)
    # matplotlib默认以RGB通道显示，所以需要用[:, :, ::-1]翻转一下
    plt.subplot(121), plt.imshow(image[:, :, ::-1]), plt.title('input')
    plt.subplot(122), plt.imshow(dst[:, :, ::-1]), plt.title('output')
    plt.show()

    return dst

# perspective_transformation(image, )
