from tensorflow.keras.preprocessing.image import ImageDataGenerator
from matplotlib.pyplot import imread, imshow, subplots, show
import numpy as np


def data_Augment(data_generator,images, limit=10):

""""
 Input data: 
 - generator function of tensorflow ImageDataGenerator, image like data 
 - and set the limit for the total augmentation allowed per image
 
 Returns Augmented image
""""
    data_generator.fit(images)
    image_iterator = data_generator.flow(images)
    genarated_data = np.array([image_iterator.next()[0]])
    limit -= 1
    for image in image_iterator:
        genarated_data = np.append(genarated_data, [image[0]], axis=0)
        limit -= 1
        if limit <= 0:
            break
    

    return genarated_data