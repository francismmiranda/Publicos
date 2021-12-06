# -*- coding: utf-8 -*-
"""
Created on Thu May 20 23:29:01 2021

@author: user
"""

import matplotlib.pyplot as plt

z = ['Barcelona','Rio de Janeiro','Duque de Caxias','Caracas']
z_1 = [23,222,12,111]
erro=[1,4,1,4]


plt.bar(z,z_1,color='purple',yerr=erro)
plt.tight_layout()

z_2=[12,88,23,11]
z_3=100-z_2



print(z.type())