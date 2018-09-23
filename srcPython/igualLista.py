def igualLista(lista_a, lista_b):
    if(len(lista_a)==len(lista_b)):
        for i in range(len(lista_a)):
            if(lista_a[i]!=lista_b[i]):
                return False
    else:
        return False
    return True

print(igualLista(["Hola","Mundo"],["Mundo","Hola"]))