import os

from patient.patientfolder import Patient

class PatientGroup:

    def __init__(self,path):
        self.path = path
        self.patients= list()

        #going through the a category and creates a list with all the patients

        if os.path.exists(self.path):
            
            for name in os.listdir(self.path):
                patientpath = os.path.join(path, name)

                #checking if name is a folder
                if os.path.isdir(self.path):
                    self.patients.append(Patient(patientpath))
               
            else:
                pass # raise Filenot exist
            
            print('Total patients in category', len(self.patients))

