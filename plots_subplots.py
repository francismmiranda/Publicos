# -*- coding: utf-8 -*-
"""
Created on Wed May 19 23:26:03 2021

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np

#criando um gráfico simples

x=np.linspace(0,38,2)
y=x**2
plt.plot(x,y)
plt.title("Função x²")
plt.xlabel("Valores de x")
plt.ylabel(len(x),labelpad=2)

print("O valor máximo da série é:",int(x.mean()),". O Valor máximo da série é:", x.max())

#criando um subplot mas só posso adicionar uma função por subplot
plt.figure(figsize=(20,20))
plt.subplot(3,2,1)
plt.plot(x,y/4,'g')
plt.plot(x,y/3,'b')

plt.subplot(3,2,2)
plt.bar(x,y)
plt.plot(x,y/5,'b')
plt.ylim((0,600))
plt.yticks((0,100,200,300,400,500,600))
plt.xticks([0,2,10,25])

plt.subplot(3,1,2)
plt.plot(x,y,'r',label="Vermelho",)
plt.plot(x,y/2,'g',label="Verde")
plt.plot(x,y/3,'b',label="Azul")
plt.xlabel("Xlabel")
plt.xlim((0,20))
plt.title("Tituloss")
plt.legend()
plt.ylabel("caraca")
plt.tight_layout()

#criando uma figura tenho mais

"""fig = plt.Figure(figsize=(10,8),dpi=300)
ax = fig.add_axes([0.1,0.1,0.9,0.9])
ax.plot(x,y,label='xy normal')
ax.plot(x,y/2,label='xy/2')

ax2= fig.add_axes([0.45,0.45,0.3,0.3])
ax2.plot(x/2,y*2,label='xylouco')"""

#link pra continuar https://www.youtube.com/watch?v=wB9C0Mz9gSo&t=1157s
