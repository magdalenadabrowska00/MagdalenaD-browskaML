import tensorflow as tf
from tensorflow.keras.layers import RandomWidth, RandomHeight, RandomZoom, RandomFlip, RandomRotation, RandomBrightness
from tensorflow.keras.utils import image_dataset_from_directory
import os; os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
import os
os.system("python C:\\Users\\Magda\\Desktop\\MagdalenaD-browskaML\\model.py")
import pathlib
import matplotlib.pyplot as plt
import seaborn as sns
import glob
from sklearn.metrics import classification_report, confusion_matrix
import cv2
import numpy as np
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Conv2D, MaxPooling2D, Flatten, Dropout, Rescaling
import math
from tensorflow import keras


width, height = 128,128
learning_rate=0.00001
batch_size= 32
epochs = 10

local_folder = 'C:\\Users\\Magda\\Desktop\\Magda nauka\\Informatyka\\Semestr 5\\Uczenie maszynowe\\Datasety'
local_folder = pathlib.Path(local_folder)
train_dir = os.path.join(local_folder, 'train')
test_dir = os.path.join(local_folder, 'test')
print(train_dir)

train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    train_dir,
    seed=123,
    image_size=(width, height),
    batch_size=batch_size)
print(type(train_dataset))

valid_dataset = image_dataset_from_directory(
    test_dir,
    seed=123,
    image_size=(width, height),
    batch_size=batch_size)

classes = train_dataset.class_names

def get_number_of_files_in_dataset(directory):
    if not os.path.exists(directory):
        print("No such directory. Sorry")
        return 0

    count = 0
    for r, dirs, files in os.walk(directory):
        for dr in dirs:
            count += len(glob.glob(os.path.join(r, dr +"/*")))
    return count

# wyświetlenie z nazwami klas
def show_examples():
    plt.figure(figsize=(10, 10))
    for images, labels in train_dataset.take(1):
      for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(classes[labels[i]])
        plt.axis("off")



print("Kategorie w zbiorach:",classes)
print("Ilość plików w zbiorze treningowym:", get_number_of_files_in_dataset(train_dir))
print("Ilość plików w zbiorze testowym:", get_number_of_files_in_dataset(test_dir))

examples=show_examples()

model = Model()
model.model_definition().fit(train_dataset, validation_data=valid_dataset, epochs=epochs)




#shift tab - cofnięcie tabulatora
# shift alt e - run one line
# ctrl / - komentarz