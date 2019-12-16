import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt
import keras as keras

import datetime as datetime
import os

# Just disables the warning, doesn't enable AVX/FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


#importing the dataset

mnist_data = tfds.load(name='mnist')

mnist_data, mnist_info = tfds.load(name='mnist', with_info=True, as_supervised=True)

mnist_train, mnist_test = mnist_data['train'], mnist_data['test']

num_validation_samples = 0.1 * mnist_info.splits['train'].num_examples
num_validation_samples = tf.cast(num_validation_samples, tf.int64)

num_test_samples = mnist_info.splits['test'].num_examples
num_test_samples = tf.cast(num_test_samples, tf.int64)


#scaling the dataset

def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255.
    return image, label

scaled_train_and_validation_data = mnist_train.map(scale)
test_data = mnist_test.map(scale)

#shuffle data set and getting the train and validation data
buffer_size = 10000

Shuffled_train_validation_data = scaled_train_and_validation_data.shuffle(buffer_size)

validation_data = Shuffled_train_validation_data.take(num_validation_samples)
train_data = Shuffled_train_validation_data.skip(num_validation_samples)

# determine the batch size
BATCH_SIZE = 200

# we can also take advantage of the occasion to batch the train data
# this would be very helpful when we train, as we would be able to iterate over the different batches
train_data = train_data.batch(BATCH_SIZE)

validation_data = validation_data.batch(num_validation_samples)

# batch the test data
test_data = test_data.batch(num_test_samples)


validation_inputs, validation_targets = next(iter(validation_data))

#outline the model
input_size = 784
output_size = 10
hidden_layers_size = 150

model = tf.keras.Sequential([
                            tf.keras.layers.Flatten(input_shape=(28,28,1)),
                            tf.keras.layers.Dense(hidden_layers_size, activation='relu'),
                            tf.keras.layers.Dense(hidden_layers_size, activation='relu'),
                            tf.keras.layers.Dense(output_size, activation='softmax')
                            ])



# customizing model
custom_optimizer_adam = tf.keras.optimizers.Adam()
SCEL = tf.keras.losses.SparseCategoricalCrossentropy()

model.compile(optimizer= custom_optimizer_adam , loss=SCEL, metrics= ['accuracy'])

# Define the Keras TensorBoard callback.

log_dir="graph\\fit\\" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = keras.callbacks.TensorBoard(log_dir =log_dir, histogram_freq=0,  
                        write_graph=True, write_images=True)


#training the data

num_epochs = 5

history = model.fit(train_data,
            epochs=num_epochs,
            validation_data=(validation_inputs, validation_targets),
            validation_steps=10,
            callbacks=[tensorboard_callback]).history

print(history)