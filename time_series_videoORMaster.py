# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 13:56:53 2021

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\user\Desktop\Python\Tutoriais\timeseries.csv',sep=';',encoding='latin-1')
print(df.info())
#transformar a coluna 'month' para formato de data através da função pd.to_datetime

df['month']=pd.to_datetime(df.month)

#noção das estatísticas principais do dataframe
print(df.describe())

#transformando a coluna 'month' em index. Ou seja, a coluna 'month' não será mais reconhecida como uma coluna normal.
df=df.set_index('month')
#plotando os dados do dataframe.. o index é usado automaticamente como eixo x
#df.plot(figsize=(15,6))

#plotando somente uma variável, no caso 'diet'
#df.diet.plot(figsize=(15,6))

#ANALISANDO TENDÊNCIA

#média móvel da coluna dieta... ao escolher 12, estamos fazendo a MM dos últimos 12 meses
#df.diet.rolling(12).mean().plot(figsize=(15,6))

#dados agrupados por ano específico
#df.diet.groupby(df.index.year).sum().plot(figsize=(15,6))

#ANALISANDO SAZONALIDADE ->usando diferenças sucessivas

print(df.diet.diff())
#df.diet.diff().plot(figsize=(15,6))

#aplicando um filtro para um período específico

filtro = (df.index.year >=2005) & (df.index.year <= 2007)
df[filtro].diet.diff().plot(kind='bar',figsize=(15,6))