# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:39:29 2021

@author: RANA
"""
# STEP 1: install csv and clean data

import pandas as pd 
poro_perm_data = pd.read_csv('poro_perm_data.csv')
poro_perm_data.head()
poro_perm_data.columns # shows column labels as series
#poro_perm_data with negative, zero, and nan (not clean raw data)

#for null values
poro_perm_data.dropna(axis = 0, inplace = True)
poro_perm_data.isnull().sum() #after cleaning Facies null values 

#identify null value by true, and by table
bool1 = poro_perm_data.loc[:,"Facies"].isnull()
null_preveious_rank = poro_perm_data.loc[bool1]
null_preveious_rank

poro_perm_data.describe()
    
