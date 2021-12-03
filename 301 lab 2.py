# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 08:41:17 2021

@author: RANA
"""

# 301 lab 2
# exercise 1

import numpy.random as rand 

# question 1

primes = [2,3,5,7,11,13,17,19,23,29]
for value in primes:
    print(value)
    
# question 2
for i in range(5):
    print(primes[i])

# question 3
x = 10
for i in primes:
    print(i + x)

# question 4
primes_sum = primes[0]
for i in range(len(primes)-1):
    primes_sum = primes_sum + primes[i+1]
    print(primes_sum)
    
#question 5
import numpy as np
new_list = np.array([2,3,5,7,11,13,17,19,23,29])
primes_sum = 0
for i in new_list:
    primes_sum = primes_sum + i
    print(primes_sum)

import numpy as np
primeV = np.array(primes)
for i in range(len(primes)):
    for i in range(len(primeV)-1):
        val1 = primeV[i] + primeV[i+1]
        print(val1)
        
# exercise 2

ex2 = []
minV = 1
maxV = 6
for i in range(5):
    x = list(range(minV,maxV))
    ex2.append(x)
    minV = minV+5
    maxV = maxV+5
print(ex2) 

# first loop (outer loop) iterates over the rows 
for i in range(len(ex2)):
    # the second loop (inner loop) iterates over the columns
    for j in range(len(ex2[i])):
        print(ex2[i][j]) # print the ith row / jth column


# exercise 3

import math
asym_list = [[math.pi, math.e, math.nan, math.inf], [True, False],['I', 'love', 'Python'], [1,1,2,6,24,120]]

for i in range(len(asym_list)):
    for j in range(len(asym_list[i])):
        print(asym_list[i][j]) 

rm=[]
for i in range(len(asym_list)):
    x = len(asym_list[i])
    rm.append(x)
    print('number of items in a row', rm)
    
# question 2

zlist = []
for i in range(len(asym_list)):
    tempL = []
    for j in range(len(asym_list[i])):
        r = type(asym_list[i][j])
        tempL.append(r)
    zlist.append(tempL)
    print('The data type of {} is {}'.format(asym_list[i][j],r))
    
## Ecercise 4
## Just playing around lalala
