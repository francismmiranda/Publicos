# -*- coding: utf-8 -*-
"""
Created on Sat May 29 23:59:22 2021

@author: user
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data1 = pd.read_csv(r'C:\Users\user\Desktop\Python\Dados_Entrada\chuvamensalCRJ.csv',sep=';',encoding='latin-1',index_col='Estações')

data2=data1.drop(columns=['TOTAL ANUAL',"MÉDIA MENSAL"])

data2=data2.round()

print (data2.head())



fig_1=plt.figure(figsize=(15,8),facecolor='white')


ax = sns.heatmap(data2,cmap='coolwarm',annot=True,annot_kws={'fontsize':8},fmt='.0f',cbar_kws={'label': 'Precipitação (mm)'})
ax.tick_params(left=False, bottom=False,right=False,top=False) ## other options are right and top
plt.xlabel('Meses do ano',labelpad=12)
plt.title('PRECIPITAÇÃO MÉDIA MENSAL')

plt.tight_layout()


fig_1.savefig(r'C:\Users\user\Desktop\Python\Dados_Entrada\chuvamensalcrj.png',dpi=300)




data2=data2.T
data2=data2.corr()

fig_2=plt.figure(figsize=(15,8),facecolor='white')
ax = sns.heatmap(data2,annot=True,cmap='gist_rainbow',annot_kws={'fontsize':8},fmt='.1f',cbar_kws={'label': 'Correlação'})
ax.tick_params(left=False, bottom=False,right=False,top=False) ## other options are right and top
ax.set_xticklabels(ax.get_xticklabels(),rotation=90,horizontalalignment='center')


fig_2.savefig(r'C:\Users\user\Desktop\Python\Dados_Entrada\chuvamensalcrj_Corr.png',dpi=300)