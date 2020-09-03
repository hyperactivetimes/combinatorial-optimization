# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:40:47 2020

@author: Navid
"""

import pandas as pd
from math import pi, cos, sin ,sqrt , e
from random import random
import numpy as np
from numpy.random import uniform as uni
import time
import matplotlib.pyplot as plt
'''Defining Problem'''
def TH(x,y):
    return -abs(sin(x)*cos(y)*(e**abs(1-(sqrt(x**2+y**2)/pi))))
'''defining parameters'''
number_of_particles = 100
stopping_criteria = 1000
r1 = uni(0,1)
r2= uni(0,1)
C1=(0.3,1,3.5)
C2=(0.3,1,3.5)
w=2.5
result = []
steps =[]
step=0# computing steps to optimality
for c1 in C1:
    for c2 in C2:      
        for t in range(10):
            '''defining variable matrixes'''  
            v=np.zeros([number_of_particles, 2], dtype = float) 
            x=np.zeros([number_of_particles, 2], dtype = float) 
            p=np.zeros([number_of_particles, 2], dtype = float) 
            g=np.zeros([1, 2], dtype = float)
            g0=np.zeros([1, 2], dtype = float)            
            temp=np.zeros([1, 2], dtype = float) 
            '''initializing positions'''
            for i in range(number_of_particles):
                p[i]=x[i]=uni(-10,10),uni(-10,10)
            '''initializing global best position'''
            for i in range(number_of_particles):
                if TH(x[i][0],x[i][1]) < TH(g[0][0],g[0][1]):
                    g[0] = x[i]
            '''main body of pso algorithm'''       
            counter=0
            step_counter=list()
            for j in range(1000) :
                g0[0]=g[0]
                for i in range(number_of_particles):
                    v[i] = w*v[i] + c1*r1*(p[i]-x[i]) + c2*r2*(g[0]-x[i])
                    temp = x[i] + v[i]
                    if -10<temp[0]<10 and -10<temp[1]<10 :
                        x[i] = temp
                    if TH(x[i][0],x[i][1]) < TH(p[i][0],p[i][1]):
                        p[i] = x[i] 
                    if TH(x[i][0],x[i][1]) < TH(g[0][0],g[0][1]):
                        g[0] = x[i]
                result.append((c1,c2,TH(g[0][0],g[0][1]),g[0][0],g[0][1])) 
                if (abs(abs(TH(g[0][0],g[0][1])) - abs(TH(g0[0][0],g0[0][1])))) < 0.0001 :
                    counter=counter+1
                if counter > 20:
                    step_counter.append(j-20)
                if abs(TH(g[0][0],g[0][1]) - TH(g0[0][0],g0[0][1])) > 0.0001:
                    counter=0
            steps.append((c1,c2,step_counter[0]))
                
                 

rough_result = pd.DataFrame(result , columns =['c1','c2','table holder value','x1','x2'])
steps_rough = pd.DataFrame(steps , columns =['c1','c2','steps to convergance'])
''' graphing each parameter set for ten times of execution'''
res =[]
plt.figure()
for p in np.arange(0,90000,10000):
    for j in np.arange(p,p+10000,1000):
        for i in range(j-1000 , j):
            res.append(result[i][2])
        plt.plot(res)
        plt.xlabel('time')
        plt.ylabel('table holder function value')
        plt.title('c1 = {} , c2={}'.format(result[p][0],result[p][1]))        
        res =[]
    plt.savefig('D:\learning sources\COP\PROJECTS\PSO\c1_{}_c2_{}.png'.format(result[p][0],result[p][1]))    
    plt.show()
'''extracting the result achieved for each parameter set'''      
res =[]
out = []
for p in np.arange(0,90000,10000):
    for j in np.arange(p,p+10000,10000):
        for i in range(j-10000 , j):
            res.append(result[i][2])
        out.append((result[p][0],result[p][1],min(res),result[res.index(min(res))][3],result[res.index(min(res))][4]))
best_result = pd.DataFrame(out,columns =['c1','c2','table holder value','x1','x2'])                 
'''extracting the mean of steps needed for convergance for each parameter set'''
res =[]
mean_step = []
for p in np.arange(0,90,10):
        for i in range(p , p+10):
            res.append(steps[i][2])
        mean_step.append((steps[i][0],steps[i][1],np.mean(res)))
mean_step = pd.DataFrame(mean_step,columns =['c1','c2','mean_steps_to_convergance'])                 
'''saving the result into an excel file'''
Results_report = pd.ExcelWriter("D:\learning sources\COP\PROJECTS\PSO\Results_report.xlsx", engine='xlsxwriter')
best_result.to_excel(Results_report, sheet_name='Best_Results')
rough_result.to_excel(Results_report, sheet_name='Rough_Results')
steps_rough.to_excel(Results_report, sheet_name='steps_to_convergance')
mean_step.to_excel(Results_report, sheet_name='steps_to_convergance')
Results_report.save()
'''plotting the best result'''                
import seaborn as sns     
label = []
for i in range(9):
    j=0
    label.append('c1={},c2={}'.format(best_result.iloc[i,j],best_result.iloc[i,j+1]))
plt.figure()       
sns.barplot(label,best_result['table holder value'])                  
plt.xticks(rotation = 90)
plt.title('best result for each parameter set') 
plt.savefig('D:\learning sources\COP\PROJECTS\PSO\plot.png')      
plt.show()     
'''plotting mean_step to convergance'''
label = []
for i in range(9):
    j=0
    label.append('c1={},c2={}'.format(mean_step.iloc[i,j],mean_step.iloc[i,j+1]))
plt.figure()       
sns.barplot(label,mean_step['mean_steps_to_convergance'])                  
plt.xticks(rotation = 90) 
plt.title('steps needed for convergance in each parameter set')
plt.savefig('D:\learning sources\COP\PROJECTS\PSO\steps_plot.png')      
plt.show()     