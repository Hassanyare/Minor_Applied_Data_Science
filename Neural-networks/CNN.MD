
# Convolutional neural networks



## Data prepration


```python


```
## The model



```python


```

## Results

These is how we get the results of the model. 

```python

````
```

```


``` Python
confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
```

Not augmented dataset:

|Accuracy |precision| recal |F1-score|
|---------|---------|-------|--------|
| 0.736   |0.657    |0.598  |0.626   |


![loss](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/validation-NN/training-val-loss.png)

![acc](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/validation-NN/training-val-accuracy.png)

confusion matrix on the test dataset
![matrix](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/validation-NN/cm-normal-data.png)



Augmentd dataset:

|Accuracy |precision| recal |F1-score|
|---------|---------|-------|--------|
|0.5066   |0.582    |0.545  |0.563   |



![loss](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/validation-NN/training-val-loss-aug.png)

![acc](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/validation-NN/training-val-accuracy-aug.png)

confusion matrix on the test dataset:

![matrix](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/validation-NN/cm-aug.png)

## Evaluation of the models


## Conclusion 


