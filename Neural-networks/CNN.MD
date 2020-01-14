
# Convolutional neural networks



## Data prepration


```python


```
## The model



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


From the results in the table below, I conclude that using the augmenting dataset, the model overfits on the training dataset since the validation loss increases while the train loss decreases. This is why is used the regular dataset 
## Validation 

The performance as measured in the validation data shows that the model performed as expected. The validation loss decreased while the accuracy increased. This means that the model is not overfitting. The overal performanced of the model is measured by the test data. The performance of the model as measured by the test data is represented in the table below.

These are the predictions per class when regular dataset is used. I used excel to calculate these predictions.

![predictions-per-class](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/predictions.PNG)


## Evaluation 
An accuracy of 

## Conclusion 

Convolutional neural networks are able to classify(cluster) patients in groups with simialar complaints and or similar diagnosis based on the FoB flock of birds data. For further research I recommend transfer learning with pretrained convolutional neural networks.    

