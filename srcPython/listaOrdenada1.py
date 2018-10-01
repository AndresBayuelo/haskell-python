# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 19:54:10 2018

@author: natal
"""

def ordenarLista(lista):
    if not lista:
        return []
    return (ordenarLista([x for x in lista[1:] if x <  lista[0]])+ [lista[0]] +ordenarLista([x for x in lista[1:] if x >= lista[0]]))
listaMal = ['B', 'D', 'A', 'E', 'C']
listaBien=['A', 'B', 'C', 'D', 'E']
ListaPRO   = ordenarLista(listaMal)

print (ListaPRO)