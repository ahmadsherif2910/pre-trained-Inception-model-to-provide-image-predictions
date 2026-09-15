import keras
from keras.preprocessing import image
from keras.applications.inception_v3 import (
    preprocess_input,
    decode_predictions,
    InceptionV3,
)
import numpy as np
import tensorflow as tf


model = InceptionV3(
    include_top=True, weights="imagenet", input_tensor=None, input_shape=None
)


def predict(image_file):
    img = image.load_img(image_file, target_size=(299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    decoded_preds = decode_predictions(preds, top=3)[0]
    return decoded_preds
