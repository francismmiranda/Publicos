# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:35:12 2021

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['figure.figsize'] = (20.0, 10.0)
plt.rcParams['font.family'] = "serif"

data1 = pd.read_csv(r'C:\Users\user\Desktop\Python\MonitoraCorona\Dados_Semanas.csv',sep=';',encoding='latin-1',index_col='Semana Epidem.')


data1=data1.fillna(0)

pavuna = data1['ETE Pavuna'].tolist()
penha=data1['ETE Penha'].tolist()


fig, (ax1, ax2, ax3) = plt.subplots(figsize=(5,3),nrows=3,ncols=3,sharex=True,sharey=True)

ax1[0].plot(data1['Data'],penha)
ax1[0].set_title('Penha')
ax1[1].plot(data1['Data'],pavuna)
ax1[1].set_title('Pavuna')

ax2[2].plot(data1['Data'],pavuna)
ax2[2].set_title('Pavuna')

ax2[1].plot(data1['Data'],pavuna)
ax2[1].set_title('Pavuna')



fig.tight_layout()
plt.show()

"""
fig, axs = plt.subplots(ncols=len(data1.columns)-2, figsize=(20,2),sharey=(True))
data1.plot(subplots=True, ax=axs)
plt.legend(loc=1)
plt.xticks(data1.index)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10,10))
for i, col in enumerate(data1.columns):
    plt.subplot(2,5,i+1)
    plt.plot(data1.index, data1[col], label=col)
    plt.xticks(data1.index)
    plt.legend(loc='upper left')
    plt.tight_layout()
plt.show()

"""
