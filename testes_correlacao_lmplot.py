# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 21:49:56 2021

@author: user
"""

import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import random
import pandas as pd

pontos = pd.read_csv(r'C:\Users\user\Desktop\Python\MonitoraCorona\DQOtodospontos.csv',sep=';',encoding='latin-1')
pontos = pontos.iloc[:, :-1]
pontos = pontos[pontos['DQO (mg/L)'].notna()]
pontos = pontos[pontos['Esgoto (SST)'].notna()]
pontos['DQO (mg/L)']=pontos['DQO (mg/L)'].astype(float)
pontos['N° de cópias/mL']=pontos['N° de cópias/mL'].astype(float)
pontos["Esgoto (DQO)"] = pontos["Esgoto (DQO)"].astype("category")
pontos["Data"] = pontos["Data"].astype("category")


print (pontos.dtypes)

g = sns.lmplot(x='N° de cópias/mL', y='DQO (mg/L)', data=pontos, col='Data',col_wrap=10,
              height=3, aspect=1)

def annotate(data, **kws):
    r,p= sp.stats.pearsonr(data['N° de cópias/mL'], data['DQO (mg/L)'])
    ax = plt.gca()
    
    ax.text(.05, 0.6, "{}: R = {:.5f}",r,
            transform=ax.transAxes)
    
g.map_dataframe(annotate)