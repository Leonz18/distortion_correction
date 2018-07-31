__author__ = 'Leon'
# -*- coding:utf-8 -*-

import cv2
import os
from layer1.trans_1 import transform_1
from layer2.trans_2 import transform_2

path = os.path.abspath(os.path.dirname(__file__))


def perspective_transform():
    image_path = os.path.join(path, 'test.jpg')
    image = cv2.imread(image_path)

    temp = transform_1(image)
    dst = transform_2(temp)

    print("done")
    cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    cv2.imshow('img', dst)
    cv2.waitKey()
    return dst

perspective_transform()
