import tensorflow as tf
from keras.utils import to_categorical
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Nadam

class Model():
    def model_definition(self):

        model = tf.keras.Sequential()

        model.add(Conv2D(filters=32, kernel_size=(3,3), padding='same', input_shape=(299, 299, 3), activation='relu')) #Xception default
        model.add(Conv2D(filters=32, kernel_size=(3,3), padding='same', activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
        model.add(Dropout(0.2))

        model.add(Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation='relu'))
        model.add(Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation='relu'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Dropout(0.2))

        model.add(Conv2D(filters=128, kernel_size=(3, 3), padding='same', activation='relu'))
        model.add(Conv2D(filters=128, kernel_size=(3, 3), padding='same', activation='relu'))
        model.add(MaxPooling2D((2, 2)))
        model.add(Dropout(0.2))

        model.add(Flatten())

        model.add(Dense(128, activation='relu'))
        model.add(Dropout(0.2))

        model.add(Dense(5, activation='softmax'))

        model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(), metrics=['accuracy'])

        return model