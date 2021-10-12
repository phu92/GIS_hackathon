#-*- coding:utf-8 -*-
import pandas as pd
import tensorflow as tf
import numpy as np
from keras.models import load_model
from keras.preprocessing import image


my_model = load_model('my_model.h5')
img_data = image.load_img('이미지 경로', target_size=(180,180))
img_data

img_data = tf.expand_dims(img_data, 0)

predictions = my_model.predict(img_data)
score = tf.nn.softmax(predictions[0])
filenames = ['맑은 날', '흐린 날', '일몰 혹은 일출']
print("해당 사진의 날씨는 {} 입니다." .format(filenames[np.argmax(score)]))