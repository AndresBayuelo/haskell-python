# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 22:15:55 2018

@author: natal
"""
def maximo(lista):
    maxi = lista[0]
    for num in lista:
        if maxi < num:
            maxi= num
    return maxi


print (maximo ([78,24,56,93,21,237,46,74,125]))