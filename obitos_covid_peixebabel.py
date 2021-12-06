# -*- coding: utf-8 -*-
"""
Created on Mon May 31 11:12:20 2021

@author: user
"""



import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML




obitos_df = pd.read_csv('https://raw.githubusercontent.com/covid19br/covid19br.github.io/master/dados/SRAGs-tabela-last-updated_revised2.csv',sep=',',error_bad_lines=False)

print(obitos_df.head())


datas = obitos_df['Data']
datas = ['/'.join(d.split('/')[::-1]) for d in datas]
obitos_df['Data'] = np.asarray(datas)
obitos_df.drop(0, inplace=True)
print(obitos_df)


dados = obitos_df[['Data', '08/05/20', '27/04/20', '20/04/20']]
dados = dados.melt('Data', var_name='Reporte', value_name='Óbitos')

print(dados.info())

plt.figure(figsize=(15, 5))

sns.barplot(data=dados, x='Data', y='Óbitos', hue='Reporte', dodge=False, palette='husl')
plt.xticks(rotation=90)

plt.close('all')
fig, ax = plt.subplots(figsize=(14, 8))
plt.ylim(0, 300)
plt.xlim(0, 54)
plt.xticks(rotation=90, fontsize=14)
plt.yticks(fontsize=14)

def plot_obitos(idx):

  colunas = obitos_df.columns[::-1]
  dados   = pd.DataFrame(obitos_df[colunas[:idx]])  
  dados['Data'] = obitos_df['Data']

  # Plot do passado
  dados = dados.melt('Data', var_name='Reporte', value_name='Óbitos')
  sns.lineplot(data=dados, x='Data', y='Óbitos', hue='Reporte', ax=ax, palette='Greys', legend=False)
  
  # Plot do presente
  sns.lineplot(data=obitos_df, x='Data', y=obitos_df[colunas[idx]], ax=ax, color='red', legend=False)

  ax.set_title('Reporte de {0}'.format(colunas[idx]), fontsize=18)
  ax.set_ylabel('Óbitos por data do óbito', fontsize=14)
  

anim = animation.FuncAnimation(fig, plot_obitos, frames=25, interval=1000, blit=False)
HTML(anim.to_html5_video())