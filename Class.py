# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 16:09:37 2021

@author: user
"""

class Rio:
    def __init__(self,declividade,estado,variacaoH):
        self.declividade = declividade
        self.estado = estado
        self.variacaoH = variacaoH
        
    def Considerar(self):
        print (
            'Declividade igual a =',self.declividade,'\n'
            'Rio X está sendo considerado')
        

Rio1=Rio(0.112,'RJ',22)
Rio2=Rio(0.44,'SP',223)
Rio1.Considerar()       