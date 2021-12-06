# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:03:34 2021

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
# Cria um vetor com todos os possíveis valores de r
R = np.linspace(0.5, 2, 20000)

# Inicializa os eixos x e y vazios
X = []
Y = []
# Loop principal (iterar para todo r em R)
for r in R:
 # Adiciona r no eixo x
     X.append(r)
 # Escolhe um valor aleatório entre 0 e 1
     x = np.random.random()
 # Gera população de equilíbrio
     for l in range(1000):
         x=r*x*(1-x**9)
     Y.append(x)
# Plota o gráfico sem utilizar retas ligando os pontos
plt.plot(X, Y, ls='', marker=',')
plt.show()
