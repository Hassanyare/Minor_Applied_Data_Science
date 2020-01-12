# Minor_Applied_Data_Science
Welcome to my portfolio on the tasks I have done and been part of during my minor Applied data science at the Hague University of Applied Sciences. 

I am a third year Civil Engineering student at The Hague university of Applied Science. I am interested in statistics and probability related problems. 

The reason I choose this minor is because there is more data available in the civil engineering sector now than ever before. Data science is the most effective way in gaining insight in large amount of data. I would like to combine the knowledge I gained during my minor with my civil engineering major.

# Table of Contents

- [1. Jargon](#1-Jargon)
- [2. Personal development](#2-Personal-development)
  - [2.1 DataCamp courses](#21-DataCamp-courses)
  - [2.2 Machine-learning](#22-Machine-learning)
  - [2.3 Online course](#23-Online-course)
- [3. Project Ortho Eyes](#3-Project-Ortho-Eyes)
  - [3.1 Project's scope and relevance](#31-Project's-scope-and-relevance)
  - [3.2 Strategy](#32-Research-proposal)
     - [3.2.1 Reproducing last group's work](#321-Reproducing-last-groups-work)
     - [3.2.1 Research proposal](#321-Research-proposal)
- [4. The data as we know](#4-The-data-as-we-know)
  - [4.1 Flock of birds system](#41-Flock-of-birds-system)
  - [4.1 Raw visualization](#41-Raw-visualization)
  - [4.1 Visualizations converted data](#41-Visualizations-converted-data)
- [5. Machnine Learning](#5-Machnine-Learning)
  - [5.1 Machine learning Lectures](#51-Machine-learning-Lectures)
  - [5.1 Preparing data for Machine learning model](#51-Preparing-data-for-Machine-learning-model)
- [6. Data Cleaning and Enrichment](#6-Data-cleaning-and-Enrichment)
  - [6.1 Steps in cleaning The data](#61-Steps-in-cleaning-the-data)
  - [6.2 Removing the idle](#62-Removing-the-idle)
  - [6.3 Different methods of data enrichment](#63-Different-methods-of-data-enrichment)
- [7. Logistic regression model](#7-Logistic-regression-model)
     - [7.1 Configuration](#71-configuration)
     - [7.2 Outcome of the model](#72-Outcome-of-the-model)
     - [7.2 model evaluation](#72-model-evaluation)
 - [8. Neural Networks](#8-Neural-Networks)
     - [8.1 recurrent neural network (RNN)](#81-recurrent-neural-network-(RNN))
     - [8.2 convolutional neural network](#82-convolutional-neural-network)

- [9. Research paper](#7-Research-paper)
- [10. Presentaties](#7-Presentaties)
- [11. Self reflection](#7-Self-reflection)

# 1. Jargons

| What:                | Meaning:                                                        |     
| ---------------------|:---------------------------------------------------------------:|
| Raw data             | Data from the Flock of birds system(FoB)                        |
| Converted Data       | transformed data from ..... to Euler angles                     |     
|                      |                                                                 |   

# 2. Personal-development
## 2.1 DataCamp courses
During the first few weeks of the minor i mostly worked on my python skills. I was able to finish the data camp courses and this helped me a lot during the project. See my DataCamp statement of accomplishments in [here](https://github.com/Hassanyare/Minor_Applied_Data_Science/tree/master/DataCamp). Furtheremore, i did a lot of research on how to use certain codes and how to write object oritented python code. I would like to thank my felow students from programming background who helped me write better code.
## 2.2 Machine learning
The machine learning lectures helped me understand the bigger picture of machine learning and how to apply different techniques. To keep up with all the different terms in Datascience and machine learning in particular, i made a list of terms that were new to me. For this list you can find it [here](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Machine%20Learning%20Terms.pdf).
For practice on what we learnt on machine learning lectures, i was able to make a classification on the left and right arm of converted data. For the code see this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/src_machine-learning/left_right_clf.py). For furthere machine learning application see chapter 5 and 7.
## 2.3 Online-course
I was also able to follow this online course on [udemy](https://www.udemy.com/course/machine-learning-with-tensorflow-for-business-intelligence/). From this course i understood the basic concepts of deep neural networks. For the summary i wrote on this course, see this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/summary_deeplearning.pdf). I was able to complete the entaire course except the business case. For the exercises i did during this course see this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/tree/master/Neural_Networks). Apart from this course i read multiple artikles on convolutional neural networks and how to optimize the hyper-parameters. 

# 3. Project Ortho Eyes
## 3.1 Project's scope and relevance

Project orth eyes is a collaboration between the Hague univeristy of Applied Sciences and Leiden University Medical Center. The project focuses on Improving treatment and diagnosis of musculoskeletal system issues, and in particular issues related with shoulder disabilities. When treating patients with limitations in shoulder movement, physio therapist use protractor or sensor system to measure the limitations of the shoulder. The former is inaccurate while the later is time consuming. 

The long term goal of the project is therefore to find an easy and accurate measurement system. The short term goals is: Is it possible to cluster patients in groups with similar complaints and / or similar diagnosis based on the flock of birds data? What parameters are used for this clustering?

## 3.2 Strategy 

Since this is not the first iteration of the project, we decided to redo the analysis of last groups work and build upon their work. We also planned on doing research on new techniques, other than the ones last group used, to categorize the patient groups.

![LONG-TERM-PLAN](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/plan.PNG)

During the beginning of the semister i was able to write down a cooperation agreement that could help us a project group to finish the project succesfully. For the coopartion agreement see this [link](C:\Users\hassa\OneDrive\Desktop\Project_py\Minor_Applied_Data_Science\Cooperation agreement.pdf)

As mentioned in the coopration agreement we used Microsoft DevOps as a scrum tool. Here is the link to the task i was apple to complete.
[Link-to-workitems](https://dev.azure.com/DataScienceMinor/Data%20Science/_workitems/recentlyupdated/)

### 3.2.1 Reproducing last group's work
After inspecting the work from last group, we noticed that there were a lot of assumptions made in cleaning and preparing the dataset. This is why we it took as more than we expected  to finish the first part of our project. 

### 3.2.2 Research proposal
For the reseach paper we come up we with the reserach question below. 

***To what extend and in what way, can different data science techniques be used on kinematic recordings to contribute to a more valid and more reliable diagnosis, made by a doctor, on shoulder disability.***

Furthermore we come up with a list of sub-questions that would insist us answering our main question. For the subquestions, see the this [link](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/Research-paper/Possible%20Research%20Questions.pdf) 

## 4.1 Raw visualization
# 4. The data as we know
## 4.1 Flock of birds system
![Group-foto](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/group-foto.PNG)
## 4.1 Raw visualization
## 4.1 Visualizations converted data
![Visualizations-converted-data](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/all_the_data_vis.png)

# 5. Machnine Learning
## 5.1 Preparing data for Machine learning model
## 5.2 The model
# 6. Data Cleaning and Enriching
   
                                                    
## 6.1 Steps in cleaning the data
The steps in data cleaning are:

## 6.2 Removing the idle
![Removing-the-idle](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/removing%20the%20idle.png)
## 6.3 Different methods of data enrichment

The types of data enrichment are: 

| Type                 | What they are:                                                  |     
| ---------------------|:---------------------------------------------------------------:|
| Resample exercises   | Reframing all the exercises into a certain frames (rows)        |
| Frame generator      |                                                                 |     
| occupied space (360) |                                                                 |     


**Resample exercises** 

![Resampleexercises](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/resampled-exer.png)

[See_work_done](https://dev.azure.com/DataScienceMinor/_git/Data%20Science/commits?user=Hassan%20Ali&userId=d934e663-8e4d-6975-8940-c5dba5e7403e&historyType=2)
# 7. Logistic regression model
## 7.1  Configurations
## 7.2 Outcome of the model
## 7.3 Model evaluation
# 8. Neural Networks
## 8.1 Recurrent neural network (RNN)
## 8.2 Convolutional neural network
# 9. Research paper
# 10. Presentations
# 11. Self reflection




