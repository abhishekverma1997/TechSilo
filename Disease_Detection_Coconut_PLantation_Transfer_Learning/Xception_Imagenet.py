# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:48:25 2020

@author: singh
"""

#%%

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import optimizers
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.callbacks import EarlyStopping, ModelCheckpoint
import keras

#%%
# re-size all the images to this
IMAGE_SIZE = [299, 299]

#%%

callbacks = [EarlyStopping(monitor='val_loss', patience=5),
             ModelCheckpoint(filepath='best_model_vgg.h5', monitor='val_loss', save_best_only=True)]

#%%
# add preprocessing layer to the front of VGG
base_model = tf.keras.applications.Xception(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)

#%%
# don't train existing weights
for layer in base_model.layers:
  layer.trainable = False
  
base_model.summary()
 
#%% 

global_average_layer = tf.keras.layers.GlobalAveragePooling2D()

#%%
# our layers - you can add more if you want
prediction_layer = tf.keras.layers.Dense(4, activation='softmax')

#%%
# create a model object
model = tf.keras.Sequential([
  base_model,
  global_average_layer,
  prediction_layer
])

# view the structure of the model
model.summary()

#%%
# tell the model what cost and optimization method to use
model.compile(
  loss='categorical_crossentropy',
  optimizer=optimizers.RMSprop(lr=1e-4),
  metrics=['accuracy']
)


#%%
train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

#%%

test_datagen = ImageDataGenerator(rescale = 1./255)

#%%

training_set = train_datagen.flow_from_directory('dataset6/training_set',
                                                 target_size = IMAGE_SIZE,
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

#%%

test_set = test_datagen.flow_from_directory('dataset6/test_set',
                                            target_size = IMAGE_SIZE,
                                            batch_size = 32,
                                            class_mode = 'categorical')

#%%

validation_set = test_datagen.flow_from_directory('dataset6/validation_set',
                                            target_size = IMAGE_SIZE,
                                            batch_size = 32,
                                            class_mode = 'categorical')

#%%

initial_epochs = 150

#%%
# fit the model
history = model.fit_generator(
  training_set,
  validation_data=validation_set,
  epochs=initial_epochs,
  steps_per_epoch=len(training_set),
  validation_steps=len(validation_set),
  callbacks=callbacks
)

#%%
'''r = model.fit_generator(
  training_set,
  validation_data=test_set,
  epochs=50,
  steps_per_epoch=len(training_set),
  validation_steps=len(test_set)
)'''

#%%

acc = history.history['acc']
val_acc = history.history['val_acc']

loss = history.history['loss']
val_loss = history.history['val_loss']

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.ylabel('Accuracy')
plt.ylim([min(plt.ylim()),1])
plt.title('Training and Validation Accuracy')

plt.subplot(2, 1, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.ylabel('Cross Entropy')
plt.ylim([0,2.0])
plt.title('Training and Validation Loss')
plt.xlabel('epoch')
plt.show()

#%%

base_model.trainable = True

#%%

print("Number of layers in the base model: ", len(base_model.layers))

#%%

fine_tune_at = 17

#%%

for layer in base_model.layers[:fine_tune_at]:
  layer.trainable =  False
  
#%%
  
model.compile(
  loss='categorical_crossentropy',
  optimizer=optimizers.RMSprop(lr=1e-4),
  metrics=['accuracy']
)  

#%%

model.summary()

#%%

len(model.trainable_variables)

#%%
initial_epochs=150
fine_tune_epochs = 50
total_epochs =  initial_epochs + fine_tune_epochs

#%%
history_fine = model.fit_generator(
  training_set,
  validation_data=validation_set,
  epochs=total_epochs,
  initial_epoch=history.epoch[-1],
  steps_per_epoch=len(training_set),
  validation_steps=len(validation_set),
  callbacks=callbacks
)


#%%

acc += history_fine.history['acc']
val_acc += history_fine.history['val_acc']

loss += history_fine.history['loss']
val_loss += history_fine.history['val_loss']

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.ylim([0, 1])
plt.plot([initial_epochs-1,initial_epochs-1],
          plt.ylim(), label='Start Fine Tuning')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(2, 1, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.ylim([0, 2.0])
plt.plot([initial_epochs-1,initial_epochs-1],
         plt.ylim(), label='Start Fine Tuning')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.xlabel('epoch')
plt.show()

#%%

'''acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(len(acc))
plt.plot(epochs, acc, 'r', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.ylabel('accuracy')  
plt.xlabel('epoch')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'r', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.ylabel('loss')  
plt.xlabel('epoch')
plt.legend()
plt.show()'''