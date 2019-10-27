import numpy as np
from alexnet import alexnet
import cv2
import os
from tqdm import tqdm
import tensorflow as tf
IMG_SIZE = 80
EPOCHS = 5
LR = 1e-3
model = alexnet(IMG_SIZE,IMG_SIZE, LR)
#model.load(MODEL_NAME)

MODEL_NAME = 'Flowers-{}-{}-{}-epochs.model'.format(LR, 'alexnet',EPOCHS)
model.load(MODEL_NAME)
#model = alexnet(IMG_SIZE,IMG_SIZE, LR)
# def model():

# 	IMG_SIZE = 80
# 	LR = 1e-3
# 	EPOCHS = 10
# 	MODEL_NAME = 'Flowers-{}-{}-{}-epochs.model'.format(LR, 'alexnet',EPOCHS)
# 	model = alexnet(IMG_SIZE,IMG_SIZE, LR)
# 	model.load(MODEL_NAME)
# 	return model


img = cv2.imread('medialoaded/img1.png',cv2.IMREAD_GRAYSCALE)
im   = cv2.resize(img,(IMG_SIZE,IMG_SIZE))
im =  np.array(im).reshape(IMG_SIZE, IMG_SIZE,1)
im = np.array(im).reshape( IMG_SIZE, IMG_SIZE, 1)
#print(im)
results = model.predict([im])[0]
print(results)
# file = cv2.imread('medialoaded/img1.png',cv2.IMREAD_GRAYSCALE)
# #print(file)
# im   = cv2.resize(np.array(file),(IMG_SIZE,IMG_SIZE))
# im = im.reshape(IMG_SIZE, IMG_SIZE,1)
# print(im.shape)
#print(model.predict(im))


