# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 14:38:03 2023

@author: WS3
"""


# importing panda library
import pandas as pd
import mne
import glob
import numpy as np
from sklearn.metrics import cohen_kappa_score

path_files = 'C:\Users\WS3\Downloads'


#%%
# Loading dataset containing the scored sleep data
file_by_krishan  = glob.glob(path_files + '/*scoredbykrishan.txt')
file_by_adla  = glob.glob(path_files + '/*scoredbyadla.txt')

#%%
# Reading given csv file and creating dataframe

# Loading data  of scorer 1
dataframe0k = pd.read_csv(file_by_krishan[0])
dataframe0k.drop(dataframe0k.index[dataframe0k[' Annotation'] == ' EEG arousal'], inplace = True)

# Loading data  of scorer 2
dataframe0a = pd.read_csv(file_by_adla[1])  
dataframe0a.drop(dataframe0a.index[dataframe0a[' Annotation'] == ' EEG arousal'], inplace = True)

# Loading dataframe containing time and annotation
df1 = dataframe0k.iloc[:,[1,4]]
df2 = dataframe0a.iloc[:,[1,4]]

# Finding common time stamps between the two dataframes
ind0 = df2[' Time'].isin(df1[' Time']) & df1[' Time'].isin(df2[' Time'])
ind0.value_counts()

# df1[ind0].append(df2[ind0])


boolean_mask_column2 = df1[ind0][' Annotation'] == df2[ind0][' Annotation']

print("Boolean mask for Column2:")
print(boolean_mask_column2)

