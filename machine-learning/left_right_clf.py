import pandas as pd
import numpy as np
import os 
import sys
import pprint as pprint
import itertools 

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import classification_report

import seaborn as sns
from sklearn import metrics

from tools.config import config
from patient.exercises import Exercises
from patient.patientfolder import Patient
from patient.patientgroup import PatientGroup

#created an empty list of patient_groups 
patient_groups = list()

#looping through path of category and prints the groupid 
for groupid in range(1, 4):
    #creating path to patientgroup
    grouppath = config.basepath.format(groupid=groupid)
    patient_groups.append(PatientGroup(grouppath))


#generating data for model
exercisetype = ['AF', 'EL', 'AB', 'RF', 'EH']
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


print('Shape of the X', soorted_data.shape)
print('Shape of the y', indicator.shape)

#splitting data into train/test 
X_train, X_test, y_train, y_test = train_test_split(soorted_data, indicator, test_size=0.20, random_state=420, shuffle=True)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# Logistic LogisticRegression model
logisticReg = LogisticRegression()

#fitting the data into the model
logisticReg.fit(X_train, y_train)

#predicting the on the test data
y_pred = logisticReg.predict(X_test)

# get the accuracy using .score and report using classification_report from sklearn
score = logisticReg.score(X_test, y_test)
report = classification_report(y_test, y_pred, labels=[0, 1])

print(score, report)

confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
print(confusion_matrix)

plt.figure(figsize=(2,2))
sns.heatmap(confusion_matrix, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
title = 'Accuracy Score: {0}'.format(score)
plt.title(title, size = 10)

plt.show()