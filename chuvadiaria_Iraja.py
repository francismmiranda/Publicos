# -*- coding: utf-8 -*-
"""
Created on Sat May 29 23:59:22 2021

@author: user
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data2 = pd.read_csv(r'C:\Users\user\Desktop\Python\Dados_Entrada\chuvadiaria_Iraja.csv',sep=';',encoding='latin-1',index_col='Ano')
print(data2.head())

#data2=data1.drop(columns=['TOTAL ANUAL',"MÉDIA MENSAL"])

#data2=data2.round()

#print (data2.head())


fig1=plt.figure(figsize=(12,5))
#fig_1, (ax0,ax1) = plt.subplots(2,1)

ax1 = sns.heatmap(data2,cmap='crest',vmax=40,annot=False,annot_kws={'fontsize':8},fmt='.0f',cbar_kws={'label': 'Precipitação (mm)'})
ax1.tick_params(left=False, bottom=False,right=False,top=False) ## other options are right and top
plt.xlabel('Dia do Ano',labelpad=12)
plt.title('Precipitação Diária no Posto Irajá')
plt.tight_layout()


fig1.savefig(r'C:\Users\user\Desktop\Python\Dados_Entrada\chuvadiariairaja.png',dpi=300)

