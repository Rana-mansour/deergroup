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

import matplotlib.pyplot as plt
fig1 = poro_perm_data.plot(x='Depth (ft)', y='Porosity (%)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'porosity(%)', color='black', title= 'Depth Vs. Porosity')
plt.legend(['Depth (ft)','Porosity (%)'])
fig2 = poro_perm_data.plot(x='Depth (ft)', y='Permeability (mD)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'permeability (mD)', color='black', title= 'Depth Vs. Permeability')
plt.legend(['Depth (ft)','Permeability (mD)'])

#identify null value by true, and by table
bool1 = poro_perm_data.loc[:,"Facies"].isnull()
null_preveious_rank = poro_perm_data.loc[bool1]
null_preveious_rank

poro_perm_data.describe()

import itertools
wrong_values_prosity = 0  # counter for wrong values in prosity
wrong_values_permeability = 0 # counter for wrong values in permeability
wrong_values_facies = 0  # counter for wrong values in facies
peorosity = []
permability = []
depth = []
Facies = []

aa = []
for i in reader:
    
    i[1] = float(i[1])
    i[2] = float(i[2])
    
        
    if i[1]<0 :
        i[1] = "incorrect value"
        wrong_values_prosity+=1
    if i[1] != str(i[1]):
        peorosity.append(i[1])
    if i[1] != "incorrect value":
        depth.append(float(i[0]))    
        
    if i[2]<=0 :
        i[2] = "incorrect value"
        wrong_values_permeability+=1
    if i[2] != str(i[2]):
        permability.append(i[2])    
    i[0] = float(i[0])
    if i[3] == 'nan':
        i[3] = "incorrect facies"
        wrong_values_facies+=1
    
print('-------------------------')  
print("total wrong values in prosity :   ",wrong_values_prosity)
print("total wrong values in permeability  :   ",wrong_values_permeability)
print("total wrong values in facies  :   ",wrong_values_facies)
