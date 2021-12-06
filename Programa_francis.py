# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 18:31:56 2014

@author: Francis
"""
##PROGRAMA PARA SOLUÇÃO DE PROBLEMAS DE TRANSPORTE ADVECTIVO-DIFUSIVO
##PELO MÉTODO DAS DIFERENÇAS FINITAS
#Aluno: Francis Martins Miranda
#Disciplina: Métodos Numéricos em Recursos Hídricos
#Prof.: Renato Elias

import math
import numpy as np
import matplotlib.pyplot as plt

#Varáveis e parâmetros da equação de transporte advectivo-difusivo#
n=161
kt=0.0001
d=0.05
L=2.0
u=1.0
h=L/(n-1)
k = 1.0
t = 0
tf=1
d = 0.05

#Calculando os coeficientes da Matriz A
def A():
    return -((u*kt)/(2*h)+(d*kt)/(h**2))
    
def B():
    return (kt/kt)+(2*d*kt)/(h**2)
    
def C():
    return -((u*kt)/(2*h)-(d*kt)/(h**2))
        
# Construindo a matriz com os coeficientes -> Matriz Identidade
def matrizidentidade():
    return B()*np.eye(n, k=0)+(A())*np.eye(n, k=-1)+(C())*np.eye(n, k=1)
    
# Aplicando a Solução analítica, ao invés da condição incial para gerar a matriz B
def solanalitica(x):
    return math.exp(-4*(np.pi**2)*d*(k**2)*t)*math.sin(2*np.pi*k*(x-u*tf))
    
# Condição de Contorno
def condicaocontorno(x):
    return math.exp(-4*(np.pi**2)*d*(k**2)*t)*math.sin(2*np.pi*k*(x-u*tf))


def calculo():  
    x= 0
    matriz1 = [] 
    for i in range(0,n):
        x=i*h
        matriz1.append(solanalitica(x)) 
        x=x+h
    return matriz1
  
def matrizB():
    matriz = []
    for i in range(0,n):
        x=i*h
        matriz.append(condicaocontorno(x))
        x=x+h        
    return matriz
     
# Resolvendo o sistema de equações X = A*B
def resolve(matrizA, matrizB):
    return np.linalg.solve(matrizA, matrizB)
    
def resultados():
#Calculando o X 
    A=matrizidentidade()
    B=matrizB()
    resultado=[]
    resultado.append(B)
    #calculando os coef. de acordo com delta t. obs: alteração manual delta t
    for i in range(0,2000):
           B=resolve(A,B)
           resultado.append(B)
           plt.plot(B)
           
    an=calculo() #calculo é a solucao analítica
    i=0
    somatorio=0
    for i in range(0,n):
        diferencaerro=B[i]-an[i]
        somatorio+=diferencaerro #fazendo o somatório das diferenças para cada "n"
        Erro=h*np.square(somatorio)      
        return  resultado,Erro,somatorio      
        
W,Erro,somatorio=resultados()
print (W)
print ("para h=", h ,"o erro é:",Erro)