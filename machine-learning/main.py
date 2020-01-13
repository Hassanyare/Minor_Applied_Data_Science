import pandas as pd
import os 
import sys
import pprint
import itertools 
import numpy as np
from time import time


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
from sklearn.metrics import classification_report, accuracy_score
from sklearn import tree


from ml.LogReg import LogisticRegressionModel 
from ml.DecisionTree import DecisionTreeClassifier 
from tools.config import config
from patient.exercises import Exercises
from patient.patientfolder import Patient
from patient.patientgroup import PatientGroup


#created an empty list of patient_group 
patient_group = list()

#looping through path of category and prints the groupid 

for groupid in range(1, 5):
    #creating path to patientgroup
    grouppath = config.basepath.format(groupid=groupid)
    patient_group.append(PatientGroup(grouppath))

# crossjoin the exercises 

train_combinations = list()
test_combinations = list() 

exercisetypes = ['AF', 'EL', 'AB', 'RF', 'EH']


for patientgroup in patient_group:
    print('patientgroup')
    for patient in patientgroup.patients:

        patient_data = {}
        for exercisetype in exercisetypes:

            # going through exercise types AF, AB, EL etc

            patient_data[exercisetype] = []
            
            #here an empty list is created in which each type of exercises gets it's own list
             
            for exercise in patient.exercises:
                #going through all the exercises of a patient
                if exercise.execerisegroup == exercisetype:
                    #each exercises is added to it's respective group.

                    patient_data[exercisetype].append(exercise)
                    
        resultaten = list(itertools.product(patient_data['AF'],
                                            patient_data['EL'],
                                            patient_data['AB'],
                                            patient_data['RF'],
                                            patient_data['EH']))
        
        if len(patient.exercises) > 0:
            if int(patient.exercises[0].patientid) in config.test_selections[patient.exercises[0].patiengroup]:
                test_combinations.extend(resultaten)
            else: 
                train_combinations.extend(resultaten)
         
           

print('Found_Possible_Combinations', len(train_combinations))

def generate_data(combinations):
    np_combination_array = np.empty((0,len(config.columns)*config.frames_counts * 5))
    np_indicator_array = np.array([])

    for exercise_combination in combinations:
        # for every exercise in the combination (['AF', 'EL', 'AB', 'RF', 'EH'])
        data = np.array([])
    
        for exercise in exercise_combination:
            # Getting 5 frames from exercise
            # print(len(exercise_combination))

            np_exercise = exercise.np_data.reshape(1,len(config.columns)*config.frames_counts)
            data = np.append(data, np_exercise[0])

        np_combination_array = np.vstack ([np_combination_array, data])
        np_indicator_array = np.append(np_indicator_array, exercise_combination[0].patiengroup)

    return np_combination_array, np_indicator_array

np_combination_test, np_indicator_test = generate_data(test_combinations)
np_combination_train, np_indicator_train = generate_data(train_combinations)


print('Shape Training data', np_combination_train.shape, np_indicator_train.shape) 
print('Shape Testing data', np_combination_test.shape, np_indicator_test.shape)


logisticregression = LogisticRegressionModel()
print("Training started")
logisticregression.train(np_combination_train, np_indicator_train)
# logisticregression.test(X_test, y_test)
print("Training done! ")

y_pred = logisticregression.predict(np_combination_test)
print(classification_report(np_indicator_test, y_pred, digits=3))
print('accuracy_score', accuracy_score(np_indicator_test, y_pred, normalize=True, sample_weight=None))