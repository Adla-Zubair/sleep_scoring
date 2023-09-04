# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:38:03 2023

@author: WS3

- The given python code uses txt files containing the annotations for sleep stages scored to the same subject by two scorers.
- The file is faulty wherein the time epochs are not completely overlapping. 

"""


# Importing required libraries
import pandas as pd
import mne
import glob
import numpy as np
from sklearn.metrics import cohen_kappa_score
from tkinter.filedialog import askdirectory

path_files = '/serverdata/ccshome/adla/'


#%%
# Loading dataset containing the scored sleep data


# Opening a UI asking to select scored EDF files
scored_files = askopenfilenames(title = "Select Scored files",
                              filetypes = (("CSV file","*.csv"),
                              ('All files', '*.*')))

files_by_krishan  = glob.glob(path_files + '/*reduced_krishan.csv')
files_by_adla  = glob.glob(path_files + '/*scoredbyadla.csv')


#%%

interraters = []
# Reading given csv file and creating dataframe
for i in range(len(files_by_adla)):
    
    # Loading data  of scorer 1
    df1 = pd.read_csv(files_by_krishan[i])
    
    
    # Loading data  of scorer 2
    df2 = pd.read_csv(files_by_adla[i])  
    
    
    # Finding common time stamps between the two dataframes
    
    
    # Finding common time stamps between the two dataframes
    ind0 = df2['W'].isin(df1['W']) & df1['W'].isin(df2['W'])
    ind0.value_counts()
    interrater = df1[ind0]['W'] == df2[ind0]['W']
    interraters.append(interrater)
    print(interrater.value_counts())

#%%
# Looking at epochs that were a mismatch
#df1[ind0][boolean_mask_column2 == False] # for df1
#df2[ind0][boolean_mask_column2 == False] # for df2

true_epochs = []
for i in range(len(interraters)):
    
    true_epochs.append(sum(interraters[i])/interraters[i].count())
    
    
interrater_score = np.mean(true_epochs) * 100
    


