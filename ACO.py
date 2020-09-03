#Ant Colony Algorithm
import numpy as np
import random
#Defining parameters & variables
CD1=(1,1,0,0,1,0,0,0)
CD2=(0,0,1,0,0,0,1,1)
CD3=(0,0,1,1,1,0,1,0)
CD4=(1,0,0,0,0,1,0,1)
CD5=(0,0,0,1,1,1,1,1)
nodes=['start',CD1,CD2,CD3,CD4,CD5]
indx={CD1:"CD1",CD2:"CD2",CD3:"CD3",CD4:"CD4",CD5:"CD5"}
costs=(1,18,23,32,28,38) #The first element(1) is redundant and doesn't affect the answer
Cnn=101 #Cnn is shortest neighborhood answer length
alfa,P,beta,m=1,0.2,2,8
nu=[1/i for i in costs]
pheromone=np.zeros([len(nodes),len(nodes)],dtype = float)
#Union function
def union (a,b):
    UniAns=list()
    for i in range (len(a)):
        UniAns.append(a[i]+b[i])
        if UniAns[i]==2:
            UniAns[i]=1
    return UniAns
#Destination node function
def destinate(remnant_nodes,origin):
    destinations=list()
    #path probabilities
    path_probability=np.zeros([len(nodes),len(nodes)],dtype = float)
    for destination in remnant_nodes:
        destinations.append(nodes.index(destination))
    for destination in destinations:
        path_probability[origin][destination]=((pheromone[origin][destination]**alfa)*(nu[destination]**beta))/(sum((pheromone[origin][destination]**alfa)*(nu[destination]**beta) for destination in destinations))  
    #selecting destination node
    cumulative=0
    r=random.uniform(0,1)
    for destination in destinations:
        cumulative+=path_probability[origin][destination]
        d=r-cumulative
        if(d<0):
            new_destination=nodes[destination]
            break
    return new_destination
#ACO
for P in [0.05,0.1,0.2]:
    for beta in [1,2,3]:
        for alfa in [0.5,1,1.5]:
            counter=0
            #initial pheromone generation
            for origin in range (len(nodes)):
                for destination in range (len(nodes)):
                    pheromone[origin][destination]=m/Cnn
            Cost=[i for i in range (8)] #arbitrary
            iterate=0
            while(not(Cost[0]==Cost[1]==Cost[2]==Cost[3]==Cost[4]==Cost[5]==Cost[6]==Cost[7])):
                Colony=list()
                Cost=list()
                for ant in range (m):
                    ans=np.zeros(8)
                    path=list()
                    origin=nodes.index('start')
                    remnant_nodes=['start',CD1,CD2,CD3,CD4,CD5]
                    while sum(ans)!=len(CD1):
                        remnant_nodes.remove(nodes[origin])
                        destination=destinate(remnant_nodes,origin)
                        ans=union(ans,destination)
                        path.append(destination)
                        origin=nodes.index(destination)
                    #Calculating answer cost
                    cost=sum(costs[nodes.index(i)] for i in path)
                    Colony.append(path)
                    Cost.append(cost)
                #Updating pheromones
                for origin in range (len(nodes)):
                    for destination in range (len(nodes)):
                        pheromone[origin][destination]=(1-P)*pheromone[origin][destination]
                for path in Colony:
                    for i in range(len(path)-1):
                        pheromone[nodes.index(path[i])][nodes.index(path[i+1])]=pheromone[nodes.index(path[i])][nodes.index(path[i+1])]+(1/Cost[Colony.index(path)])
                iterate+=1
                counter+=1
                if counter>5000:
                    break
            Answer=list()
            for i in path:
                Answer.append(indx[i])
            print('alfa={},beta={},P={},number of iterations={},objective function={},CDs={}'.format(alfa,beta,P,iterate,min(Cost),Answer))


number of ants=8

alfa=0.5,beta=1,P=0.05,number of iterations=5001,objective function=79,CDs=['CD1', 'CD2', 'CD4', 'CD3']
alfa=1,beta=1,P=0.05,number of iterations=503,objective function=79,CDs=['CD2', 'CD5', 'CD1']
alfa=1.5,beta=1,P=0.05,number of iterations=81,objective function=78,CDs=['CD1', 'CD4', 'CD3']
alfa=0.5,beta=2,P=0.05,number of iterations=1495,objective function=101,CDs=['CD1', 'CD2', 'CD4', 'CD3']
alfa=1,beta=2,P=0.05,number of iterations=343,objective function=101,CDs=['CD2', 'CD4', 'CD3', 'CD1']
alfa=1.5,beta=2,P=0.05,number of iterations=190,objective function=78,CDs=['CD4', 'CD1', 'CD3']
alfa=0.5,beta=3,P=0.05,number of iterations=151,objective function=101,CDs=['CD2', 'CD3', 'CD1', 'CD4']
alfa=1,beta=3,P=0.05,number of iterations=76,objective function=101,CDs=['CD1', 'CD2', 'CD4', 'CD3']
alfa=1.5,beta=3,P=0.05,number of iterations=31,objective function=101,CDs=['CD1', 'CD2', 'CD4', 'CD3']
alfa=0.5,beta=1,P=0.1,number of iterations=5001,objective function=79,CDs=['CD2', 'CD5', 'CD3', 'CD1']
alfa=1,beta=1,P=0.1,number of iterations=112,objective function=79,CDs=['CD1', 'CD2', 'CD5']
alfa=1.5,beta=1,P=0.1,number of iterations=83,objective function=78,CDs=['CD1', 'CD3', 'CD4']
alfa=0.5,beta=2,P=0.1,number of iterations=155,objective function=101,CDs=['CD1', 'CD2', 'CD3', 'CD4']
alfa=1,beta=2,P=0.1,number of iterations=101,objective function=101,CDs=['CD4', 'CD2', 'CD3', 'CD1']
alfa=1.5,beta=2,P=0.1,number of iterations=120,objective function=78,CDs=['CD3', 'CD4', 'CD1']
alfa=0.5,beta=3,P=0.1,number of iterations=493,objective function=101,CDs=['CD2', 'CD4', 'CD1', 'CD3']
alfa=1,beta=3,P=0.1,number of iterations=70,objective function=101,CDs=['CD2', 'CD4', 'CD1', 'CD3']
alfa=1.5,beta=3,P=0.1,number of iterations=86,objective function=78,CDs=['CD4', 'CD3', 'CD1']
alfa=0.5,beta=1,P=0.2,number of iterations=5001,objective function=78,CDs=['CD5', 'CD1', 'CD3']
alfa=1,beta=1,P=0.2,number of iterations=108,objective function=78,CDs=['CD3', 'CD1', 'CD4']
alfa=1.5,beta=1,P=0.2,number of iterations=47,objective function=78,CDs=['CD1', 'CD4', 'CD3']
alfa=0.5,beta=2,P=0.2,number of iterations=918,objective function=101,CDs=['CD1', 'CD3', 'CD2', 'CD4']
alfa=1,beta=2,P=0.2,number of iterations=100,objective function=101,CDs=['CD1', 'CD2', 'CD4', 'CD3']
alfa=1.5,beta=2,P=0.2,number of iterations=87,objective function=78,CDs=['CD1', 'CD3', 'CD4']
alfa=0.5,beta=3,P=0.2,number of iterations=98,objective function=101,CDs=['CD1', 'CD2', 'CD3', 'CD4']
alfa=1,beta=3,P=0.2,number of iterations=40,objective function=101,CDs=['CD2', 'CD1', 'CD4', 'CD3']
alfa=1.5,beta=3,P=0.2,number of iterations=20,objective function=101,CDs=['CD1', 'CD2', 'CD3', 'CD4']


number of ants=12

alfa=0.5,beta=1,P=0.05,number of iterations=5001,objective function=78,CDs=['CD4', 'CD3', 'CD5', 'CD1']
alfa=1,beta=1,P=0.05,number of iterations=350,objective function=78,CDs=['CD4', 'CD3', 'CD1']
alfa=1.5,beta=1,P=0.05,number of iterations=292,objective function=78,CDs=['CD3', 'CD1', 'CD4']
alfa=0.5,beta=2,P=0.05,number of iterations=5001,objective function=78,CDs=['CD3', 'CD1', 'CD2', 'CD4']
alfa=1,beta=2,P=0.05,number of iterations=419,objective function=101,CDs=['CD1', 'CD2', 'CD3', 'CD4']
alfa=1.5,beta=2,P=0.05,number of iterations=122,objective function=101,CDs=['CD2', 'CD4', 'CD3', 'CD1']
alfa=0.5,beta=3,P=0.05,number of iterations=1244,objective function=101,CDs=['CD2', 'CD1', 'CD3', 'CD4']
alfa=1,beta=3,P=0.05,number of iterations=83,objective function=101,CDs=['CD1', 'CD2', 'CD3', 'CD4']
alfa=1.5,beta=3,P=0.05,number of iterations=58,objective function=101,CDs=['CD1', 'CD2', 'CD4', 'CD3']
alfa=0.5,beta=1,P=0.1,number of iterations=5001,objective function=78,CDs=['CD4', 'CD1', 'CD2', 'CD3']
alfa=1,beta=1,P=0.1,number of iterations=505,objective function=79,CDs=['CD1', 'CD2', 'CD5']
alfa=1.5,beta=1,P=0.1,number of iterations=380,objective function=79,CDs=['CD1', 'CD2', 'CD5']
alfa=0.5,beta=2,P=0.1,number of iterations=5001,objective function=78,CDs=['CD2', 'CD1', 'CD5']
alfa=1,beta=2,P=0.1,number of iterations=332,objective function=101,CDs=['CD1', 'CD2', 'CD4', 'CD3']
alfa=1.5,beta=2,P=0.1,number of iterations=65,objective function=101,CDs=['CD4', 'CD1', 'CD2', 'CD3']
alfa=0.5,beta=3,P=0.1,number of iterations=1096,objective function=101,CDs=['CD2', 'CD4', 'CD1', 'CD3']
alfa=1,beta=3,P=0.1,number of iterations=118,objective function=101,CDs=['CD1', 'CD4', 'CD2', 'CD3']
alfa=1.5,beta=3,P=0.1,number of iterations=269,objective function=78,CDs=['CD4', 'CD3', 'CD1']
alfa=0.5,beta=1,P=0.2,number of iterations=5001,objective function=79,CDs=['CD4', 'CD1', 'CD5', 'CD2']
alfa=1,beta=1,P=0.2,number of iterations=432,objective function=78,CDs=['CD3', 'CD4', 'CD1']
alfa=1.5,beta=1,P=0.2,number of iterations=383,objective function=79,CDs=['CD1', 'CD2', 'CD5']
alfa=0.5,beta=2,P=0.2,number of iterations=5001,objective function=78,CDs=['CD3', 'CD1', 'CD4']
alfa=1,beta=2,P=0.2,number of iterations=550,objective function=101,CDs=['CD2', 'CD4', 'CD1', 'CD3']
alfa=1.5,beta=2,P=0.2,number of iterations=81,objective function=78,CDs=['CD1', 'CD4', 'CD3']
alfa=0.5,beta=3,P=0.2,number of iterations=40,objective function=101,CDs=['CD1', 'CD4', 'CD2', 'CD3']
alfa=1,beta=3,P=0.2,number of iterations=69,objective function=101,CDs=['CD2', 'CD4', 'CD1', 'CD3']
alfa=1.5,beta=3,P=0.2,number of iterations=16,objective function=101,CDs=['CD1', 'CD2', 'CD4', 'CD3']

number of ants=16

alfa=0.5,beta=1,P=0.05,number of iterations=5001,objective function=78,CDs=['CD2', 'CD5', 'CD1']
alfa=1,beta=1,P=0.05,number of iterations=4532,objective function=79,CDs=['CD2', 'CD5', 'CD1']
alfa=1.5,beta=1,P=0.05,number of iterations=473,objective function=79,CDs=['CD1', 'CD2', 'CD5']
alfa=0.5,beta=2,P=0.05,number of iterations=5001,objective function=78,CDs=['CD1', 'CD4', 'CD3']
alfa=1,beta=2,P=0.05,number of iterations=869,objective function=101,CDs=['CD1', 'CD2', 'CD4', 'CD3']
alfa=1.5,beta=2,P=0.05,number of iterations=318,objective function=78,CDs=['CD1', 'CD4', 'CD3']
alfa=0.5,beta=3,P=0.05,number of iterations=5001,objective function=78,CDs=['CD1', 'CD2', 'CD4', 'CD5']
alfa=1,beta=3,P=0.05,number of iterations=68,objective function=101,CDs=['CD2', 'CD1', 'CD4', 'CD3']
alfa=1.5,beta=3,P=0.05,number of iterations=26,objective function=101,CDs=['CD2', 'CD1', 'CD4', 'CD3']
alfa=0.5,beta=1,P=0.1,number of iterations=5001,objective function=78,CDs=['CD1', 'CD2', 'CD4', 'CD3']
alfa=1,beta=1,P=0.1,number of iterations=2220,objective function=79,CDs=['CD1', 'CD2', 'CD5']
alfa=1.5,beta=1,P=0.1,number of iterations=1096,objective function=78,CDs=['CD3', 'CD1', 'CD4']
alfa=0.5,beta=2,P=0.1,number of iterations=5001,objective function=79,CDs=['CD5', 'CD2', 'CD1']
alfa=1,beta=2,P=0.1,number of iterations=893,objective function=101,CDs=['CD1', 'CD2', 'CD4', 'CD3']
alfa=1.5,beta=2,P=0.1,number of iterations=92,objective function=79,CDs=['CD1', 'CD2', 'CD5']
alfa=0.5,beta=3,P=0.1,number of iterations=5001,objective function=78,CDs=['CD1', 'CD2', 'CD5']
alfa=1,beta=3,P=0.1,number of iterations=177,objective function=101,CDs=['CD2', 'CD4', 'CD1', 'CD3']
alfa=1.5,beta=3,P=0.1,number of iterations=45,objective function=101,CDs=['CD1', 'CD2', 'CD4', 'CD3']
alfa=0.5,beta=1,P=0.2,number of iterations=5001,objective function=78,CDs=['CD4', 'CD1', 'CD3']
alfa=1,beta=1,P=0.2,number of iterations=1893,objective function=101,CDs=['CD1', 'CD2', 'CD4', 'CD3']
alfa=1.5,beta=1,P=0.2,number of iterations=529,objective function=79,CDs=['CD2', 'CD1', 'CD5']
alfa=0.5,beta=2,P=0.2,number of iterations=5001,objective function=78,CDs=['CD5', 'CD1', 'CD3']
alfa=1,beta=2,P=0.2,number of iterations=3304,objective function=78,CDs=['CD1', 'CD3', 'CD4']
alfa=1.5,beta=2,P=0.2,number of iterations=540,objective function=78,CDs=['CD3', 'CD1', 'CD4']
alfa=0.5,beta=3,P=0.2,number of iterations=1148,objective function=101,CDs=['CD2', 'CD4', 'CD1', 'CD3']
alfa=1,beta=3,P=0.2,number of iterations=90,objective function=101,CDs=['CD4', 'CD1', 'CD2', 'CD3']
alfa=1.5,beta=3,P=0.2,number of iterations=221,objective function=78,CDs=['CD1', 'CD4', 'CD3']
