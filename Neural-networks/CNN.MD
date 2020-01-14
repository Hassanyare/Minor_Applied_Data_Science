
# Convolutional neural networks



## Data prepration

After trying many other options, i found that classifying the patient groups on exercise level to work best without any biases. 

For preparing image data these are the steps I took.

-	Generate image data for each exercises.
-   Use the resampled exercise data since these ones have fixed rows(frames)
-	Reshape the features that belong together into an RGB format
    -   Reshape the x,y,z coordinates of one body part into an RGB format
-	Place a decoder [colour bar] between the bones for the model to better differentiate between them 
-   Normalize the data to be values between 0 and 1: this is good for the model

This is how the genarated image data then looks like. 
![image](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/data-resampled-color.png)

I also prepared the motion dataset into other shapes, for ininstance a dataset with velocity with Arjun. However i was not able to build a model for each an every data representation. 

```python


```
## The model

The figure below is a representation of the model i configured to read the image data. 

![CNN-model](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/model.png)



```python


```

## Results
### Augmented dataset vs reguler dataset (not augmented) vs

These are the results: 

|Type of data used  |Accuracy |precision| recal |F1-score|
|-------------------|---------|---------|-------|--------|
|Augmented dataset  |0.5066   |0.582    |0.545  |0.563   |
|Reguler dataset    | 0.726   |0.657    |0.605  |0.630   |

The graphs below, shows when regular dataset is used.

![loss](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/training-val-loss.png)

![acc](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/training-val-accuracy.png)

confusion matrix on the test dataset, when regurlar dataset is used. 

![matrix](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/cm-normal-data.png)

The graphs below, shows when augmentend dataset is used.

![loss](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/validation-NN/training-val-loss-aug.png)

![acc](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/validation-NN/training-val-accuracy-aug.png)


confusion matrix on the test dataset when the :

![matrix](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/validation-NN/cm-aug.png)


From the results in the in the graphs above, I found that when using the augmented dataset, the model overfits on the training dataset since the validation loss increases while the train loss decreases. This is why i used the regular dataset to validated and evaluate the model. 
## Validation 

The performance as measured in the validation data shows that the model performed as expected. The validation loss decreased while the accuracy increased. This means that the model is not overfitting. The overal performanced of the model is measured by the test data. The performance of the model as measured by the test data is represented in the table below.

These are the predictions per class when regular dataset is used. I used excel to calculate these predictions.

![predictions-per-class](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/predictions.PNG)


## Evaluation 

According to one of the Physitians, 70% accuracy of predicting the right patient group is regarded enough. The way the data is prepared was and very useful in get beter predictions. 

## Conclusion 

Convolutional neural networks are able to classify(cluster) patients in groups with simialar complaints and or similar diagnosis based on the FoB flock of birds data. For further research I recommend transfer learning with pretrained convolutional neural networks.    

