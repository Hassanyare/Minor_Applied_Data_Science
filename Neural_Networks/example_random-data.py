import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Just disables the warning, doesn't enable AVX/FMA
# import osc 
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

observations = 100000

xs = np.random.uniform(low=-10, high=10, size=(observations,1))
zs = np.random.uniform(-10, 10, (observations,1))

generated_inputs = np.column_stack((xs,zs))

noise = np.random.uniform(-1, 1, (observations,1))
generated_targets = 2*xs - 3*zs + 5 + noise

np.savez('TF_intro', inputs=generated_inputs, targets=generated_targets)

training_data = np.load('TF_intro.npz')

input_size = 2 #The model needs to know what the input shape of the (dimension) it should except
output_size = 1

model = tf.keras.Sequential([
                            tf.keras.layers.Dense(output_size, 
                            kernel_initializer = tf.random_uniform_initializer(minval=0.1, maxval=0.1),
                            bias_initializer = tf.random_uniform_initializer(minval=0.1, maxval=0.1)
                            )

                            ]) 

custom_optimizer_sgd = tf.keras.optimizers.SGD(learning_rate=0.02)
custom_optimizer_adam = tf.keras.optimizers.Adam()

loss_BCEL = tf.keras.losses.BinaryCrossentropy()
loss_huber = tf.keras.losses.Huber()
loss_MSE = tf.keras.losses.MeanSquaredError()
SCEL = tf.keras.losses.SparseCategoricalCrossentropy()


model.compile(optimizer= custom_optimizer_adam , loss=loss_BCEL)


model.fit(training_data['inputs'], training_data['targets'],batch_size=64, epochs=50, verbose=2)

weights = model.layers[0].get_weights()

# print(weights)
# print(weights[0])
# bias = model.layers[0].get_weights()[1]

prediction = model.predict_on_batch(training_data['inputs'])

plt.plot(np.squeeze(model.predict_on_batch(training_data['inputs'])), np.squeeze(training_data['targets']))
plt.xlabel('inputs')
plt.ylabel('targets')

plt.show()
# print(prediction)