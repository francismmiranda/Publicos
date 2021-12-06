# -*- coding: utf-8 -*-
"""
Created on Thu May 20 16:26:09 2021

@author: user
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data4 = pd.read_csv(r'C:\Users\user\Desktop\Python\Dados_Entrada\teste_correl.csv',sep=';',encoding='latin-1')

print(data4.head())

data5 = data4.sort_values(by='ETE Pavuna')
print (data5.head())
nparr = data5.values

x1 = nparr[:,0]
x2 = nparr[:,6]

fig5 = plt.figure(figsize=(3,3),dpi=200)
ax5 = fig5.add_axes([0,0,1,1])
ax5.plot(x1,x2)

ax5.text(0,90,'vixe')
ax5.text(0,100,r'$\alpha \beta \lambda$')
ax5.text(30,120,r'$\delta_i \gamma^{ij} \sum_{i=0}^\infty x_i \frac {3}{4}$')
ax5.text(35,140, r'$\frac{8 - \frac{x}{5}}{8} \sqrt{9} \sin(\pi) \sqrt{3}{8} \acute a \div$')
ax5.text(50,60, r'$\bar a \hat a \tilde a \vec a \overline {a} a \lim_{x \to 2} f(x) = {4} $')
ax5.text(75,20, r'$\geq \leq \neq \{=} $')
ax5.annotate('testando2',xy=(x1.max(),len(x2)),xytext=(90,80),arrowprops=dict(facecolor='black',shrink=0.05))