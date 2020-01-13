
# Machnine Learning

For practice i did a classification on the left and right movements part of the exercises (arm). I used sklearn logistic regression as a model. For the complete code I wrote on this classification see this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/src_machine-learning/left_right_clf.py)


## Data prepration

To generate the data consisting of left and right arm data, we first filter the left and right arm movements using regex. see the code below. 
``` Python
def df_regex(self, pattern):
    # Left          r"._l_."
    # Right         r"._r_."
    return self.df.filter(regex=(pattern))
```

To generate the data we loop through each patient_group, and patient data to creat a filtered data. We then convert the data to numpy array. After this, we save all the patient data, both the left and right arm to one numpy array. We then genarate the indicator(our y values). 

```python
Soorted_data = None
Indicator = None

if soorted_data is None:
    soorted_data = np.concatenate((exercise_right.to_numpy(), exercise_left.to_numpy()))
else:
    soorted_data = np.concatenate((soorted_data, exercise_right.to_numpy()))
    soorted_data = np.concatenate((soorted_data, exercise_left.to_numpy()))

#genarating the true values (y values)
if indicator is None:
    indicator = np.concatenate((indices_left, indices_right))
else: 
    indicator = np.concatenate((indicator, indices_left))
    indicator = np.concatenate((indicator, indices_right))


```
## The model

I used sklearn logistic regression to categorize the left and right arm movements. First we split the data using sklearn train_test_split function into 80/20. The use the default logistic regression model from sklearn and fit the train data into the model. Then use the test data to validate the model. 

```python

#splitting data into train/test 
X_train, X_test, y_train, y_test = train_test_split(soorted_data, indicator, test_size=0.20, random_state=420, shuffle=True)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# Logistic LogisticRegression model
logisticReg = LogisticRegression()

#fitting the data into the model
logisticReg.fit(X_train, y_train)

#predicting the on the test data
y_pred = logisticReg.predict(X_test)

```

## Results

These is how we get the results of the model. 

```python
# get the accuracy using score and model report using classification_report from sklearn
score = logisticReg.score(X_test, y_test)
report = classification_report(y_test, y_pred, labels=[0, 1])

````
```

           0       0.74      0.73      0.74     30755
           1       0.74      0.74      0.74     30770

    accuracy                           0.74     61525
   macro avg       0.74      0.74      0.74     61525
weighted avg       0.74      0.74      0.74     61525

```

The accuracy is 73.83%. I also computed the confusion matrix of the model using sklearn matrics. 

``` Python
confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
```
![matrix](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/matrix-leftvsright.png)

## Evaluation of the models

The model did well, the precision and recall are both as high as the accuracy. 

## Conclusion 

This was a good practice for my python/machine learning skills and to understand the data better. 

## Furthermore

I was also able to prepare the motion data as the last project group did, namely a data set of all exercises per patient in one raw. This created datashape of (x, 650), x is the rows/ patient data and the 650 columns. For more about how i prepared this dataset, see the personal [powerpoint](C:\Users\hassa\OneDrive\Desktop\Project_py\Minor_Applied_Data_Science\presentation\personal-presentation-30-oct.pptx) I made. This way of preparing the data helped me understand the analysis the previous groups did and validating their results. 
