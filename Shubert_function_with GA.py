# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 14:14:21 2020

@author: Navid
"""

from math import sqrt , cos , sin , e , pi
import numpy as np
from numpy.random import uniform as uni
from random import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.set
import pandas as pd
import time
'''defining problem'''
def shubert(x,y):
    temp1 , temp2 = 0 , 0
    for i in range(1,6):
        temp1 += i*cos(((i+1)*x) + i)
    for i in range(1,6):
        temp2 += i*cos(((i+1)*y) + i)
    return temp1*temp2
 


   
''''''''''''''''''''''''''''''''''''''
'''''''''''''''GA'''''''''''''''''''''




'''coding'''  
''' 
x = np.zeros((psize,2),float)
for i in range(psize):
    x[i][0] , x[i][1] = uni(-5,5),uni(-5,5)
'''


'''fitness function'''

def fitness(x,y):
    return 1/(187.7309+shubert(x,y))

'''roulette wheel'''

def wheel(x , psize , parentsize):
    
    global overall_fit,wl_table,parents
    # calculate overall fitness
    
    overall_fit = 0 
    for i in range(psize):
        overall_fit += fitness(x[i][0],x[i][1])
        
    # calculating roulette wheel table
    
    wl_table = np.zeros((psize,4))
    for i in range(psize):
        wl_table[i][0] = i

        wl_table[i][1] = fitness(x[i][0],x[i][1])
        
    wl_table = wl_table[np.argsort(-wl_table[:,1])]
    
    for i in range(psize):

        wl_table[i][2] = wl_table[i][1]/overall_fit
       
        
        if i == 0 :
            wl_table[i][3] = wl_table[i][2]
        else:
            temp = 0 
            for j in range(i+1):
                temp += wl_table[j][2]
            wl_table[i][3] = temp
            
    # selection
    parents =[]
    while len(parents) < parentsize :
        R = uni(0,1)
        for j in range(wl_table.shape[0]):
            if R < wl_table[j][3]  :
                if wl_table[j][0] not in parents :
                    parents.append(int(wl_table[j][0]))
                    break
    parents = x[parents]
                    
    return wl_table , overall_fit , parents
    
'''crossover'''

# uniform crossover

def cross(n_children):
    global children
    children =np.zeros((n_children,2))
    for i in range(n_children):
        _,_,parents = wheel(x,x.shape[0],2)
        for j in range(2):
            R = uni(0,1)
            if R<0.5:
                children[i][j] = parents[0][j]
            else:
                children[i][j] = parents[1][j]
    return children
    
'''mutation'''

# mutation strategy is a random number bigger than 0.8

def mut(n_children_m):
    if n_children_m != 0 :
        global children_m
        children_m = np.zeros((n_children_m ,2))
        for i in range(n_children_m):
             _,_,parents = wheel(x,x.shape[0],1)
             while True:
                 cell = np.random.random_integers(0,1)
                 R = uni(-1,1)
                 children_m[i][cell] = parents[:,cell] + R
                 children_m[i][-(cell -1)] = parents[:,-(cell -1)] 
                 if -10 < parents[:,cell] + R < 10 :
                     break
        return children_m



'''GA Implimentation'''

psize = 50

best=[]             
for iter in range(36):
    print(iter)
    x = np.zeros((psize,2),float)
    for i in range(psize):
        x[i][0] , x[i][1] = uni(-10,10),uni(-10,10)
    
    '''body'''
    
    ans =[]
    
    timeout = time.time() + 240
    while time.time() < timeout :
        R = uni(0,1)
        if R > 0.8:
            n_m = np.random.random_integers(1,10)
            n_c = psize - n_m
            children = cross(n_c)
            children_m = mut(n_m)
            new_pop = np.concatenate((x , children , children_m))
        else:
            n_c = psize
            children = cross(n_c)
            new_pop = np.concatenate((x , children ))
            
        _,_,x = wheel(new_pop , new_pop.shape[0],psize)
        final = []
        for i in range(x.shape[0]):
                final.append(shubert(x[i][0],x[i][1]))
             
        ans.append(np.min(final))
        
    final = []
    for i in range(x.shape[0]):
        final.append(shubert(x[i][0],x[i][1]))
    final = np.concatenate((x,np.array(final).reshape(-1,1)) ,axis=1 )   
    best.append(final[np.argmax(final[:,2]),:])
    
best = pd.DataFrame(best , columns = ['x','y','shubert Value'])
best.to_csv('D:/learning sources/COP/ASSIGNMENTS/ass4/_shubert_GA_Results.csv') 

plt.plot(ans)
plt.xlabel("itteration")
plt.ylabel("SHUBERT VALUE")
plt.show()        
    
    
    
    

    
    
    
    
    