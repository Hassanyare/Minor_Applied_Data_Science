import pandas as pd
import numpy as np
import os 

from tools.config import config

class Exercises:
    
    def __init__ (self, path):
        self.path = path

        # csv file inlezen 

        self.data = pd.read_csv(self.path, names=list(range(30)))

        colnames = {0: "thorax_r_x", 1: "thorax_r_y", 2: "thorax_r_z",
            3: "clavicula_r_x", 4: "clavicula_r_y",
            5: "clavicula_r_z",
            6: "scapula_r_x", 7: "scapula_r_y", 8: "scapula_r_z",
            9: "humerus_r_x", 10: "humerus_r_y", 11: "humerus_r_z",
            12: "ellebooghoek_r",
            15: "thorax_l_x", 16: "thorax_l_y", 17: "thorax_l_z",
            18: "clavicula_l_x", 19: "clavicula_l_y",
            20: "clavicula_l_z",
            21: "scapula_l_x", 22: "scapula_l_y", 23: "scapula_l_z",
            24: "humerus_l_x", 25: "humerus_l_y", 26: "humerus_l_z",
            27: "ellebooghoek_l"}

        self.data = self.data.rename(columns= colnames)

        self.df = self.data[config.columns]

        self.soorted_exercise_left = self.df_regex(r"._l_.")
        self.soorted_exercise_right = self.df_regex(r"._r_.")


        self.dataframe = self.data[config.columns].iloc[self.get_frames()]
      
        #compute the numpy array of dataframe by using .to_numpy
        self.np_data = self.dataframe.to_numpy()

        # extracting path exercise type and type of exercise 
        exercisepath, exercisestype = os.path.split(self.path)

        #extracting patientid from path

        grouppath, self.patientid = os.path.split(exercisepath)

        #extracting patientgroup and exercisetype from patientgategory and exercise name  respectively, by indexing the position of the string.

        self.patiengroup = grouppath[-1]
        self.execerisegroup = exercisestype[:2]

    
    def total_rows(self):
        return int(self.data.size / len(self.data.columns))

    def get_frames(self):
        frames = []
        total_rows = self.total_rows() - 1
        for index in range(1, config.frames_counts + 1):
            frames.append(int((total_rows/ config.frames_counts) * index))
        return frames
    
    
    def df_regex(self, pattern):
        # Left          r"._l_."
        # Right         r"._r_."
        return self.df.filter(regex=(pattern))

