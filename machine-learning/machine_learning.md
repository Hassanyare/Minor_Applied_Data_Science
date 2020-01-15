
# Machine Learning

For practice i did a classification on the left and right movements part of an exercises (limb). I used sklearn logistic regression as a model. For the complete code I wrote on this classification see this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/src_machine-learning/left_right_clf.py)


## Data prepration

To generate the data consisting of left and right limb, I first filter the left and right limb movements using regex. see the code below. 
``` Python
def df_regex(self, pattern):
    # Left          r"._l_."
    # Right         r"._r_."
    return self.df.filter(regex=(pattern))
```

With the code above i filtered the columns as shown below:

``` Python
#right limb
"thorax_r_x_ext", "thorax_r_y_ax", "thorax_r_z_lat",
"clavicula_r_y_pro", "clavicula_r_z_ele", "clavicula_r_x_ax",
"scapula_r_y_pro", "scapula_r_z_lat", "scapula_r_x_tilt",
"humerus_r_y_plane", "humerus_r_z_ele", "humerus_r_y_ax",

#Left limb
"thorax_l_x_ext", "thorax_l_y_ax", "thorax_l_z_lat",
"clavicula_l_y_pro", "clavicula_l_z_ele", "clavicula_l_x_ax",
"scapula_l_y_pro", "scapula_l_z_lat", "scapula_l_x_tilt",
"humerus_l_y_plane", "humerus_l_z_ele", "humerus_l_y_ax",
"ellebooghoek_l"

```

To generate the data I loped through each patient_group, and patient data to creat a filtered data. I then convert the data to numpy array. After this, I saved all the patient data, both the left and right limb to one numpy array. I then genarate the indicator array(the y values). see the code below: 

```python

soorted_data = None
indicator = None

for patientgroup in patient_groups:
    print('patientgroup')
    for patient in patientgroup.patients:
        patient_data = {}
        for exercisetype in exercisetype:
            patient_data[exercisetype] = []

            for exercise in patient.exercises:
                if exercise.execerisegroup == exercisetype:
                    patient_data[exercisetype].append(exercise)
                    # print(patient_data)

                exercise_right = exercise.soorted_exercise_right
                exercise_left = exercise.soorted_exercise_left

                if soorted_data is None:
                    soorted_data = np.concatenate((exercise_right.to_numpy(), exercise_left.to_numpy()))
                else:
                    soorted_data = np.concatenate((soorted_data, exercise_right.to_numpy()))
                    soorted_data = np.concatenate((soorted_data, exercise_left.to_numpy()))
                
                #creating indicators for the left(0) and right(1)
                indices_left  = np.zeros(len(exercise_left), dtype=int)
                indices_right = np.ones(len(exercise_right), dtype=int)
               
                
                if indicator is None:
                    indicator = np.concatenate((indices_left, indices_right))
                else: 
                    indicator = np.concatenate((indicator, indices_left))
                    indicator = np.concatenate((indicator, indices_right))
```
## The model

I used sklearn logistic regression to categorize the left and right limb movements. First we split the data using sklearn train_test_split function into 80/20. The use the default logistic regression model from sklearn and fit the train data into the model. Then use the test data to validate the model. 

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

These is how I get the results of the model. 

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

I was also able to prepare the motion data as the last project group did, namely a data set of all exercises per patient in one raw. This created datashape of (x, 650), x is the rows/ patient data and the 650 columns. For more about how i prepared this dataset, see the personal [powerpoint](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/presentation/internal-presentation-30-oct.pdf) I made. This way of preparing the data helped me understand the analysis the previous groups did and validating their results. 
