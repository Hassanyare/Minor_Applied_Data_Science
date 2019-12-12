from sklearn.linear_model import LogisticRegression

from ml.modelinterface import MlInterface

import numpy as np 

class LogisticRegressionModel(MlInterface):
    
    # def __init__(self,*args,**kwargs):#,**kwargs):
    #     self.model = LogisticRegression(*args,**kwargs)#,**args)

    def __init__(self, clf = None, *args,**kwargs):
        if clf is None:
            clf = LogisticRegression(*args,**kwargs)
        super().__init__(clf)
 
    def train(self, x, y):
        self.clf.fit(x, y)

    def predict(self, data):
        return self.clf.predict(data)
