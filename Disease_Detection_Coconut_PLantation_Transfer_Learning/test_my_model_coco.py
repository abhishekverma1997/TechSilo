# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 10:54:26 2020

@author: Abhishek
"""

from flask import Flask, request, jsonify, url_for, render_template
import uuid
import os
from tensorflow.keras.models import load_model
import numpy as np
from werkzeug import secure_filename
from tensorflow.keras.applications import MobileNet
from PIL import Image, ImageFile
from io import BytesIO
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input
from tensorflow.keras.applications.mobilenet import decode_predictions

import cv2
import numpy as np


ALLOWED_EXTENSION  =set(['txt', 'pdf', 'png','JPG','jpeg','gif', 'jpg'])
#IMAGE_HEIGHT =224
#IMAGE_WIDTH = 224
#IMAGE_CHANNELS = 3
os.chdir(r'C:\Users\Abhishek V\Desktop\test_my_coco_model')

def allowed_file(filename):
    return '.' in filename and \
     filename.rsplit('.',1)[1] in ALLOWED_EXTENSION


#-----------------------------------------------------------------------

app = Flask(__name__)
#model = MobileNet(weights='imagenet', include_top=True)




def create_model():
    
    from keras.models import Sequential
    from keras.layers import Convolution2D
    from keras.layers import MaxPooling2D
    from keras.layers import Flatten
    from keras.layers import Dense
     
    classifier = Sequential() #object of class sequential.

    # Step 1 - Convolution
    classifier.add(Convolution2D(32, (3, 3), input_shape = (64, 64, 3), activation = 'relu'))
    #(32-no of filters/feature map, no of rows & col of feature detector matrix,I_shape=3-no of channel
    #colour image, 64*64 format for image converstion, )
    
    # Step 2 - Pooling
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    # to reduce no. of nodes in flattening, 2,2 to size the mat that slides over.
    # Adding a second convolutional layer
    classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
    classifier.add(MaxPooling2D(pool_size = (2, 2)))
    
    # Step 3 - Flattening
    classifier.add(Flatten())
    
    # Step 4 - Full connection
    classifier.add(Dense(activation="relu", units=128)) #rectifier A FN for input/hidden layer.
    classifier.add(Dense(activation="sigmoid", units=1)) #sigmoid layer.
    
    #classifier.add(Dense())
    # Compiling the CNN
    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    

    return classifier

new_model=create_model()

new_model.load_weights('first_try_Kmeans.h5')

new_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


@app.route('/index')
def index():
    return render_template('ImageML.html')

@app.route('/api/image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return render_template('ImageML.html', prediction='No posted image. Should be attribute named image')
    file = request.files['image']
    
    if file.filename =='':
        return render_template('ImageML.html', prediction = 'You did not select an image')
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        print("***"+filename)
        x = []
        ImageFile.LOAD_TRUNCATED_IMAGES = False
        img = Image.open(BytesIO(file.read()))
        img.load()
        img  = img.resize((64, 64), Image.ANTIALIAS)
        
        
        x  = image.img_to_array(img)
        
        x = np.expand_dims(x, axis=0)
        #x  = preprocess_input(x)
        pred = new_model.predict(x)
        
        a=pred[0][0]
        if a==0.0:
            return render_template('ImageML.html', prediction = 'Plant is Healthy')
        elif a==1.0:
            return render_template('ImageML.html', prediction = 'Plant is ***NOT HEALTHY*** --->Stem Bleeding/Beetle Hole<---  REMEDIES --->> ::: Apply 200g Phosphobacteria and 200 g Azotobactor mixed with 50kg of FYM/palm. ::: Apply FYM 50kg + neem cake 5 Kg once in 6 months along with fertilizers. ::: Apply FYM 50kg + neem cake 5 Kg once in 6 months along with fertilizers.')
        else:
            return render_template('ImageML.html', prediction = 'Disease Not Detected')
        
        
        
if __name__ == '__main__':
    app.run(host='172.20.51.158', debug=True, use_reloader=False)
