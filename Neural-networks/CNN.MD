
# Convolutional neural networks (CNN)

Since CNN works well with image data, I created an Image data from the resampled exercises. For more on this see data preparation. I used [Tensorflow](https://www.tensorflow.org/) to build the model, because i had a course on these library and there are a lot of information about it online. 

## Data prepration

After trying other options, i found that classifying the patient groups on exercise level works best for CNN without any biases. 

For preparing image data these are the steps I took.

- Use the resampled exercise data since these ones have fixed rows(frames)	
- Generate image data for each exercises.
- Reshape the features that belong together into an RGB format
    - Reshape the x,y,z coordinates of one body part into an RGB format

[RGB-Image](C:\Users\hassa\OneDrive\Desktop\Minor_Applied_Data_Science\Neural-networks\foto's\RGB.png)

-	Place a decoder [colour bar] between the bones for the model to better differentiate between them 
-   Normalize the data to be values between 0 and 1: this is good for the model

This is how the genarated image data then looks like. 
![image](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/data-resampled-color.png)

I also prepared the motion dataset into other shapes, for ininstance a dataset with velocity. However i was not able to build a model for each an every data representation. Arjun worked with me on this part, he helped me on preparing the different data representations. See this [code](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/dataCNN2.py) for the data preparation. 

## The model

The figure below is a representation of the model i configured to read the image data. The model consists of two main parts. The feature learning part and the classification part.  

![CNN-model](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/model.png)

These are the different layers of the model and what they do:



| Layer                 | Describtion                                               | 
|-----------------------|-----------------------------------------------------------|
| [Conv2D](https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148)                | The convolutional leyer filters(convolves) the input data to get usefull information (feuture maps).
| [Maxpooling](https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148)            | Maxpool layer reduces the dimensionality of the convolved data by selecting maximum values only.                                                      |
| [Dropout](https://leonardoaraujosantos.gitbooks.io/artificial-inteligence/dropout_layer.html)| During trainging percentage (40%) of the neurons will be deactivated to overcome overifitting and force the model to generalize.                                                                            |
| [Flatten](https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148)          | Flatten the output of the last layer into a vector so that we can feed it into a dense layer.                                                           |
| [Fully connected layer (FC layer)](https://medium.com/@RaghavPrabhu/understanding-of-convolutional-neural-network-cnn-deep-learning-99760835f148)         |  With fully connceted layer all the features are combined in order to predict the right patient group.                                                         |   
| Output                |  After the fully connceted layer, i used softmax function as activation function for the output layer. The softmax function interprets the final activation produced by the FC-layer as probabilities                                    |

### Hyper-parameters tuning

**Kernal_size** - Since the data does not have the same width and hight, i choose a regtangular kernal instead of the ussual square kernal size. Also an even kernal size was adviced by most documents i read.

**Dropout Percentage** - After trial and error i found that 40% to be good Percentage for the dropout layer.

**Adam vs SGD** - After trial and error I found [adam](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/Adam?version=stable) to be a better optimization since it converges much faster to a global minimum.

**Loss function** - as adivised by [Tesnorflow](https://www.tensorflow.org/api_docs/python/tf/keras/losses/SparseCategoricalCrossentropy?version=stable) used the Sparse Categorical Crossentropy to compute the crossentropy loss between the labels and predictions.


## Results
### Augmented dataset vs reguler dataset (not augmented) vs

These are the results: 

|Accuracy |precision| recal |F1-score|
|---------|---------|---------|------|
| 0.726   |0.657    |0.605    |0.630 |


<details>
  <summary>The graphs below, show when loss and accuracy of the model on the train and validation dataset.
</summary>
![loss](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/training-val-loss.png)

![acc](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/training-val-accuracy.png)

</details>

<details>
  <summary>confusion matrix on the test dataset
</summary>
    
![matrix](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/cm-normal-data.png)

</details>

## Validation 

The performance as measured in the validation data shows that the model performed as expected. The validation loss decreased while the accuracy increased. This means that the model is not overfitting. The overal performanced of the model is measured by the test data. The performance of the model as measured by the test data is represented in the table below.

These are the predictions per class when regular dataset is used. I used excel to calculate these predictions.

![predictions-per-class](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/predictions.PNG)


## Evaluation 

According to one of the Physitians, 70% accuracy of predicting the right patient group is regarded enough. The way the data is prepared was and very useful in get beter predictions. 

## Conclusion 

Convolutional neural networks are able to classify(cluster) patients in groups with simialar complaints and or similar diagnosis based on the FoB flock of birds data. For further research I recommend transfer learning with pretrained convolutional neural networks.    

