# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 20:22:30 2020

@author: Abhishek
"""

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# Initialising the CNN
classifier = Sequential() #object of class sequential.

# Step 1 - Convolution
classifier.add(Convolution2D(32, (3, 3), input_shape = (160, 160, 3), activation = 'relu'))
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

# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size = (160, 160),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size = (160, 160),
                                            batch_size = 32,
                                            class_mode = 'binary')

classifier.fit_generator(training_set,
                         steps_per_epoch = 250,
                         epochs = 25,
                         validation_data = test_set,
                         validation_steps = 32)


classifier.save('C:/Users/Abhishek V/Desktop/Face_mask_classifier/mtcnn_face_mask.h5')