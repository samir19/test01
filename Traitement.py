# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 14:52:41 2021

@author: belbe
"""
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.approximation import dominating_set
import random
import json
import ast
import time

itération=1
Moyen=80
size=250
places = []

while itération<=1:
    c=str(size)+"_"+str(Moyen)+"_"+str(itération)+".txt"
    print(c)
    # open file and read the content in a list
    with open(c, 'r') as filehandle:
        places = [current_place.rstrip() for current_place in filehandle.readlines()]
    print(places)
    energie=[]
    matrice=[]
    j=0
    while j<size:
        energie.append(float(places[j+1]))
        matrice.append(places[size+j+1])
        j=j+1
    print(energie)
    print(matrice)
    nomF1="I_"+c
    nomF2="E_"+c
    fichier1 = open(nomF1, "w")
    fichier2 = open(nomF2, "w")
    
    k=0
    while k<size:
        fichier1.write(matrice[k]+"\n")
        fichier2.write(str(energie[k])+"\n")
        k=k+1
    
    
    fichier1.close()
    fichier2.close()
    itération=itération+1


print("-----------END-----------")

a=[]
p=0
while p<size:
    a.append(matrice[p].split())
    p=p+1
print(a)
print(len(a[1]))

p=0
while p<size:
    k=0
    while  k<size:
        a[p][k]=int(a[p][k])
        k=k+1
    p=p+1
print(a)
A=[]
A=np.array(a)
G=nx.from_numpy_matrix(A)
nx.draw(G,with_labels=1,node_size=2000,node_color='Yellow')
plt.show()
