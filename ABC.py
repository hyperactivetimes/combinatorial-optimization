# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:01:31 2020

@author: Navid
"""
#set covering problem solved by artificial bee colony algorithm

import numpy as np
import random
#Define the sets
A=set(['a','b','c','d','e','f','g'])
A1=set(['a','b','f','g'])
A2=set(['a','b','g'])
A3=set(['a','b','c'])
A4=set(['e','f','g'])
A5=set(['f','g'])
A6=set(['d','f'])
A7=set(['d'])
sets=[A1,A2,A3,A4,A5,A6,A7]
Ans={0:"A1",1:"A2",2:"A3",3:"A4",4:"A5",5:"A6",6:"A7"}
#Define costs
C1=[1,1,1,1,1,1,1]
C2=[2,2,3,3,2,3,1]
#Cost functions:
def cost(v,C):
    c=0
    for i in (v):
        c=c+C[i]
    return c
#Unique list
def unique(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
#Initial answer generation
def initial_ans(N):
    init_ans=list()
    for i in range(N):
        f=list()
        F=set([])
        while(F!=A):
            s=random.choice(sets)
            f.append(sets.index(s))
            F=F.union(s)
        init_ans.append(unique(f))
    return  init_ans
#Define local search
#O is the number of Onlooker bees
#f is index set of an answer
def local_search(l,onlook,C):
    if (onlook<1):
        return l,cost(l,C)
    else:
        l_past=l
        F=set([])
        for i in range(onlook):
            while (F!=A):
                ans=l
                F=set([])
                Candidate=random.choice(ans)
                ans[ans.index(Candidate)]=sets.index(random.choice(sets))
                ans=unique(ans)
                for k in (ans):
                    F=F.union(sets[k])
            l=ans
            l_new=l
            if (cost(l_new,C1)>cost(l_past,C1)):
                l=l_past
                c=cost(l_past,C)
            else:
                l=l_new
                l_past=l_new
                c=cost(l_new,C)
        return l,c
#Onlooker Selection Function
def Onlookers (N_Onlook,index_AnsSet,C):   
    fit=list()
    P=list()
    #Fitness Function
    for i in range(len(index_AnsSet)):
        fit.append(1/(1+cost(index_AnsSet[i],C)))
    #Probability Function
    for j in range(len(index_AnsSet)):
        P.append(fit[j]/sum(fit))
    #Onlooker Selection
    onlook=[]
    for v in range(len(P)):
        onlook.append(0)
    for k in range(N_Onlook):
        cumulative=0
        r=random.uniform(0,1)
        for i in range (len(P)):
            cumulative=cumulative+P[i]
            d=r-cumulative
            if(d<0):
                onlook[i]+=1
                break
    return onlook
N_Colony=100
N_Onlook=50
N_Worker=N_Colony-N_Onlook
C=C2
c=list()
onlook=list()
d=list()
diff=list()
init_answers=initial_ans(N_Worker)
local_ans=init_answers
for i in range(len(init_answers)):
    c.append(cost(init_answers[i],C))
    onlook.append(1)
    d.append(0)
for iteration in range (1000):
    c_p=c
    for i in range(len(init_answers)):
        local_ans[i],c[i]=local_search(local_ans[i],onlook[i],C)
    c_best_answer= min(c)
    best_answer=local_ans[c.index(min(c))]
    for j in range(len(init_answers)):
        d[j]=c[j]-c_p[j]
    diff.append(d)
    if(iteration>10):
        for v in range(len(init_answers)):
            D=0
            for k in range(10):
                D+=diff[-1-k][v]
            if(D==0):
                if(c[v]<c_best_answer):
                    c_best_answer=c[v]
                    best_answer=local_ans[v]
                local_ans[v]=initial_ans(1)[0]
    onlook=Onlookers(N_Onlook,local_ans,C)
Answer=list()
for i in best_answer:
    Answer.append(Ans[i])
print("The best answer with C=C2 is",Answer,"and the objective function is equal to",c_best_answer)

'''
The best answer with C=C1 is ['A7', 'A3', 'A4'] and the objective function is equal to 3

The best answer with C=C2 is ['A4', 'A3', 'A7'] and the objective function is equal to 7
'''


