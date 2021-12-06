# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:15:50 2021

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np

#criando um gráfico simples

x=np.linspace(0,38,2)
y=x**2

fig_1, (axes_1,axes_2) = plt.subplots(figsize=(16,8),nrows=2,ncols=2)
plt.tight_layout()

axes_2[1].set_title('Plot2')
axes_2[1].set_xlabel('X')
axes_2[1].set_ylabel('eixo UUs')
axes_2[1].plot(x,y,'r',label='rerer')

axes_2[0].plot(x,y,color='navy',alpha=0.5, lw=3,ls='-.',marker='o',markersize=2,
               markerfacecolor='y',markeredgecolor='y',markeredgewidth=4)

axes_2[0].set_xlim([0,50])
axes_2[0].set_ylim([0,1000])
axes_2[0].grid(True, color='0.6',dashes=(5,2,1,2))
axes_2[0].set_facecolor('#FAEBD7')
plt.tight_layout()

fig_1.savefig(r'C:\Users\user\Desktop\Python\3plotsdeteste.png',dpi=300)  