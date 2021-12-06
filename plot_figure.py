# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:04:02 2021

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np

#criando um gráfico simples

x=np.linspace(0,38,2)
y=x**2

fig_1 = plt.figure(figsize=(5,4),dpi=300)
axes_1 = fig_1.add_axes([0.1,0.1,0.9,0.9])

axes_1.set_xlabel('Days')
axes_1.set_ylabel(' Squared')

axes_1.set_title('Days Squared Chat')
axes_1.plot(x,y,label='x/x²')

axes_1.plot(y,x,label='x²/x')
axes_1.legend(loc=0)

#criando um eixo menor e plotando dentro dele

axes_2 = fig_1.add_axes([0.45,0.45,0.4,0.3])
axes_2.set_xlabel('Days')
axes_2.set_ylabel(' Squared')

axes_2.set_title('Days Squared Chat')
axes_2.plot(x,y,label='x/x²')
axes_2.plot(y/2,x**2,'r')

#colocando um texto qualquer

axes_2.text(0,2000,'Messanesas')# os primeiros campos se referem ao local em relacao aos eixos x e y

