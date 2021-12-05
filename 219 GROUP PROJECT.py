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

import numpy as np
d = poro_perm_data.replace(0, np.nan)
d = poro_perm_data.dropna(how = 'all', axis = 0)
d = poro_perm_data.replace(np.nan, 0)

#deletes all the values below zero in porosity csv file
poro_perm_data = poro_perm_data[poro_perm_data['Porosity (%)'] > 0]

#deletes all the values below zero in permeability csv file
poro_perm_data = poro_perm_data[poro_perm_data['Permeability (mD)'] > 0]
#now the data is clean from nan, negative, and zero values: check:
poro_perm_data.describe()
#to check for each facies again:

bool_las = poro_perm_data.loc[:,"Facies"] == "'overbanks'"
newOdata= poro_perm_data[bool_las]
newOdata.describe()

bool_las2 = poro_perm_data.loc[:,"Facies"] == "'crevasse splay'"
newCdata= poro_perm_data[bool_las2]
newCdata.describe()

bool_las3 = poro_perm_data.loc[:,"Facies"] == "'channel'"
newCHdata= poro_perm_data[bool_las3]
newCHdata.describe()
#now min and max of each facies is identified

#plots for channel 
fig3 = poro_perm_data.plot(x='Depth (ft)', y='Porosity (%)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'porosity(%)', color='black', title= 'Channel facies porosity graph')
plt.legend(['Depth (ft)','Porosity (%)'])

fig4 = poro_perm_data.plot(x='Depth (ft)', y='Permeability (mD)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'Permeability (mD)', color='black', title= 'Channel facies permeability graph')
plt.legend(['Depth (ft)','Permeability (mD)'])

#plots for crevasse splay 
fig5 = poro_perm_data.plot(x='Depth (ft)', y='Porosity (%)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'porosity(%)', color='black', title= 'crevasse splay facies porosity graph')
plt.legend(['Depth (ft)','Porosity (%)'])

fig6 = poro_perm_data.plot(x='Depth (ft)', y='Permeability (mD)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'Permeability (mD)', color='black', title= 'crevasse splay facies permeability graph')
plt.legend(['Depth (ft)','Permeability (mD)'])

#plots for overbanks
fig7 = poro_perm_data.plot(x='Depth (ft)', y='Porosity (%)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'porosity(%)', color='black', title= 'overbanks facies porosity graph')
plt.legend(['Depth (ft)','Porosity (%)'])

fig8 = poro_perm_data.plot(x='Depth (ft)', y='Permeability (mD)',kind = 'scatter',xlabel = 'Depth (ft)', ylabel = 'Permeability (mD)', color='black', title= 'overbanks facies permeability graph')
plt.legend(['Depth (ft)','Permeability (mD)'])

#STEP 2: install las and clean data
f = open('1051661071.las', 'r') # 'r' = read
lines = f.read()

#f and lines are the las file
las = lasio.read('1051661071.las')
df = las.df()
summary = df.describe()
df.isnull().sum()

df = df.reset_index()
df = df.rename(columns = {'DEPT' : 'DEPTH'})

# 100000, negative values are deleted from the data
import numpy as np
df = df.replace(0, np.nan)
df = df.dropna(how = 'all', axis = 0)
df = df.replace(np.nan, 0)
df = df.drop(columns = 'AVTX')
df = df.drop(columns = 'BVTX')
df = df.drop(columns = 'LSPD')
df = df.drop(columns = 'SP')

df = df[df['CILD'] > 0]
df = df[df['CNDL'] > 0]
df = df[df['CNLS'] > 0]
df = df[df['CNPOR'] > 0]
df = df[df['CNSS'] > 0]
df = df[df['GR'] > 0]
df = df[df['LTEN'] > 0]
df = df[df['RILD'] != 100000]
df = df[df['RILM'] > 0]
df = df[df['RLL3'] > 0]
df = df[df['RXORT'] > 0]
df = df[df['MCAL'] > 0]
df = df[df['MI'] > 0]
df = df[df['MN'] > 0]
df = df[df['DCAL'] > 0]
df = df[df['RHOB'] > 0]
df = df[df['RHOC'] > 0]
df = df[df['DPOR'] > 0]

summary2 = df.describe()

#to check original file
df1= las.df()

#plots for las file (logs):
#Deep resistivity (RILD)
fig9 = df.plot(x='RILD', y='DEPTH', c='blue', lw=0.5, legend=False, figsize=(7,10))
plt.ylim(300, 5000)
plt.xlim(0,400)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, labeltop=True)
plt.ylabel("Depth (ft)")
plt.title('RILD')
fig9.set_xlabel("RILD (ohm.m)")
fig9.xaxis.set_label_position('top') 
plt.show()

#shallow Resistivity (RLL3)
fig10 = df.plot(x='RLL3', y='DEPTH', c='red', lw=0.5, legend=False, figsize=(7,10))
plt.ylim(300, 5000)
plt.xlim(0,300)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, labeltop=True)
plt.ylabel("Depth (ft)")
plt.title('RLL3')
fig10.set_xlabel("RLL3 (ohm.m)")
fig10.xaxis.set_label_position('top') 
plt.show()

#Medium Resistivity (RILM)
fig11 = df.plot(x='RILM', y='DEPTH', c='green', lw=0.5, legend=False, figsize=(7,10))
plt.ylim(300, 5000)
plt.xlim(0,400)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, labeltop=True)
plt.ylabel("Depth (ft)")
plt.title('RILM')
fig11.set_xlabel("RILM (ohm.m)")
fig11.xaxis.set_label_position('top') 
plt.show()

#logs all together
ax = df.plot(x='RILD', y='DEPTH', c='blue', lw=0.5, legend=False, figsize=(7,10))
ax = df.plot(x='RLL3', y='DEPTH', c='red', lw=0.5, legend=False, figsize=(7,10),ax=ax)
ax = df.plot(x='RILM', y='DEPTH', c='green', lw=0.5, legend=False, figsize=(7,10), ax=ax)
plt.ylim(300, 5000)
plt.xlim(0,400)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, labeltop=True)
plt.ylabel("Depth (ft)")
plt.title('RILM, RILD, RLL3')
ax.set_xlabel("RILM, RILD, RLL3 (ohm.m)")
ax.xaxis.set_label_position('top') 
plt.show()

#gamma ray log
fig13=df.plot(x='GR',y='DEPTH', c='black', lw=0.5, legend= False, figsize=(7,10))
plt.ylim(300, 5000)
plt.xlim(0,1)
plt.tick_params(axis='both', which='major')
plt.ylabel("Depth (ft)")
plt.title('GR')
fig11.set_xlabel("Gr (GAPI)")
logi=df["GR"]<50
f =logi.sum()
z=0.5*0.3048
thickness=z*f
print(thickness)
#thickness is 14.6304

#gamma ray for a potential reservoir should be low, so generally any values larger than 100 for example wont be important to delete from the data frame since they are already bad reservoirs. (low GR is wanted) 

#gamma ray color map
# Plot of Gamma ray adapted with a color map fill
left_col_value = 24.5
right_col_value =183.8
# assign the column to a variable for easier reading
curve = df['GR']
# calculate the span of values
span = abs(left_col_value - right_col_value)
# assign a color map
cmap = plt.get_cmap('viridis')
# create array of values to divide up the area under curve
color_index = np.arange(left_col_value, right_col_value, span / 100)
# setup the plot
ax = df.plot(x='GR', y='DEPTH', c='black', lw=0.5, legend=False, figsize=(7,10))
plt.ylim(4456, 228.5)
plt.xlim(12.8,203)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, labeltop=True)
plt.ylabel("Depth (ft)")
plt.title('Gamma Ray')
ax.set_xlabel("GR")
ax.xaxis.set_label_position('top')
for index in sorted(color_index):
    index_value = (index - left_col_value)/span
    color = cmap(index_value) #obtain colour for color index value
    plt.fill_betweenx(df['DEPTH'], 400 , curve, where = curve >= index,  color = color)
plt.show()

#RHOB log
# assign the column to a variable for easier reading
curve = df['RHOB']
left_col_value = 1
right_col_value = 3
# calculate the span of values
span = abs(left_col_value - right_col_value)
#assign a color map
cmap = plt.get_cmap('PuBuGn')
#create array of values to divide up the area under curve
color_index = np.arange(left_col_value, right_col_value, span / 100)
#setup the plot
fig12 = df.plot(x='RHOB', y='DEPTH', c='black', lw=0.5, legend=False, figsize=(7,10))
plt.ylim(300, 5000)
plt.xlim(1,3)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom = False, bottom=False, top = False, labeltop=True)
plt.ylabel("Depth (ft)")
plt.title('Bulk density log')
fig12.set_xlabel("RHOB g/cc")
fig12.xaxis.set_label_position('top') 
#loop through each value in the color_index
for index in sorted(color_index):
    index_value = (index - left_col_value)/span
    color = cmap(index_value) #obtain colour for color index value
    plt.fill_betweenx(df['DEPTH'], 400 , curve, where = curve >= index,  color = color)
plt.show()

#Clustring: 
RHOB = df['RHOB']
RHOB = RHOB.to_numpy()
CNPOR = df['CNPOR']
CNPOR = CNPOR.to_numpy()

fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.scatter(CNPOR, RHOB,edgecolors = 'k')
plt.xlabel("Porosity (%)")
plt.ylabel("Bulk density (g/cm^3)")
plt.show()

#------------------------------------
#Histograms
#porosity
poro_perm_data['Porosity (%)'].hist()
plt.ylabel('Porosity (%)')
plt.legend(["Porosity"])
ax=poro_perm_data['Porosity (%)'].plot(kind='hist', title= 'Porosity distribution')

#permeability 
poro_perm_data['Permeability (mD)'].hist()
plt.ylabel('Permeability (mD)')
plt.legend(["Porosity"])
plt.legend(["Permeability"])
ax=poro_perm_data['Permeability (mD)'].plot(kind='hist', title= 'Permeability distribution')
#------------------------------------
# Density and porosity did not know how to find neutron density
figg = plt.subplots(figsize=(7,10))

ax1 = plt.subplot2grid((1,1), (0,0), rowspan=1, colspan=1)
ax2 = ax1.twiny()

ax1.plot('RHOB', 'DEPTH', data=df, color='red', lw=0.5)
ax1.set_xlim(1, 3)
ax1.set_xlabel('Density')
ax1.xaxis.label.set_color("red")
ax1.tick_params(axis='x', colors="red")
ax1.spines["top"].set_edgecolor("red")

ax2.plot('CNPOR', 'DEPTH', data=df, color='blue', lw=0.5)
ax2.set_xlim(0, 50)
ax2.set_xlabel('Porosity (%)')
ax2.xaxis.label.set_color("blue")
ax2.spines["top"].set_position(("axes", 1.08))
ax2.tick_params(axis='x', colors="blue")
ax2.spines["top"].set_edgecolor("blue")

x1=df['RHOB']
x2=df['CNPOR']

x = np.array(ax1.get_xlim())
z = np.array(ax2.get_xlim())

nz=((x2-np.max(z))/(np.min(z)-np.max(z)))*(np.max(x)-np.min(x))+np.min(x)

ax1.fill_betweenx(df['DEPTH'], x1, nz, where=x1>=nz, interpolate=True, color='green')
ax1.fill_betweenx(df['DEPTH'], x1, nz, where=x1<=nz, interpolate=True, color='yellow')

for ax in [ax1, ax2]:
    ax.set_ylim(400, 5000)
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")
