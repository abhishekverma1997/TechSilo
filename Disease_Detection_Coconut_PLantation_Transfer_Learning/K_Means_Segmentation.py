# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:35:35 2020

@author: Abhishek
"""

#import cv2 
import glob
#import matplotlib.pyplot as plt


import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

for imgName in glob.glob('*.JPG'):
    pic = plt.imread(imgName)/255 
    print(pic.shape)
    pic_n = pic.reshape(pic.shape[0]*pic.shape[1], pic.shape[2])
    pic_n.shape
    kmeans = KMeans(n_clusters=5, random_state=0).fit(pic_n)
    pic2show = kmeans.cluster_centers_[kmeans.labels_]    
    cluster_pic = pic2show.reshape(pic.shape[0], pic.shape[1], pic.shape[2])    
    plt.imshow(cluster_pic)   
    plt.savefig(imgName, bbox_inches='tight', pad_inches=0)
    plt.close()
    