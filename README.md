# Minor_Applied_Data_Science
Welcome to my portfolio on the tasks I have done and been part of during my minor Applied data science at the Hague University of Applied Sciences. 


# Table of Contents

- [1. Jargon](#1-Jargon)

- [2. Personal development](#2-Personal-development)
  - [2.1 DataCamp courses](##21-DataCamp-courses)
  - [2.2 Machine-learning](##22-Machine-learning)
  - [2.3 Online course](##23-Online-course)

- [3. Project Ortho Eyes](#3-Project-Ortho-Eyes)
  - [3.1 Project's scope and relevance](##31-Project's-scope-and-relevance)
  - [3.2 Strategy](##32-Research-proposal)
     - [3.2.1 Research proposal](###321-Research-proposal)
     
- [4. The dataset](#4-The-dataset)
  - [4.1 Flock of birds system](##41-Flock-of-birds-system)
  - [4.1 Raw visualization](##41-Raw-visualization)
  - [4.1 Visualizations converted data](##41-Visualizations-converted-data)

- [5. Data Cleaning and Enrichment](#5-Data-cleaning-and-Enrichment)
  - [5.1  Data Cleaning](##51-Data-Cleaning)
     - [5.1.1 Removing the idle](###511-Removing-the-idle)
  - [5.2 Data enrichment](##52-Data-enrichment)

 - [6. Neural Networks](#6-Neural-Networks)
     - [6.1 Convolutional neural network](#61-convolutional-neural-network)

- [7. Research ](#7-Research)
  - [7.1 Evaluation](#7-Evaluation)
  - [7.2 Conclusion ](#7-Conclusion)
- [8. Presentaties](#8-Presentaties)
- [9. Reference to Git commits](#9-Reference-to-Git-commits)
- [10. Self reflection](#9-Self-reflection)

# 1. Jargons

| Jargon:         | Describtion:                                                                 |     
|----------------:|---------------------------------------------------------------------------:|
| Raw data        | Data from the Flock of birds system(FoB) X,Y,Z coordinates of each sensor  |
| Converted Data  | Transformed data from sensor data to rotation angle between bones          |     

# 2. Personal development
## 2.1 DataCamp courses
During the first few weeks of the minor i mostly worked on my python skills. I was able to finish the data camp courses and this helped me a lot during the project. See my DataCamp statement of accomplishments in [here](https://github.com/Hassanyare/Minor_Applied_Data_Science/tree/master/DataCamp). Furtheremore, i did a lot of research on how to use certain codes and how to write object oritented python code. I would like to thank my felow students from programming background who helped me write better code.
## 2.2 Machine learning
The machine learning lectures helped me understand the bigger picture of machine learning and how to apply different techniques. To keep up with all the different terms in Datascience and machine learning in particular, i made a list of terms that were new to me. For this list you can find it [here](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Machine%20Learning%20Terms.pdf).
For practice on what we learnt on machine learning lectures, i was able to make a classification on the left and right arm of converted data. For the this see this [Reader](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/machine-learning/machine_learning.md).
## 2.3 Online course
I was also able to follow this online course on [udemy](https://www.udemy.com/course/machine-learning-with-tensorflow-for-business-intelligence/). From this course i understood the basic concepts of deep neural networks. For the summary i wrote on this course, see this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/summary_deeplearning.pdf). I was able to complete the entaire course except the business case. For the exercises i did during this course see this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/tree/master/udemy_course). Apart from this course i read multiple artikles on convolutional neural networks and how to optimize the hyper-parameters. For further of neural networks that i have applied during this project see this chapter 7. 

# 3. Project Ortho Eyes
## 3.1 Project's scope and relevance

Project orth eyes is a collaboration between the Hague univeristy of Applied Sciences and Leiden University Medical Center (LUMC). The project focuses on Improving treatment and diagnosis of musculoskeletal system issues, and in particular issues related with shoulder disabilities. When treating patients with limitations in shoulder movement, physio therapist use protractor or sensor system to measure the limitations of the shoulder. The former is inaccurate while the later is time consuming. 

The long term goal of the project is therefore to find an easy and accurate measurement system. The short term goals is: Is it possible to cluster patients in groups with similar complaints and / or similar diagnosis based on the flock of birds data? What parameters are used for this clustering?

## 3.2 Strategy and planning

This is not the first iteration of the project, There have been two other iterations of this project. After fact checking the [research](https://github.com/Hassanyare/Applied-Data-Science/blob/master/paper_ortho_eyes.pdf) done by last group, we found that they made a sumptions on the columns(bone names) and labeling the exercises. That is why we would like redo their analysis using labeled data by LUMC physicians to categorize the patient groups. 

Furthermore, at the beginning of the semister i was able to write down a [coopration](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Cooperation%20agreement.pdf) agreement that could help us a project group to finish the project succesfully. As mentioned in the agreement, we used Microsoft DevOps as a scrum tool. How scrum is used is explained in the Coopration agreement. 

<details>
  <summary>Here are the tasks that i did during this minor. </summary>

|  |      |     |      |    |     |  
|-:|----| --- | --- | --- | --- | 
|ID|Work Item Type|Title|State|Area Path|Changed Date
|191|Task|Data: CNN datashape|To Do|Data Science|12/16/2019 2:05 PM
|183|Task|Data: Remove Idle|Doing|Data Science|1/10/2020 9:53 AM
|175|Task|Find the best architecture for CNN|Doing|Data Science|12/20/2019 9:37 AM
|169|Task|Log result of the CNN script|Done|Data Science|12/12/2019 6:32 AM
|155|Task|Understand how to train and improve RNN's|Done|Data Science|12/3/2019 7:47 PM
|148|Task|Listing reached goals|Done|Data Science|11/19/2019 2:12 PM
|134|Task|Check if the idle at the start and end of an exercise is an anomaly|Done|Data Science|11/15/2019 9:07 AM
|121|Task|creating dataframe of 650 columns for the ml model|Done|Data Science|10/24/2019 9:01 PM
|120|Task|read in filenames, files, and create metadata.|Done|Data Science|10/24/2019 9:01 PM
|106|Task|I would like to make a presentation on how the data is prepared for ml mdoels|Done|Data Science|10/31/2019 9:57 AM
|101|Task|Write and train a ML model on our data|Done|Data Science|10/31/2019 9:55 AM
|81|Task|Understand the conversion of the original data to csv. The convertion with matlab|Done|Data Science|12/16/2019 1:13 PM
|69|Task|What kind of parameters are (ideally) used by the doctors / researchers?|Done|Data Science|10/12/2019 9:22 AM
|33|Task|General projectplanning|Done|Data Science|9/11/2019 2:08 PM
|31|Task|Cooperation agreement|Done|Data Science|9/11/2019 2:07 PM
|27|Task|define the process used to clean the data|Done|Data Science|9/16/2019 9:03 AM
|22|Task|Read paper|Done|Data Science|9/16/2019 9:03 AM
|10|Task|Hassan|Done|Data Science|9/6/2019 9:30 PM

</details>


# 4. The dataset
In this projcet we are using motion data optained from the Laboratorium for Kinematics en Neuromechanics (LK&N)
of LUMC. The data is recorded using the flock of birds system (FoB), A six-degrees-of-freedom electromagnetic measurement system that measures the position and orientation data of targerts. 


![flock-of-birds-system](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/FOB.png)

The sensors from the FoB are placed on fixed positions on a patient and the patient does exercises as instructed by a physician.The sensors then return the position (X,Y,Z coordinates) of the each sensor. This raw data is later converted to rotation angel relative to each bone by the LUMC. 

</details>

See the figure below, made by [Vincent](https://github.com/Vincentvdoord/Data-Science-KB-74), member of ortho eyes 2018/2019.

<details>
  <summary>Position-of-sensors</summary>

![Position-of-sensors](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/sensors.png). 

</details>

<details>
  <summary>This is how the data of an exercise look like:</summary>

![exercise-data](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/exercise.PNG)

</details>

The dataset consists of patient groups (4 in total) with similar complaints and or diagnostics. Each patient group consists of multiple patients and each patient has done multiple exercises. There are 5 main exercises that  all the patients have in common:

|Abbreviation |Describtion                |
|------------:|--------------------------:|
| AB          | Abduction                 |
| AF          | Anteflexion               |
| RF          | Retroflexion              |
| EH          | Endo/Exorotation coronal  |
| EL          | Endo/Exorotation humerus  |


## 4.1 Data visualizations

The visualization below made by [Raphi](https://github.com/djbob0/Data-Science-Minor) and [Eddie](https://github.com/v3rslu1s/Applied-Datascience) helped me understand how the data is represented. 

<details>
  <summary>Visualizations-Gif</summary>

![Visualizations-converted-data](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/Visualization.gif)

</details>

<details>
  <summary>2D-Visualization</summary>

![Visualizations-converted-data](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/all_the_data_vis.png)

</details>

# 5. Data Cleaning and Enrichment                                                    
## 5.1 Data Cleaning

Steps in data cleaning are:

| Type                              | What they are:                                              |     
| ---------------------------------:|------------------------------------------------------------:|
| Removing idle                     | Removing stationary data at the start and end of exercises  |
| Splitting Double exercises        | Detect and splitting of double exercises in one file.       |    
| Detect wrongly named exercises    | ie: if a file is named Incorrectly.                         |


### 5.1.1 Removing the idle

After inspecting the sensor data, we noticed that almost every exercise contained an idle at the beginning and end of each exercise. An idle comes to exist between the time when a physician starting or stops the recording, and the patient actual starts or stops the exercise. In between these moments exists an almost stationary movement that is not part of the exercise.  

Removing the idle was one of the tasks I did during this minor. To remove the idle I developed a script that detects when a the movement is below or above the mean of the data at the start or end of the exercise. More this, see this [Reader](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/machine-learning/Removing_idle.md)


## 5.2 Data Enrichment

These are the data enrichments we did.  

| Type                 | What they are:                                                                      |  
| ---------------------|:-----------------------------------------------------------------------------------:|
| Default (n frames)   | Taking n frames(exercise length) that are evenly spaced from each exercise          |
| Resample exercises   | Reframing all the exercises into a fixed frames (exercise length)                   |
| Frame generator      | selecting more data points before and after each (n)frame,                          |
| occupied space (360) | The space decribtion of an exercise. The movement of each exercise in 360 space     |

# 6. Neural Networks
## 6.1 Convolutional neural network

A convolutional neural network is a Deep Learning algorithm which can classify images by assigning importance to various aspects of the image. By read this [paper](https://arxiv.org/pdf/1610.07031.pdf), which used Convolutional neural networks on classification of motion data, i was motivated in trying to use this technique. I used Convolutional neural networks in classifing patients in groups with similar complaints using the flock of birds data. 


# Convolutional neural networks (CNN)

Since CNN works well with image data, I created an Image data from the resampled exercises. For more on this see data preparation. I used [Tensorflow](https://www.tensorflow.org/) to build the model, because i had a course on these library and there are a lot of information about it online. 

## Data prepration

After trying other options, i found that classifying the patient groups on exercise level works best for CNN without any biases. 

For preparing image data these are the steps I took.

- Use the resampled exercise data since these ones have fixed rows(frames)	
- Generate image data for each exercises.
- Reshape the features that belong together into an RGB format
    - Reshape the x,y,z coordinates of one body part into an RGB format
-	Place a decoder [colour bar] between the bones for the model to better differentiate between them 
-   Normalize the data to be values between 0 and 1: this is good for the model

<details>
  <summary>Genarated image from the converted data
</summary>
  
![RGB-1](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/RGB.png)
    
![image](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/data-resampled-color.png)

</details>

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

See this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/cnn_model.py) for the complete code of the model.

## Results

These are the results of the model.

|Accuracy |precision| recal |F1-score|
|---------|---------|---------|------|
| 0.726   |0.657    |0.605    |0.630 |


<details>
  <summary>The graphs below, show the loss and accuracy of the model on the train and validation dataset. 
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


<details>
  <summary>These are the predictions per class on the train dataset. I used excel to calculate these predictions.
</summary>

![predictions-per-class](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/predictions.PNG)

</details>


# 7. Research 

For research we come up we with the main question below. 

***To what extend and in what way, can different supervised data science techniques be used on kinematic recordings to contribute to a more valid and more reliable diagnosis, made by a doctor, on shoulder disability.***

Furthermore we come up with a list of sub-questions that would insist us answering our main question. For the subquestions, see the this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Research-paper/Possible%20Research%20Questions.pdf) 

For the contributions to the research see my self reflection.

## 7.1 Evaluation 

According to the research I did with my fellow students, i found that after extensive data cleaning, the logistic regression was not able to classify patient group 2 from 3. After i tried CNN on the same dataset, after cleaned it gave better results in differentiating patient group 2 from 3. That is why i recommend the next project group to look at CNN as an alternative model than logistic regression. 

## 7.2 Conclusion 

Given the research question mention above, after extensive data cleaning and data normalization, the logistic rigression gave and accuracy of 69% and precision and recall of:

![metrices](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/foto's/LG-RG.PNG)

This shows that logistic regression is able to classify(cluster) patients in groups with simialar complaints and or similar diagnosis based on the FoB flock of birds data. 


# 8. Presentations

These are the [presentation](https://github.com/Hassanyare/Minor_Applied_Data_Science/tree/master/presentation) i did during this minor.
# 9. Reference to Git commits

See this [Reader](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/git-commits.md) for all my git commits on the project. 


# 10. Self reflection

For the self reflection see this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Reflection.pdf).


![Group-picture](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/group-foto.PNG)

