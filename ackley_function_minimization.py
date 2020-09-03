# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 14:50:45 2020

@author: Navid
"""

# -*- coding: utf-8 -*-

"""
Created on Thu Apr 5 13:43:08 2020

@author: mehdi
"""
import pandas as pd
from math import pi, cos, sin ,sqrt , e
from random import random
import numpy as np
from numpy.random import uniform as uni
import time
'''define the problem'''
def ackley(x,y):
    return (-20)*(e**(-0.2*sqrt(0.5*(x**2+y**2))))-(e**(0.5*(cos(2*pi*x)+cos(2*pi*y))))+e+20
'''define neighborhood search'''
def neighborpoints(h,k,r):
    j=True
    while j:
         theta = random() * 2 * pi
         if -32.768<h + cos(theta) * r<32.768 and -32.768<k + sin(theta) * r<32.768:
             a,b = h + cos(theta) * r, k + sin(theta) * r
             j=False
    return a,b
'''define local search'''
import sympy as sym
#Calculate gradient of f(x,y)
x,y=sym.symbols('x y')
f=(-20)*(e**(-0.2*sym.sqrt(0.5*(x**2+y**2))))-(e**(0.5*(sym.cos(2*pi*x)+sym.cos(2*pi*y))))+e+20
x_derive=sym.diff(f,x)
y_derive=sym.diff(f,y)
x_derive_val=sym.lambdify((x,y),x_derive)
y_derive_val=sym.lambdify((x,y),y_derive)
'''Description: The functionLocalsearch takes in an initial or previous value for (x,y), 
updates it based on steps taken via the learning rate and outputs the most 
minimum value of (x,y) that reaches the precision satisfaction.
Arguments:
x_new - a starting value of x that will get updated based on the learning rate
y_new - a starting value of y that will get updated based on the learning rate
precision - a precision that determines the stop of the stepwise descent 
alfa - the learning rate (size of each descent step)'''
#defining Local variables
def Localsearch(x_new, y_new, precision=0.0000001, alfa=0.1):
    # change the value of (x,y)
    x_prev = x_new  
    y_prev = y_new  
    # get the derivation of the old value of (x,y)
    d_x = - x_derive_val(x_prev,y_prev)
    d_y = - y_derive_val(x_prev,y_prev)
    ''' get the new value of (x,y) by adding the previous,
    the multiplication of the derivative and the learning rate'''
    x_new = x_prev + (alfa * d_x)
    y_new = y_prev + (alfa * d_y)
    # keep looping until desired precision
    r_step=sqrt((x_new - x_prev)**2+(y_new - y_prev)**2)
    n=1
    #defining number of steps to approach local optima
    NS=1
    # keep looping until your desired precision
    while r_step > precision:
        #n is maximum  number of steps to approach local optima
        if(n<1500):
            x_prev = x_new  
            y_prev = y_new  
            d_x = - x_derive_val(x_prev,y_prev)
            d_y = - y_derive_val(x_prev,y_prev)
            ''' get the new value of (x,y) by adding the previous,
            the multiplication of the derivative and the learning rate'''
            x_new = x_prev + (alfa * d_x)
            y_new = y_prev + (alfa * d_y)
            alfa=alfa * (e**(-n/8))
            r_step=sqrt((x_new - x_prev)**2+(y_new - y_prev)**2)
            NS=NS+1
            n=n+1
        else:
            break
    return x_new, y_new, NS
#Local_x,Local_y,NS=Localsearch(1,0,3)
'''solving with VNS'''
Ackley=[]
X=[]
Y=[]
Time=[]
for j in range(20):
    x,y=uni(-32.768,32.768),uni(-32.768,32.768)   
    start_time = time.time() 
    for i in range(1000):
        for r in (0.1,0.5,3,5,8,13,21,34):
            j=True
            while j:
                a=neighborpoints(x,y,r)
                b=Localsearch(a[0],a[1])
                if ackley(b[0],b[1])<ackley(x,y):
                    x,y=b[0],b[1]
                else:
                    j=False 
    end_time = time.time()                     
    Ackley.append(ackley(x,y))
    X.append(x)
    Y.append(y)
    Time.append(end_time-start_time)
    
AverageResult=pd.DataFrame( index=["Algorithm Precision"],columns=["X","Y","Ackley Value","Time"])
AverageResult.iloc[0,0]=np.mean(X)
AverageResult.iloc[0,1]=np.mean(Y)
AverageResult.iloc[0,2]=np.mean(Ackley)
AverageResult.iloc[0,3]=np.mean(Time)


Result=pd.DataFrame(pd.DataFrame( index=range(20),columns=["X","Y","Ackley Value","Time"]))
for i in range(20):
    Result.iloc[i,0]=X[i]
    Result.iloc[i,1]=Y[i]
    Result.iloc[i,2]=Ackley[i]
    Result.iloc[i,3]=Time[i]
    

Results_report = pd.ExcelWriter("D:\learning sources\COP\PROJECTS\VNS\Results_report.xlsx", engine='xlsxwriter')
Result.to_excel(Results_report, sheet_name='Results')
AverageResult.to_excel(Results_report, sheet_name='AverageResult')   
Results_report.save()
    
        

