import tensorflow as tf
from keras.utils import to_categorical
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Nadam
import os; os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

class Model():
    def model_definition(learning_rate):
        data_augmentation = tf.keras.Sequential(
            [
                RandomFlip("horizontal_and_vertical",
                           input_shape=(299,
                                        299,
                                        3)),
                RandomRotation(0.1),
                RandomZoom(0.1),
                RandomBrightness(factor=0.2),
            ]
        )

        model = tf.keras.Sequential([
            data_augmentation,
            Rescaling(1. / 255),

            Conv2D(filters=16, kernel_size=(3, 3), padding='same', activation='relu'),
            MaxPooling2D(),
            Dropout(0.2),

            Conv2D(filters=32, kernel_size=(3, 3), padding='same', activation='relu'),
            MaxPooling2D(),
            Dropout(0.2),

            Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation='relu'),
            MaxPooling2D(),
            Dropout(0.2),

            Flatten(),

            Dense(128, activation='relu'),
            Dropout(0.2),

            Dense(len(classes), activation='softmax')
        ])

        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                      # SparseCategoricalCrossentropy(from_logits=True)
                      metrics=['accuracy'])

        model.summary()
        return model