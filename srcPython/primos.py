import esPrimo as p

def primos(num):
    lista = []
    numero = 1
    while(len(lista)<num):
        if(p.esPrimo(numero)):
            lista.append(numero)
        numero = numero + 1
    return lista

print(primos(100))
