import os.path
from config import hyper_cnn
from config import Optimize_cnn
from cnn_conf import cnnConfiguration
from dataCNN2 import *
from dataAug import *

import tensorflow as tf

import numpy as np
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from matplotlib.pyplot import imread, imshow, subplots, show

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing

import matplotlib.pyplot as plt
import seaborn as sns

import json


patient_groups = [
    PatientGroup(config.basepath.format(groupid=1)),
    # PatientGroup(config.basepath.format(groupid=4)),
    PatientGroup(config.basepath.format(groupid=2)),
    PatientGroup(config.basepath.format(groupid=3)),
]


def CNN_new(train_x, train_y, valid_x, valid_y, test_x, test_y):

    #preview:
    plt.figure(figsize=(3,3))
    for i in range(3):
        # plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_x[i], cmap=plt.cm.binary)
        plt.xlabel(train_y[[i][0]])
    plt.show()


    output_size = 3
    img_input= 100, 16, 3
    kernal_size= 5,3
    strides = 1,1

    model = models.Sequential()

    # Block 1
    # Conv2D( number_of_filters , kernal_size , input_shape(add this parameter just for the input conv layer))
    model.add(layers.Conv2D(64, kernal_size,
                      strides= strides,
                      padding = 'same', 
                      activation='relu',
                      input_shape=(img_input),
                      name='block1_conv1'))

    model.add(layers.MaxPooling2D((2, 2), 
                    strides=(2, 2),
                    name='block1_pool'))
    
    model.add(layers.Dropout(0.4))


    # Block 2
    # Conv2D( number_of_filters , kernal_size , input_shape(add this parameter just for the input conv layer))
    model.add(layers.Conv2D(64, kernal_size,
                      strides= strides,
                      padding = 'same', 
                      activation='relu',
                      name='block2_conv1'))


    model.add(layers.MaxPooling2D((2, 2), 
                    strides=(2, 2),
                    name='block2_pool'))

    model.add(layers.Dropout(0.4))

    #flatten layer
    model.add(layers.Flatten())

    #fully connected layer
    model.add(layers.Dense(256, activation='relu'))

    model.add(layers.Dropout(0.4))

    #output layer with the size as the number of categories 
    model.add(layers.Dense(output_size, activation='softmax'))
    model.summary()

    #Computes the crossentropy loss between the labels and predictions.
    cce = tf.keras.losses.SparseCategoricalCrossentropy()


    model.compile(optimizer= 'adam',
                  loss=cce,
                  metrics=['accuracy'])

    history = model.fit(train_x, train_y,
                        epochs=20,
                        validation_data=(valid_x, valid_y),
                        batch_size=32,
                        callbacks=[Optimize_cnn.earlystopping]).history

    #plotting the loss and the accuracy of the model
    plt.plot(history['loss'], label='loss')
    plt.plot(history['val_loss'], label='val_loss')
   
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training/validation loss', loc='center')
    plt.legend(loc='upper right')
    plt.show()


    plt.plot(history['accuracy'], label='accuracy')
    plt.plot(history['val_accuracy'], label='val_accuracy')

    plt.xlabel('Epoch')
    plt.ylabel('accuracy')
    plt.title('Training/validation accuracy', loc='center')
    plt.legend(loc='upper right')
    
    plt.show()

    val_loss, val_accuracy = model.evaluate(valid_x, valid_y, verbose=2)

    print(val_loss, val_accuracy)

    # Evaluate the model on the test data 
    print('\n# Evaluate on test data')
    results = model.evaluate(test_x, test_y, batch_size=32)
    print('test loss, test acc:', results)

    # Generate predictions (probabilities -- the output of the last layer)

    # on new data using `predict`
    print('\n# Generate predictions for test samples')
    predictions = model.predict(test_x)
    print('predictions shape:', predictions.shape)

    #convert the one-hot-encoded predictions to normal label, I use the argmax function:
    predictions = tf.argmax(predictions, axis = 1)

    #To compute the confusion matrix i use the tf.math.confusion_matrix
    matrix = tf.math.confusion_matrix(labels=test_y, predictions=predictions, num_classes=output_size)
    tf.print(matrix)
    #Plotting the confusion_matrix
    plt.figure(figsize=(3,3))
    sns.heatmap(matrix, annot=True, fmt=".3f", linewidths=.2, square = True, cmap = 'Blues_r')
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')
    title = 'CNN of two convolutional_layers'
    plt.title(title, size = 20)

    plt.show()

    #Caluculating precision, recall and the F1-score:

    TP = tf.math.count_nonzero(predictions * test_y)
    TN = tf.math.count_nonzero((predictions - 1) * (test_y - 1))
    FP = tf.math.count_nonzero(predictions * (test_y - 1))
    FN = tf.math.count_nonzero((predictions - 1) * test_y)

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = 2 * precision * recall / (precision + recall)

    tf.print("precision:", precision, "recall:", recall, "f1:", f1)

#generating dataset: generate_data_resampled_colour
X, y = generate_data_resampled_colour(patient_groups)

#image augmentations of tensorflow.keras
data_generator = ImageDataGenerator(rotation_range=90,
                                    zoom_range=0.15,
                                    width_shift_range=0.2,
                                    height_shift_range=0.2,
                                    shear_range=0.15,
                                    horizontal_flip=True,
                                    fill_mode="nearest")

# # applying data augmentation
# dataset_x = np.zeros([0, 100, 16, 3])
# for image in X:
    
#     image = image.reshape((1, 100,16,3))
#     augmented_image = data_Augment(data_generator, image, limit=10)
    
#     dataset_x = np.concatenate((dataset_x, augmented_image), axis=0)

# #generating as much labels as extra image created
# dataset_y = np.array([])
# for label in y: 
#     dataset_y = np.append(dataset_y,[label]*10, axis=0)



#splitting the into train and test dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=420)


#splitting the train verder dataset into validation and train dataset
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.20, random_state=420)

print(X_train.shape, X_test.shape, X_val.shape)

CNN_new(X_train, y_train, X_val, y_val, X_test, y_test)
