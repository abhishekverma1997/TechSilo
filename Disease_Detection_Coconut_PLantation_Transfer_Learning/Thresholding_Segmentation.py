# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:28:06 2020

@author: Abhishek
"""

import glob
#import matplotlib.pyplot as plt

import numpy as np
import cv2

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



for imgName in glob.glob('*.JPG'):
    img = cv2.imread(imgName,0)
    blur = cv2.GaussianBlur(img,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    plt.imshow(th3)
    plt.savefig(imgName, bbox_inches='tight', pad_inches=0)
    plt.close()