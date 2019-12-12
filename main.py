
from dicts.body import Body as B
from parser import Parser
from visuzalizer import Visualizer
from metadata import MetaData

import matplotlib.pyplot as plt

def visualise_difference():
    # Importing cleaned file / original file 
    data = Parser('data/Cat2_pat3_meting10_oef4.csv')
    datasplit = Parser('Data%20Science/data/Cat1_pat1_meting10_oef5_split1.csv')
    
    # Setting the preferable bodypart 
    data.set_bodypart('thorax', 'r')
    datasplit.set_bodypart('thorax', 'r')

    # Requesting the first rows of the splitted dataset 
    data_firstrow = datasplit.first_rows() 

    # Finding the start index of the cleaned data in the full dataset, based on the first rows
    datasplit_startnum = data.find_row_index(data_firstrow) 
    # Calculating the last index by getting the start index + the size of the cleaned data
    datasplit_endnum = datasplit_startnum + datasplit.dataframe_size() 

    # Printing information
    print('split start:', datasplit_startnum)
    print('split ends:', datasplit_endnum)
    print('total size:', data.dataframe_size())

    # Creating a nice plot
    plt.plot(data.bodypart)

    # Setting the red lines
    plt.axvline(x=datasplit_startnum, c='r')
    plt.axvline(x=datasplit_endnum, c='r')
    plt.axvline(x=6, c='b')
    plt.axvline(x=80, c='b') 
    
    # Showing the plot
    plt.title(data.bodypart.columns[0] + ' | ' + data.get_filename())
    plt.legend()
    plt.show()
    # thorax_r = df.get_bodypart(B.part['THORAX_R'])
    # Visualizer.flat(thorax_r)




if __name__ == '__main__':
    meta = MetaData('Data%20Science/data/AllMetaData - All.csv')
