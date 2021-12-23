# -*- coding: utf-8 -*-
"""CBÜ Workshop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GBIIG6YHFP-C-OwpteKAZIFFzY8JxPd7
"""

from tensorflow import keras

(train_images, train_labels), (test_images, test_labels) = keras.datasets.cifar10.load_data()

train_images, test_images = train_images / 255, test_images / 255

from keras import layers, models, losses

model = models.Sequential()

train_images.shape[0] + test_images.shape[0]

#Feature Learning
model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(32,32,3))) #input 
model.add(layers.MaxPooling2D())
model.add(layers.Conv2D(64, (3,3), activation="relu"))
model.add(layers.MaxPooling2D())
model.add(layers.Conv2D(64, (3,3), activation = "relu"))
model.add(layers.MaxPooling2D())

#Classification
model.add(layers.Flatten())
model.add(layers.Dense(64, activation = "relu"))
model.add(layers.Dense(10))

model.compile(optimizer="adam", 
              loss = losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

data_generator = ImageDataGenerator(
    rotation_range=40,
    width_shift_range = 0.2,
    height_shift_range = 0.2,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
    fill_mode = 'nearest'
)

data_generator.fit(train_images)

train_labels.shape

train_images.shape

model.fit(data_generator.flow(train_images, train_labels), batch_size = 512,
                              steps_per_epoch = len(train_images)/512,
                              epochs = 15, verbose = 1)

loss = model.evaluate(data_generator.flow(test_images, test_labels), batch_size=512)

class_name= ["airplane", "automobile","bird","cat","deer","dog","frog","horse", "ship","truck"]

import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing import image

img = image.load_img("/content/dog.jpg", target_size=(32,32,3))

img = image.load_img("/content/download.jpeg", target_size=(32,32,3))

img_array = image.img_to_array(img)
img_array = img_array / 255
reshaped_img_array = img_array.reshape((1,)+img_array.shape)

plt.figure()
plt.imshow(img_array)

prediction = model.predict(reshaped_img_array)

predicted_value = class_name[np.argmax(prediction)]

predicted_value

