def contarPares(lista):
    cont = 0
    for x in lista:
        if( x%2==0 ):
            cont = cont + 1
    return cont

print(contarPares([2,4,3,6,8]))