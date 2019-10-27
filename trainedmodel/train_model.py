# train_model.py

import numpy as np
from alexnet import alexnet
import cv2
import os
from tqdm import tqdm
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import pandas as pd
import warnings
IMG_SIZE = 80
LR = 1e-3
EPOCHS = 100

imdir = '/Users/mac/Documents/Dataset/aptos2019-blindness-detection/train_images/'
mdata =pd.read_csv('/Users/mac/Documents/Dataset/aptos2019-blindness-detection/train.csv')
y = mdata['diagnosis']
def imdata(floder):
	X = []

	for filename in tqdm(os.listdir(floder)):
		im_data = cv2.imread(floder + '/' + filename , cv2.IMREAD_GRAYSCALE)
		if im_data is not None:
			img = cv2.resize(im_data,(IMG_SIZE,IMG_SIZE))
			X.append(img)
	X = np.array(X)
	return X



X = imdata(imdir)

X = X.reshape(-1,IMG_SIZE,IMG_SIZE,1)

X = X/255.0
import time
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.layers import BatchNormalization

model = Sequential()
# 1st Convolutional Layer
model.add(Conv2D(filters=96, input_shape=X.shape[1:], kernel_size=(11,11),\
 strides=(4,4), padding='same'))
model.add(Activation('relu'))
# Pooling 
model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2), padding='same'))
# Batch Normalisation before passing it to the next layer
model.add(BatchNormalization())

model.add(Conv2D(filters=32, kernel_size=(3,3), strides=(2,2), padding='same'))
model.add(Activation('relu'))
# Pooling
model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2), padding='same'))
# Batch Normalisation
model.add(BatchNormalization())

# 3rd Convolutional Layer
model.add(Conv2D(filters=32, kernel_size=(5,5), strides=(1,1), padding='same'))
model.add(Activation('relu'))
# Batch Normalisation
model.add(BatchNormalization())

# 4th Convolutional Layer
model.add(Conv2D(filters=64, kernel_size=(5,5), strides=(1,1), padding='same'))
model.add(Activation('relu'))
# Batch Normalisation
model.add(BatchNormalization())

model.add(Conv2D(filters=64, kernel_size=(5,5), strides=(1,1), padding='same'))
model.add(Activation('relu'))
# Pooling
model.add(MaxPooling2D(pool_size=(3,3), strides=(2,2), padding='same'))
# Batch Normalisation
model.add(BatchNormalization())

# Passing it to a dense layer
model.add(Flatten())
# 1st Dense Layer
model.add(Dense(128, input_shape=(80*80*1,)))
model.add(Activation('relu'))
# Add Dropout to prevent overfitting
model.add(Dropout(0.5))
# Batch Normalisation
# model.add(BatchNormalization())

# # 2nd Dense Layer
# model.add(Dense(4096))
# model.add(Activation('relu'))
# # Add Dropout
# model.add(Dropout(0.5))
# # Batch Normalisation
# model.add(BatchNormalization())

# #3rd Dense Layer
# model.add(Dense(1000))
# model.add(Activation('relu'))
# # Add Dropout
# model.add(Dropout(0.4))
# # Batch Normalisation
# model.add(BatchNormalization())

# Output Layer
model.add(Dense(5))
model.add(Activation('softmax'))
opt = tf.keras.optimizers.Adam(lr=0.001, decay=1e-6)

model.compile(loss='sparse_categorical_crossentropy',
               optimizer=opt,
               metrics=['accuracy'])

model.fit(X, y, batch_size=32, epochs=50,
          validation_split=0.3)

model.save('64x2-CNN.model')

