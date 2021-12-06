# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:09:24 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
i=[]
j=[]
k=[]
l=[]

rangee=np.linspace(0.1, 10, 20000)
for iii in rangee:
    x=iii
    y=x*np.log(x)
    a.append(x)
    b.append(y)
plt.plot(a,b,ls='-.',color='black')

for iii in rangee:
    x=iii
    y=np.log(x)
    c.append(x)
    d.append(y)
plt.plot(c,d,ls='-',color='black')

for iii in rangee:
    x=iii
    y=x**3
    e.append(x)
    f.append(y)
plt.plot(e,f,ls='--',color='black')

for iii in rangee:
    x=iii
    y=x**2
    g.append(x)
    h.append(y)
plt.plot(g,h,ls='--',color='blue')

for iii in rangee:
    x=iii
    y=2**x
    i.append(x)
    j.append(y)
plt.ylim((0,max(rangee)*10))
plt.xlim((0,max(rangee)))
plt.plot(i,j,ls=':',color='gray')

plt.legend(('Log-Normal','Log','Cúbica','Quadrática','Exponencial'),title='__Legenda__',)