import tensorflow as tf
from keras.utils import to_categorical
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Conv2D, MaxPooling2D, Flatten, Dropout, BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Nadam
import os; os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

class Model():
    def model_definition(learning_rate):
        data_augmentation = tf.keras.Sequential(
            [
                RandomFlip("horizontal_and_vertical",
                           input_shape=(128,
                                        128,
                                        3)),
                RandomBrightness(factor=0.2),
            ]
        )

        model = tf.keras.Sequential([
            data_augmentation,

            Conv2D(filters=32, kernel_size=(3,3), padding='valid', activation='relu'),
            BatchNormalization(),
            MaxPooling2D(),
            Dropout(0.25),

            Conv2D(filters=64, kernel_size=(3,3), padding='valid', activation='relu'),
            BatchNormalization(),
            MaxPooling2D(),
            Dropout(0.25),

            Conv2D(filters=128, kernel_size=(3,3), padding='valid', activation='relu'),
            BatchNormalization(),
            MaxPooling2D(),
            Dropout(0.25),

            Flatten(),

            Dense(512, activation='relu', bias_regularizer=tf.keras.regularizers.l2(0.2)),
            BatchNormalization(),
            Dropout(0.5),

            Dense(len(classes), activation='softmax')
        ])

        model.compile(optimizer=tf.keras.optimizers.RMSprop(learning_rate=0.00001),
                      loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                      metrics=['accuracy'])

        model.summary()
        return model