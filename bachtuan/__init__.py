#http://blog.asilla.vn/2019/04/06/chan-doan-benh-viem-phoi-bang-tri-tue-nhan-tao-step-by-step/?fbclid=IwAR14uoR5oAfuZ_fnGIH38bzGgygmepMHyhCkUs3gWHxhONImYsEO0tL3Q3o

from keras.layers import Input, Lambda, Dense, Flatten
from keras.models import Model
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
from keras.models import load_model
import numpy as np
from glob import glob
import matplotlib.pyplot as plt

IMAGE_SIZE = [224, 224]
BATCH_SIZE = 8
NUM_EPOCH = 10

train_path = '/content/gdrive/My Drive/AI_BACHTUAN/chest_xray/train'
valid_path = '/content/gdrive/My Drive/AI_BACHTUAN/chest_xray/val'

vgg = VGG16(input_shape=IMAGE_SIZE + [3], weights='imagenet', include_top=False)
for layer in vgg.layers:
    layer.trainable = False

folders = glob('/content/gdrive/My Drive/AI_BACHTUAN/chest_xray/train/*')
x = Flatten()(vgg.output)
prediction = Dense(len(folders), activation='softmax')(x)
model = Model(inputs=vgg.input, outputs=prediction)
model.summary()

model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
    train_path,
    target_size=(224, 224),
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

valid_set = test_datagen.flow_from_directory(
    valid_path,
    target_size=(224, 224),
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

r = model.fit_generator(
    training_set,
    validation_data=valid_set,
    epochs=NUM_EPOCH,
    steps_per_epoch=len(training_set),
    validation_steps=len(valid_set)
)

plt.plot(r.history['loss'], label='train loss')
plt.plot(r.history['val_loss'], label='val loss')
plt.legend()
plt.show()
plt.savefig('LossVal_loss')

plt.plot(r.history['acc'], label='train acc')
plt.plot(r.history['val_acc'], label='val acc')
plt.legend()
plt.show()
plt.savefig('AccVal_acc')

model.save('model_vgg19.h5')