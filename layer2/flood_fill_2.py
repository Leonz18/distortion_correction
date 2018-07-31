__author__ = 'Leon'
# -*- coding: utf-8 -*-

import cv2
import numpy as np


def fill_hole(img):
    # Read image
    # im_in = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    im_in = img 
    # Threshold.
    # Set values equal to or above 220 to 0.
    # Set values below 220 to 255.
     
    th, im_th = cv2.threshold(im_in, 220, 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow("Thresholded Image", im_th)
    # Copy the thresholded image.
    im_floodfill = im_th.copy()
     
    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = im_th.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
     
    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (1500,900), 255)
    # cv2.imshow("Floodfilled Image", im_floodfill) 
    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    # cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv) 
    # Combine the two images to get the foreground.
    im_out = im_th | im_floodfill_inv
    im_out = 255 - im_out
     
    # Display images.
    cv2.namedWindow('Foreground0',cv2.WINDOW_NORMAL)
    cv2.imshow("Foreground0", im_out)
    cv2.waitKey(0)
    
    return im_out

    
def fill_hole_inv(img):
    # Read image
    im_in = img
     
    # Threshold.
    # Set values equal to or above 220 to 0.
    # Set values below 220 to 255.
     
    th, im_th = cv2.threshold(im_in, 220, 255, cv2.THRESH_BINARY)
    # cv2.namedWindow('Thresholded Image',cv2.WINDOW_NORMAL)
    # cv2.imshow("Thresholded Image", im_th)
    # Copy the thresholded image.
    im_floodfill = im_th.copy()
     
    # Mask used to flood filling.
    # Notice the size needs to be 2 pixels than the image.
    h, w = im_th.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)
     
    # Floodfill from point (0, 0)
    cv2.floodFill(im_floodfill, mask, (100,0), (255,255,255), 0 , 255)
    # cv2.namedWindow('Floodfilled Image',cv2.WINDOW_NORMAL)
    # cv2.imshow("Floodfilled Image", im_floodfill) 
    # Invert floodfilled image
    im_floodfill_inv = cv2.bitwise_not(im_floodfill)
    # cv2.namedWindow('Inverted Floodfilled Image',cv2.WINDOW_NORMAL)
    # cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv) 
    # Combine the two images to get the foreground.
    im_out = im_th | im_floodfill_inv
    # im_out = 255 - im_out

    # # Display images.
    # cv2.namedWindow('Foreground1',cv2.WINDOW_NORMAL)
    # cv2.imshow("Foreground1", im_out)
    # cv2.waitKey(0)
    
    return im_out

binary = cv2.imread('binary.jpg')
# fill_hole_inv(binary)    

def flood_fill_2(image):    
    # temp = fill_hole(image)
    dst = fill_hole_inv(image)
    element = cv2.getStructuringElement(cv2.MORPH_RECT,(5, 5))
    dilation = cv2.dilate(dst, element, iterations = 2)
    erosion = cv2.erode(dilation, element, iterations = 4)
    # cv2.namedWindow('result',cv2.WINDOW_NORMAL)
    # cv2.imshow("result", dilation)
    cv2.imwrite("flood_fill.jpg", erosion)
    # cv2.waitKey(0)
    
    return erosion

# flood_fill_2(binary)
