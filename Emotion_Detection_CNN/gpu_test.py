# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 13:14:56 2018

@author: Abhishek
"""

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense #to add fully connected layer to ANN


import tensorflow as tf
with tf.device('/gpu:0'):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)

with tf.Session() as sess:
    print (sess.run(c))
    

with tf.Session() as sess:
  devices = sess.list_devices()

print(devices)


from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())



#to check if requested GPU is available.
tf.test.is_gpu_available(
    cuda_only=False,
    min_cuda_compute_capability=None
)

import tensorflow as tf
if tf.test.gpu_device_name():
 print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
 print('Please install GPU version of TF')