# -*- coding: utf-8 -*-
"""
Created on Thu May 20 23:12:07 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

arr1 = np.random.randint(1,7,6000)
arr2 = np.random.randint(1,7,6000)
arr3 = arr1+arr2

fig3 = plt.hist(arr3, bins=5,density=True,stacked=True, cumulative=False,orientation='horizontal',histtype='step',color='orange')

plt.xlabel('sasasasas')
plt.ylabel('KKKKKrynig')
plt.xtitle('asassa')
plt.text(0.03, 4, 'dsdsd')


