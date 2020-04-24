# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:00:03 2020

@author: Abhishek
"""

from datetime import datetime
import geocoder
g = geocoder.ip('me')
a=str(g.latlng[0])
b=str(g.latlng[1])
c='GPS::'+a+' '+b


import cv2
from mtcnn.mtcnn import MTCNN
detector = MTCNN()


import numpy as np
from keras.preprocessing.image import img_to_array

from resizeimage import resizeimage
from keras.models import load_model
 

model = load_model("mtcnn_face_mask.h5")

from keras.preprocessing.image import load_img

font = cv2.FONT_HERSHEY_TRIPLEX
font2 = cv2.FONT_HERSHEY_COMPLEX_SMALL
font3 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
font4 = cv2.FONT_HERSHEY_SIMPLEX
#image_file = load_img('test_img.jpg')

#print(chr(169))
#rights=chr(169)+'2020'

cap = cv2.VideoCapture(0)
while True: 
    
    #Capture frame-by-frame
    __, frame = cap.read()
    
    cv2.putText(frame,str(datetime.now()),(10,30), font3, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,c,(10,450), font2, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(frame,'ARR-AB\'s CAM',(480,450), font2, 0.9,(255,255,255),2,cv2.LINE_AA)
    #Use MTCNN to detect faces
    result = detector.detect_faces(frame)
    if result != []:
        for person in result:
            bounding_box = person['box']
            keypoints = person['keypoints']
            #cv2.putText(frame,"The Face",(200,100), font, 1,(255,255,255),2,cv2.LINE_AA)
            cv2.imwrite('opencv.png', frame)
            image_file = load_img('opencv.png')
            cover = resizeimage.resize_cover(image_file, [160, 160], validate=False)


            x = []
            
            
            x = img_to_array(cover)
            
            x = np.expand_dims(x, axis=0)
            
            pred = model.predict(x)
            
            #print(pred[0][0])
            
            if pred[0][0]==0.0:
                cv2.putText(frame,"ACCESS GRANTED, MASK ON",(100,100), font4, 0.8,(0,255,0),2,cv2.LINE_AA)
            
            elif pred[0][0]==1.0:
                cv2.putText(frame,"ACCESS DENIED, No FACE-MASK",(100,100), font4, 0.8,(0,0,255),2,cv2.LINE_AA)
            
            cv2.rectangle(frame,
                          (bounding_box[0], bounding_box[1]),
                          (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                          (0,155,255),
                          2)
    
            cv2.circle(frame,(keypoints['left_eye']), 2, (0,155,255), 2)
            cv2.circle(frame,(keypoints['right_eye']), 2, (0,155,255), 2)
            cv2.circle(frame,(keypoints['nose']), 2, (0,155,255), 2)
            cv2.circle(frame,(keypoints['mouth_left']), 2, (0,155,255), 2)
            cv2.circle(frame,(keypoints['mouth_right']), 2, (0,155,255), 2)
    #display resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(10) &0xFF == ord('q'):
        break
#When everything's done, release capture
cap.release()
cv2.destroyAllWindows()