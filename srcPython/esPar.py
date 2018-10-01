# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 23:12:37 2018

@author: natal
"""



def esPar(lista):
    enumerar = []
    for i in lista:
        if i % 2 == 0:
            enumerar.append(i)
    return enumerar
print(esPar([1, 2, 3, 4, 5, 6, 7, 8, 9,10]))

         
