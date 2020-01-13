# Minor_Applied_Data_Science
Welcome to my portfolio on the tasks I have done and been part of during my minor Applied data science at the Hague University of Applied Sciences. 

I am a third year Civil Engineering student at The Hague university of Applied Science. I am interested in statistics and probability related problems. 

The reason I choose this minor is because there is more data available in the civil engineering sector now than ever before. Data science is the most effective way in gaining insight in large amount of data. I would like to combine the knowledge I gained during my minor with my civil engineering major.

# Table of Contents

- [1. Jargon](#1-Jargon)

- [2. Personal development](#2-Personal-development)
  - [2.1 DataCamp courses](##21-DataCamp-courses)
  - [2.2 Machine-learning](##22-Machine-learning)
  - [2.3 Online course](##23-Online-course)

- [3. Project Ortho Eyes](#3-Project-Ortho-Eyes)
  - [3.1 Project's scope and relevance](##31-Project's-scope-and-relevance)
  - [3.2 Strategy](##32-Research-proposal)
     - [3.2.1 Reproducing last group's work](###321-Reproducing-last-groups-work)
     - [3.2.1 Research proposal](###321-Research-proposal)
     
- [4. The data as we know](#4-The-data-as-we-know)
  - [4.1 Flock of birds system](##41-Flock-of-birds-system)
  - [4.1 Raw visualization](##41-Raw-visualization)
  - [4.1 Visualizations converted data](##41-Visualizations-converted-data)

- [5. Data Cleaning and Enrichment](#5-Data-cleaning-and-Enrichment)
  - [5.1  Data Cleaning](##51-Data-Cleaning)
     - [5.1.1 Removing the idle](###511-Removing-the-idle)
  - [5.2 Data enrichment](##52-Data-enrichment)

- [6. Logistic regression model](#6-Logistic-regression-model)
     - [6.1 Data prepration](##61-Data-prepration)
     - [6.2 Models](##62-Models)
     - [6.3 Results](##63Results)
     - [6.4 Models evaluations](##64-Models-evaluations)

 - [7. Neural Networks](#8-Neural-Networks)
     - [7.1 Recurrent neural network (RNN)](#81-recurrent-neural-network-(RNN))
     - [7.2 Convolutional neural network](#82-convolutional-neural-network)

- [8. Research paper](#7-Research-paper)
- [9. Presentaties](#7-Presentaties)
- [10. Self reflection](#7-Self-reflection)

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
For practice on what we learnt on machine learning lectures, i was able to make a classification on the left and right arm of converted data. For the code see this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/src_machine-learning/machine_learning.md). For furthere machine learning application see chapter 6.
## 2.3 Online course
I was also able to follow this online course on [udemy](https://www.udemy.com/course/machine-learning-with-tensorflow-for-business-intelligence/). From this course i understood the basic concepts of deep neural networks. For the summary i wrote on this course, see this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/summary_deeplearning.pdf). I was able to complete the entaire course except the business case. For the exercises i did during this course see this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/tree/master/Neural_Networks). Apart from this course i read multiple artikles on convolutional neural networks and how to optimize the hyper-parameters. For further of neural networks that i have applied during this project see this chapter 7. 

# 3. Project Ortho Eyes
## 3.1 Project's scope and relevance

Project orth eyes is a collaboration between the Hague univeristy of Applied Sciences and Leiden University Medical Center (LUMC). The project focuses on Improving treatment and diagnosis of musculoskeletal system issues, and in particular issues related with shoulder disabilities. When treating patients with limitations in shoulder movement, physio therapist use protractor or sensor system to measure the limitations of the shoulder. The former is inaccurate while the later is time consuming. 

The long term goal of the project is therefore to find an easy and accurate measurement system. The short term goals is: Is it possible to cluster patients in groups with similar complaints and / or similar diagnosis based on the flock of birds data? What parameters are used for this clustering?

## 3.2 Strategy and planning

This is not the first iteration of the project, There have been two other iterations of this project. To build upon the [research](https://github.com/Hassanyare/Applied-Data-Science/blob/master/paper_ortho_eyes.pdf) done by last group, we decided to redo their analysis and validate their results. Furthermore we planned on doing research on new techniques, other than the ones last group used, to categorize the patient groups. 

See the figure below for our long term plan.

![LONG-TERM-PLAN](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/plan.PNG)

At the beginning of the semister i was able to write down a [coopration](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Cooperation%20agreement.pdf) agreement that could help us a project group to finish the project succesfully. As mentioned in the agreement, we used Microsoft DevOps as a scrum tool. How scrum is used is explained in the Coopration agreement. 

Here are the tasks that i did during this minor. 

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

### 3.2. Research proposal
For the reseach paper we come up we with the reserach question below. 

***To what extend and in what way, can different data science techniques be used on kinematic recordings to contribute to a more valid and more reliable diagnosis, made by a doctor, on shoulder disability.***

Furthermore we come up with a list of sub-questions that would insist us answering our main question. For the subquestions, see the this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Research-paper/Possible%20Research%20Questions.pdf) 

# 4. The dataset
In this projcet we are using motion data optained from the Laboratorium for Kinematics en Neuromechanics (LK&N)
of LUMC. The data is recorded using the flock of birds system (FoB), A six-degrees-of-freedom electromagnetic measurement system that measures the position and orientation data of targerts. 

![flock-of-birds-system](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/FOB.png)

The sensors from the FoB are placed on fixed positions on a patient and the patient does exercises as instructed by a physician.The sensors then return the position (X,Y,Z coordinates) of the each sensor. This raw data is later converted to rotation angel relative to each bone by the LUMC. See the figure below, made by [Vincent](https://github.com/Vincentvdoord/Data-Science-KB-74), member of ortho eyes 2018/2019.

![Position-of-sensors](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/sensors.png). 

The dataset consists of patient groups (4 in total) with similar complaints and or diagnostics. Each patient group consists of multiple patients and each patient has done multiple exercises. There are 5 main exercises that  all the patients have in common, these are:

|Abbreviation |Describtion                |
|------------:|--------------------------:|
| AB          | Abduction                 |
| AF          | Anteflexion               |
| RF          | Retroflexion              |
| EH          | Endo/Exorotation coronal  |
| EL          | Endo/Exorotation humerus  |


## 4.1 Data visualizations

The visualization below made by [Raphi](https://github.com/djbob0/Data-Science-Minor) and [Eddie](https://github.com/v3rslu1s/Applied-Datascience) helped me understand how the data is represented. 

![Visualizations-converted-data](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/Visualization.gif)



![Visualizations-converted-data](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/all_the_data_vis.png)


# 5. Data Cleaning and Enrichment                                                    
## 5.1 Data Cleaning

Steps in data cleaning are:

| Type                              | What they are:                                              |     
| ---------------------------------:|------------------------------------------------------------:|
| Removing idle                     | Removing stationary data at the start and end of exercises  |
| Splitting Double exercises        | Detect and splitting of double exercises in one file.       |    
| Detect wrongly named exercises    | ie: if a file is named Incorrectly.                         |


### 5.1.1 Removing the idle
![Removing-the-idle](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/removing%20the%20idle.png)


After inspecting the sensor data, we noticed that almost every exercise contained an idle at the beginning and end of each exercise. An idle comes to exist between the time when a physician starting or stops the recording, and the patient actual starts or stops the exercise. In between these moments exists an almost stationary movement that is not part of the exercise.  

Removing the idle was one of the tasks I did during this minor. To remove the idle I developed a script that detects when a the movement is below or above the mean of the data at the start or end of the exercise. More this, see this [Reader](C:\Users\hassa\OneDrive\Desktop\Minor_Applied_Data_Science\machine-learning\Removing_idle.md)


## 5.2 Data Enrichment

The exercises 

| Type                 | What they are:                                                                      |  
| ---------------------|:-----------------------------------------------------------------------------------:|
| Default (n frames)   | Taking n frames(exercise length) that are evenly spaced from each exercise          |
| Resample exercises   | Reframing all the exercises into a fixed frames (exercise length)                   |
| Frame generator      | selecting more data points before and after each (n)frame,                          |
| occupied space (360) | The space decribtion of an exercise. The movement of each exercise in 360 space     |


**Resample exercises** 

![Resampleexercises](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/resampled-exer.png)


# 6. Logistic regression model
## 6.1 Data prepration
## 6.2 Models
## 6.2 Results
## 6.3 Evaluation of the models

# 7. Neural Networks
## 7.1 Recurrent neural network (RNN)
## 7.2 Convolutional neural network

blaaaaah, blaaaaah

Fill in this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Neural-networks/CNN.MD) for cnn model.

# 8. Research paper

# 9. Presentations

These are the [presentation](C:\Users\hassa\OneDrive\Desktop\Project_py\Minor_Applied_Data_Science\presentation) that I gave during this minor.

# 10. Self reflection

For the self reflection see this [link]().

For the links to all my git commits during this semester, see this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/git-commits.md)


![Group-foto](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/group-foto.PNG)
