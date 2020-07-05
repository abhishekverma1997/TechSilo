# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:58:41 2020

@author: Abhishek
"""

import array 
import cv2 
# initializing array with array values 
# initializes array with signed integers 
arr = array.array('i', [1, 2, 3])  

filelist = []

import glob


for imgName in glob.glob('*.JPG'):
    image = cv2.imread(imgName)
    #cv2.imshow("original", image)
    cv2.waitKey(0)
    # print the dimensions of the image
    print (image.shape)
    
    # we need to keep in mind aspect ratio so the image does
    # not look skewed or distorted -- therefore, we calculate
    # the ratio of the new image to the old image
    r = 512.0 / image.shape[1]
    dim = (600, int(image.shape[0] * r))
     
    # perform the actual resizing of the image and show it
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    #cv2.imshow("resized", resized)
    cv2.waitKey(0)
    cv2.imwrite(imgName, resized, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

 
# load the image and show it
image = cv2.imread(filelist[0])
cv2.imshow("original", image)
cv2.waitKey(0)