
# How the scripts Removing the idle works

## The Code
The code looks only at one column (bone: humerus_r_y_plane) because here is where the idle is most Visibel. After getting the data of this one column, i used numpy's funcion [np.cumsum](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cumsum.html) to calculate the moving average filter to remove noise out of the data. I then calculated the difference between the subsequent values using numpy function [np.diff](https://docs.scipy.org/doc/numpy/reference/generated/numpy.diff.html). Further more I split the exercise into 3 equal parts, which can be extended upto 6 parts. I tested different splits and three was the optimal amount of splits. 


``` python
"TODO: 
- Calculate the moving average 
- Calculate the diff 
- Calculate the mean for the start and end
- save the outcome of start and into a variable
"

Class Removeidle:

    exercise_bone = { 
            'AB' : ('humerus_r_y_plane', 1.5),
            'AF' : ('humerus_r_y_plane', 1.5),
            'EL' : ('humerus_r_y_plane', 1.5),
            'RF' : ('humerus_r_y_plane', 1.5),
            'EH' : ('humerus_r_y_plane', 1.5),
        }

    def moving_average(self, a, n=3) :
        ret = np.cumsum(a, dtype=float)
        ret[n:] = ret[n:] - ret[:-n]
        return ret[n - 1:] / n

    def __init__(self, exercise):
        self.exercise = exercise 
        self.bone, self.variatie = Removeidle.exercise_bone[self.exercise.exercisegroup]

        self.np_data = self.exercise.df[self.bone].to_numpy()

        self.difference = np.diff(self.moving_average(self.np_data))
        difference_split = np.array_split(self.difference, 6)
        self.difference_start = difference_split[0]
        self.difference_end = difference_split[-1]
        self.lenght = len(self.np_data)
 
        end = self.end() 
        start = self.start() 

        if start < end:
            df_range = list(range(start, end)) 
            self.df = self.exercise.df.iloc[df_range].copy() 
        else:
            self.df = self.exercise.df  


"TODO: 
- Calculate the satrt_mean (average)
- caluculate mean_min (reduce the mean by 10% ) and mean_max (extend the mean by 10%) to be tolerant for outliners. 
- Check when values from difference_start are greater/less than the mean
- save the outcome of start and end into a variable

"

def start(self):
        self.mean_start = np.mean(self.difference_start)
        
        variatie = self.variatie

        found = False 
        while not found: 
            if self.mean_start < 0: 
                mean_start_min = self.mean_start - (self.mean_start * -variatie)
                mean_start_max = self.mean_start + (self.mean_start * -variatie) 
            else:
                mean_start_min = self.mean_start - (self.mean_start * variatie)
                mean_start_max = self.mean_start + (self.mean_start * variatie)

            lijst = []
            for index, value in enumerate(self.difference_start): 
                if self.difference_start[0] > mean_start_max:
                    if value < mean_start_min: 
                        lijst.append(index)
                        # plt.plot(index, value, marker='o', markersize=3, color="red")
                elif self.difference_start[0] < mean_start_min:
                    if value > mean_start_max: 
                        lijst.append(index)
                        # plt.plot(index, value, marker='o', markersize=3, color="red")
                else:  
                    if value > mean_start_max or value < mean_start_min:
                        lijst.append(index) 
                        # plt.plot(index, value, marker='o', markersize=3, color="red")
            if lijst: 
                if len(lijst) > (len(self.difference_start)  * 0.5):
                        variatie = variatie * 1.3 
                else:   
                    found = True 
            else:
                variatie = variatie * 0.6  
        return lijst[0]


def end(self):
    self.mean_end = np.mean(self.difference_end)
    variatie = self.variatie
    found = False 

    while not found: 
        if self.mean_end < 0: 
            mean_end_min = self.mean_end - (self.mean_end * -variatie)
            mean_end_max = self.mean_end + (self.mean_end * -variatie) 
        else:
            mean_end_min = self.mean_end - (self.mean_end * variatie)
            mean_end_max = self.mean_end + (self.mean_end * variatie)

        lijst = [] 
        
        reversed_list = np.flip(self.difference_end)

        for index, value in enumerate(reversed_list): 
            index = self.lenght - index - 1
            if reversed_list[0] > mean_end_max:
                if value < mean_end_min: 
                    lijst.append(index)
                    # plt.plot(index - 2, value, marker='o', markersize=3, color="red")
            elif reversed_list[0] < mean_end_min:
                if value > mean_end_max: 
                    lijst.append(index)
                    # plt.plot(index - 2, value, marker='o', markersize=3, color="red")
            else:  
                if value > mean_end_max or value < mean_end_min:
                    lijst.append(index) 
                    # plt.plot(index - 2, value, marker='o', markersize=3, color="red")
        if lijst: 
            if len(lijst) > (len(self.difference_end)  * 0.5):
                variatie = variatie * 1.3 
            else:   
                found = True 
        else:
            variatie = variatie * 0.6   
    return lijst[0]


```


## Visualization:

I used [Raphi's](https://github.com/djbob0/Data-Science-Minor) code to see if the remove idle function worked correctly. The figure shows the Abduction(AB) exercise(both the left and right limb) done done by patient 1 of category 1. See the code and figure below.

```Python 

#calling the function to visualize Remove idle
vv = Visualize(patient_groups,catagory = [1], patients=[5], exercises=['AB'], bones=["thorax_r_x_ext"])

# vv.visualise(mode='exercise')
# The red and blue line indicate the satrt and end of one limb, while the brown line indicates the other limb.
vv.visualise(mode = 'idle')

```

![Removing_the_idle](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/Visualization-idle.png)

![Removing-the-idle](https://github.com/Hassanyare/Minor_Applied_Data_Science/blob/master/fotos/removing%20the%20idle.png)


## Results
These are the results of logistic regression model when the remove idle function is off/on. The data used is the resampled exercises. 


| Accuracy  | remove_idle   | resample_exercise  |                
| ----------|:--------------|-------------------:|
| 0.639306  | False         | True               |



| Accuracy  | remove_idle   | resample_exercise  |                
| ----------|:--------------|-------------------:|
| 0.661272  | True          | True               |


The script worked well on the resempled exercises, and helped increase the overal accuracy when resempled exercise is on. This means that the code helped increase the accuracy of some models. 

## Conclusion:

The remove idle was a useful configuration for some models, howere it did not contribute to the top results of the different configurations we run. 